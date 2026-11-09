# -*- coding: utf-8 -*-
"""mark_water_h.py — помечает протоны гостевой воды как Hw в CIF-файле.

Зачем: FastConduct выбирает подвижный вид только по символу элемента, а цифры
в метке вырезает (H1/H2 -> H). Поэтому, чтобы считать диффузию протонов воды
и не тащить в расчёт структурные водороды (C-H, N-H, O-H каркаса, гидроксиды),
протоны воды нужно пометить отдельным символом — Hw.

Правило: кислород, у которого ровно два водорода в пределах 1.25 A, считается
молекулой воды; её водороды получают Hw (ключ --ow дополнительно помечает
кислород воды как Ow). Всё остальное не меняется.

Использование:
    python mark_water_h.py вход.cif [выход.cif] [--ow]

Выход: CIF в P1 с явными координатами и метками Hw/Ow.
ВНИМАНИЕ: Hw и Ow — не химические элементы. VESTA/ASE/pymatgen такой файл
не откроют, в DFT его подавать нельзя. Перед DFT сделайте обратную замену
Hw -> H (и Ow -> O): mark_water_h.py --unmark вход.cif
"""
import re
import sys

import numpy as np
from ase.io import read, write

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

OH_MAX = 1.25      # A, порог O-H
CH_MAX = 1.35      # A, порог C-H (для отчёта)


def normalize_cif(path):
    """loop_ с тегами в одной строке -> разносим (GSAS2CIF/FullProf)."""
    txt = open(path, encoding="utf-8", errors="replace").read()
    out = []
    for raw in txt.splitlines():
        s = raw.strip()
        if s.startswith("loop_") and len(s.split()) > 1:
            parts = s.split()
            out.append(parts[0])
            out.extend(parts[1:])
        else:
            out.append(raw)
    tmp = path + ".normalized.cif"
    open(tmp, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    return tmp


def load(path):
    try:
        return read(normalize_cif(path))
    except Exception as e1:
        try:
            from pymatgen.core import Structure
            s = Structure.from_file(normalize_cif(path))
            from ase import Atoms
            return Atoms(species=[str(x) for x in s.species],
                         positions=s.cart_coords, cell=s.lattice.matrix, pbc=True)
        except Exception as e2:
            raise SystemExit(f"не удалось прочитать {path}:\n ASE: {e1}\n pymatgen: {e2}")


def unmark(path, out=None):
    """Обратная замена Hw -> H, Ow -> O (для DFT)."""
    txt = open(path, encoding="utf-8", errors="replace").read()
    n_hw = len(re.findall(r"\bHw(\d+)", txt))
    n_ow = len(re.findall(r"\bOw(\d+)", txt))
    txt = re.sub(r"(?<![\w])Hw(\d+)", r"H\1", txt)
    txt = re.sub(r"(?<![\w])Ow(\d+)", r"O\1", txt)
    txt = txt.replace("Hw", "H").replace("Ow", "O")
    out = out or path.replace(".cif", "_plain.cif")
    open(out, "w", encoding="utf-8", newline="\n").write(txt)
    print(f"обратная замена: Hw -> H ({n_hw}), Ow -> O ({n_ow})")
    print(f"записано: {out}")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__)
        return 1

    if "--unmark" in flags:
        unmark(args[0], args[1] if len(args) > 1 else None)
        return 0

    src = args[0]
    dst = args[1] if len(args) > 1 else src.replace(".cif", "_Hw.cif")

    atoms = load(src)
    sym = np.array(atoms.get_chemical_symbols())
    d = atoms.get_all_distances(mic=True)
    frac = atoms.get_scaled_positions(wrap=True)

    o_idx = [i for i, s in enumerate(sym) if s == "O"]
    h_idx = [i for i, s in enumerate(sym) if s == "H"]
    c_idx = [i for i, s in enumerate(sym) if s == "C"]
    n_idx = [i for i, s in enumerate(sym) if s == "N"]

    # к какому тяжёлому атому привязан каждый H
    partner = {}
    for i in h_idx:
        cand = [(d[i, j], sym[j], j) for j in range(len(atoms))
                if j != i and sym[j] in ("O", "C", "N", "S")]
        cand = [c for c in cand if c[0] < 1.45]
        if cand:
            cand.sort()
            partner[i] = cand[0]

    water = {}          # индекс O -> список индексов H
    for i in h_idx:
        if i in partner and partner[i][1] == "O" and partner[i][0] < OH_MAX:
            water.setdefault(partner[i][2], []).append(i)
    water_os = [o for o, hs in water.items() if len(hs) == 2]
    hydroxy_os = [o for o, hs in water.items() if len(hs) == 1]

    water_h = {h for o in water_os for h in water[o]}
    structural_h = [i for i in h_idx if i not in water_h]

    print(f"файл: {src}")
    print(f"  атомов: {len(atoms)}  (O {len(o_idx)}, H {len(h_idx)}, C {len(c_idx)}, N {len(n_idx)})")
    print(f"  молекул воды (O с двумя H): {len(water_os)}  ->  протонов воды: {len(water_h)}")
    print(f"  OH-групп (O с одним H):     {len(hydroxy_os)}")
    print(f"  структурных H (остаются H): {len(structural_h)}")
    if not water_os:
        print("\nВНИМАНИЕ: молекул воды не найдено — Hw не появится.")
        print("Если вода в структуре есть, проверьте, что водороды воды вообще заданы в CIF")
        print("(часто их не уточняют по порошковым данным — тогда воду нужно достроить).")

    # --- запись ---
    mark_o = "--ow" in flags
    out_sym = list(sym)
    for i in water_h:
        out_sym[i] = "Hw"
    if mark_o:
        for o in water_os:
            out_sym[o] = "Ow"

    from collections import Counter as _Counter
    _comp = _Counter(out_sym)
    formula_str = " ".join(f"{el}{n}" for el, n in sorted(_comp.items()))
    counter = {}
    lines = ["data_fastconduct_Hw", "",
             f"_chemical_formula_sum    '{formula_str}'",
             f"_cell_length_a    {atoms.cell.cellpar()[0]:.6f}",
             f"_cell_length_b    {atoms.cell.cellpar()[1]:.6f}",
             f"_cell_length_c    {atoms.cell.cellpar()[2]:.6f}",
             f"_cell_angle_alpha    {atoms.cell.cellpar()[3]:.6f}",
             f"_cell_angle_beta     {atoms.cell.cellpar()[4]:.6f}",
             f"_cell_angle_gamma    {atoms.cell.cellpar()[5]:.6f}",
             "_symmetry_space_group_name_H-M    'P 1'",
             "_symmetry_Int_Tables_number       1",
             "loop_", "  _symmetry_equiv_pos_as_xyz", "  'x, y, z'", "",
             "loop_",
             "  _atom_site_label", "  _atom_site_type_symbol",
             "  _atom_site_fract_x", "  _atom_site_fract_y", "  _atom_site_fract_z",
             "  _atom_site_occupancy"]
    for i in range(len(atoms)):
        el = out_sym[i]
        counter[el] = counter.get(el, 0) + 1
        x, y, z = frac[i] % 1.0
        lines.append(f"  {el}{counter[el]:<5d} {el:<3s} {x:.6f} {y:.6f} {z:.6f} 1.0000")
    lines.append("")
    open(dst, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print(f"\nзаписано: {dst}")
    print(f"  метки: " + ", ".join(f"{k}{v}" for k, v in sorted(counter.items())))
    print("\nВ программе: рабочий ион = Hw, заряд = +1.")
    print("Перед DFT: python mark_water_h.py --unmark " + dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
