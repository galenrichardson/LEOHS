# 🌍 LEOHS: Landsat Harmonization Toolkit (Support Repository)

This repository contains **support files** for the [LEOHS Python package](https://pypi.org/project/leohs/), and related publications. The paper explaining the LEOHS tool can be found here: **[A tool for global and regional Landsat 7 and Landsat 8 cross-sensor harmonization](https://doi.org/10.1080/10106049.2025.2538108)**.

> 📦 **Installation and full documentation** are available on the PyPI project page:  
> 🔗 [https://pypi.org/project/leohs](https://pypi.org/project/leohs)

---

## 📁 Repository Contents

- **`Global_Harmonization_functions_SRandTOA.txt`**  
  A set of globally derived regression equations to harmonize Landsat 7 and 8 reflectance values.

- **`WRS_overlaps.zip`**  
  A shapefile containing the **WRS-2 Overlap zones**.  
  Use this to confirm that your Area of Interest (AOI) intersects a valid overlap region.

- **`apply_leohs.ipynb`**  
  A Jupyter notebook that can be used to **apply LEOHS regression equations** to multiband imagery.

- **`apply_harmonization_XGB.ipynb`**  
  A Jupyter notebook that can be used to **apply LEOHS XGB models** to multiband imagery.

- **`Incorporating Multiple Bands and Land Cover Improves Cross-Sensor Normalization`**  
  This folder contains data and notebooks used to make this publication.

---
