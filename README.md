# ⚡ FastConduct

<p align="center">
  <img src="logo.png" alt="FastConduct Logo" width="150">
</p>

<p align="center">
  <b>Ionic Conductivity Calculator using Kinetic Monte Carlo (kMC)</b>
</p>

<p align="center">
  <a href="https://yelizmorkhova.github.io/FastConduct/">
    <img src="https://img.shields.io/badge/Website-Visit-blue?style=for-the-badge&logo=github" alt="Website">
  </a>
  <a href="https://github.com/YelizMorkhova/FastConduct/releases">
    <img src="https://img.shields.io/badge/Releases-Latest-green?style=for-the-badge&logo=github" alt="Releases">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge" alt="License">
  </a>
</p>

---

## 📥 Download

| Platform | Download | Size |
|----------|----------|------|
| 🪟 **Windows 10 / 11 (64-bit)** | [FastConduct.exe](https://github.com/YelizMorkhova/FastConduct/releases/download/v1.2/FastConduct.exe) | 57 MB |

> **Note**: Windows only. Windows 7 and 8 are **not supported** (the application is built on Python 3.12+).
> Linux and macOS versions are planned for future releases.

### 🔐 Verify your download

`FastConduct.exe` — v1.2, 60 141 667 bytes. SHA-256:

```
c6c1dac8e13615265a03ff8e7a537d98123af65b30690b5d9643c021160c39dd
```

Check it in PowerShell, from the folder where you saved the file:

```powershell
Get-FileHash .\FastConduct.exe -Algorithm SHA256
```

The hash printed by PowerShell must match the value above. If it does not, do not run the file —
download it again from the official release page.

The executable is not code-signed, so Windows SmartScreen may show *"Windows protected your PC"*.
Click **More info** → **Run anyway** to start the program.

---

## 🚀 Features

- ✅ **Multi-format**: VASP POSCAR/CONTCAR, CIF files
- ✅ **BKL kMC algorithm**: Bortz–Kalos–Lebowitz kinetic Monte Carlo
- ✅ **1D/2D/3D diffusion**: Supports all dimensionalities
- ✅ **Ion-ion repulsion**: Configurable alpha and cutoff
- ✅ **Arrhenius plots**: Automatic visualization with error bars
- ✅ **CIF export**: Vacancy structures for DFT
- ✅ **User-friendly GUI**: CustomTkinter interface

### 🩹 What's new in v1.2

- **Robust CIF reader**: `loop_` tags written on one line (GSAS2CIF, FullProf), rows of neighbouring
  data loops are no longer read as atoms, several `data_` blocks, Cartesian coordinates
  (`_atom_site_Cartn_*`), positions on the cell boundary merged correctly, and the atom count is
  cross-checked against `_chemical_formula_sum`.
- **CIF export**: real cell angles for hexagonal / monoclinic / triclinic cells (plus `_cell_volume`).
- **`Hw` convention for guest-water protons**: label the two H of each water molecule as `Hw`, select
  `Hw` as the working ion with charge +1 — structural C–H / N–H / O–H groups then stay out of the
  jump network. The helper script `mark_water_h.py` does the relabelling automatically.
- **“Save plot → PDF”** works again.

---

## 💻 System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10 / 11 (64-bit) |
| **RAM** | 4 GB minimum, 8 GB recommended |
| **Disk space** | ~200 MB free space (the single `.exe` unpacks itself to a temporary folder on start) |
| **Download** | 57 MB, no installer |

---

## 🎮 Quick Start

1. Download **FastConduct.exe**
2. Run the executable (no installation required)
3. Load a structure (POSCAR/CIF)
4. Set parameters & run the simulation

---

## 📖 Documentation

- 📄 [User Manual (PDF)](https://github.com/YelizMorkhova/FastConduct/raw/main/Manual_v.1.2.pdf)
- 🌐 [Website](https://yelizmorkhova.github.io/FastConduct/)

---

## 📝 Citation

No peer-reviewed paper yet. If you use FastConduct in your research, please cite the software entry
below — and let me know, so your paper can be listed on the website.

```bibtex
@software{morkhova2026fastconduct,
  author  = {Morkhova, Yelizaveta A.},
  title   = {FastConduct: Ionic Conductivity Calculator using Kinetic Monte Carlo},
  year    = {2026},
  version = {1.2},
  url     = {https://github.com/YelizMorkhova/FastConduct}
}
```

---

## 📜 License

Proprietary — see [LICENSE](LICENSE) for the exact terms.

## 📬 Contact

[ORCID](https://orcid.org/0000-0002-5243-296X) ·
[ResearchGate](https://www.researchgate.net/profile/Yelizaveta-Morkhova) ·
[eliztimofeeva@mail.ru](mailto:eliztimofeeva@mail.ru)
