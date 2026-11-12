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
| 🪟 **Windows 10 / 11 (64-bit)** | [FastConduct.exe](https://github.com/YelizMorkhova/FastConduct/releases/download/v1.2.1/FastConduct.exe) | 57 MB |

> **Note**: Windows only. Windows 7 and 8 are **not supported** (the application is built on Python 3.12+).
> Linux and macOS versions are planned for future releases.

### 🔐 Verify your download

`FastConduct.exe` — v1.2.1, 60 142 073 bytes. SHA-256:

```
e99e45513a04edb14e86bc951915af499dbfbf275440d9f64580ab2c01a73c5f
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

### 🩹 What's new in v1.2.1

- **Diffusion coefficient from the slope of MSD(t)**: the conductivity is now computed from the
  linear fit of the mean-squared displacement instead of its last point, and the MSD linearity
  (`R²`) is printed in the report — you can see when the trajectory has not reached the diffusive
  regime yet. The Haven ratio is still assumed `H_R = 1` (stated in the report).
- First paper using FastConduct: Orlova et al., *Tuning electronic and ionic conductivity in
  ZnFe₂O₄ spinel via Sn doping for Zn-ion cathodes: the role of cation defects*,
  J. Phys. Chem. Solids **222** (2027) 114290, [doi:10.1016/j.jpcs.2026.114290](https://doi.org/10.1016/j.jpcs.2026.114290).

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
  version = {1.2.1},
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
