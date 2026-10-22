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
    <img src="https://img.shields.io/github/downloads/YelizMorkhova/FastConduct/total?style=for-the-badge&logo=github&label=Downloads" alt="Downloads">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge" alt="License">
  </a>
</p>

---

## 📥 Download

| Platform | Download | Size |
|----------|----------|------|
| 🪟 **Windows 10 / 11 (64-bit)** | [FastConduct.exe](https://github.com/YelizMorkhova/FastConduct/releases/download/v1.1/FastConduct.exe) | 57 MB |

> **Note**: Windows only. Windows 7 and 8 are **not supported** (the application is built on Python 3.12+).
> Linux and macOS versions are planned for future releases.

### 🔐 Verify your download

`FastConduct.exe` — v1.1, 60 138 616 bytes. SHA-256:

```
4f7b164f89acc9e6609c2541b9bb98e72366cbe2bdecd974c5e5f6389a11c09f
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

### 🩹 Fixed in the current v1.1 build

- **CIF export**: correct cell angles for non-orthorhombic cells (hexagonal, monoclinic, triclinic).
  Previously `alpha` / `beta` / `gamma` were always written as 90°, so the exported structure could not
  be used for DFT. Lengths and angles are now computed from the actual supercell vectors, and
  `_cell_volume` is written as well.
- **Save plot → PDF** no longer fails.

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

- 📄 [User Manual (PDF)](https://github.com/YelizMorkhova/FastConduct/raw/main/Manual_1.1.pdf)
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
  version = {1.1},
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
