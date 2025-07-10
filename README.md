# 🌍 LEOHS: Landsat Harmonization Toolkit (Support Repository)

This repository contains **support files** for the [LEOHS Python package](https://pypi.org/project/leohs/), a tool for harmonizing Landsat imagery using Google Earth Engine.

> 📦 **Installation and full documentation** are available on the PyPI project page:  
> 🔗 [https://pypi.org/project/leohs](https://pypi.org/project/leohs)

---

## 📁 Repository Contents

- **`Global_Harmonization_functions_SRandTOA.txt`**  
  A set of globally derived regression equations to harmonize Landsat 7 ↔ 8 reflectance values under different conditions.

- **`WRS_overlaps.zip`**  
  A shapefile containing the **WRS-2 Overlap zones**, required for LEOHS.  
  Use this to confirm that your Area of Interest (AOI) intersects a valid overlap region.

- **`apply_leohs.ipynb`**  
  A Jupyter notebook that demonstrates how to **apply LEOHS regression equations** to multiband imagery.

---

## 📌 Note

This repository **does not contain the core LEOHS tool** — it is distributed through PyPI.  
You must install it via:

```bash
pip install leohs
