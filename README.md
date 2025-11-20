# 🛰️ Global Atmospheric CO₂ Simulations with IAP-AACM Using an Improved Vertical Diffusion Scheme and Multi-Source Evaluation*

**Institute of Atmospheric Physics, Chinese Academy of Sciences (CAS-IAP)**
**Correspondence:** [wangzhe@mail.iap.ac.cn](mailto:wangzhe@mail.iap.ac.cn), [zifawang@mail.iap.ac.cn](mailto:zifawang@mail.iap.ac.cn)

---

## 📘 Overview

This repository provides the **software description**, **data references**, and **reproducibility information** for the study:

**Global Atmospheric CO₂ Simulations with the IAP-AACM Model using an Improved Vertical Diffusion Scheme and Evaluation with Multi-Source Data**

The research enhances **IAP-AACM** (Institute of Atmospheric Physics Aerosol and Atmospheric Chemistry Model) by implementing a **new vertical diffusion scheme** based on **Mixing-Length Theory** under **stable boundary layer (SBL)** conditions.

This improvement corrects the common **overestimation of nighttime CO₂ near the surface** found in many chemical transport models (CTMs), leading to significantly improved agreement with multi-platform CO₂ observations.

---

## ✨ Key Features

* **New SBL vertical diffusion scheme** improves PBL mixing representation
* Corrects **overestimated nighttime CO₂** in stable boundary layers
* **Ten-year global simulation (2010–2019)**
* Validation against multi-source datasets:

  * NOAA GML surface CO₂
  * GLOBALVIEWplus ObsPack
  * OCO-2 XCO₂ (2015–2019)
  * Aircraft vertical profiles
* **High-accuracy global XCO₂ simulation**

  * *r = 0.97*, *RMSE = 1.08 ppm*, *NMB = 0.06%*
* Outperforms NOAA CarbonTracker CT2022 at **non-assimilated sites** (e.g., TAP, UTA)

---

## 🧠 Model Description: IAP-AACM

IAP-AACM is a global-to-regional aerosol and atmospheric chemistry model derived from **GNAQPMS**. It includes:

* Positive-definite, mass-conservative advection
* Gas-, liquid-, heterogeneous-chemistry modules
* Aerosol thermodynamics and secondary organic aerosols
* Dry & wet deposition
* Two-way nested grid capability
* Turbulent diffusion schemes based on Monin–Obukhov theory (original)
* **New SBL scheme based on Mixing-Length Theory** (this work)

The improved scheme increases vertical diffusivity under stable conditions, preventing excessive nighttime CO₂ accumulation.

---

## 📊 Evaluation Datasets

This study uses **publicly accessible datasets**, including:

### **CarbonTracker CT2022**

* NOAA global CO₂ reanalysis
* Initial fields + fluxes
* [https://carbontracker.noaa.gov](https://carbontracker.noaa.gov)

### **OCO-2 XCO₂ (V11.1r)**

* NASA GES DISC
* Column-averaged CO₂ (2015–2019)
* [https://disc.gsfc.nasa.gov](https://disc.gsfc.nasa.gov)

### **NOAA GML Surface CO₂**

* Global monthly mean CO₂ at WMO GAW sites
* [https://gml.noaa.gov](https://gml.noaa.gov)

### **GLOBALVIEWplus ObsPack (v8.0)**

* Multi-platform atmospheric CO₂ (surface, aircraft, flask)
* [https://gml.noaa.gov/ccgg/obspack/](https://gml.noaa.gov/ccgg/obspack/)

---

## 🌍 Main Results

### **1. Surface CO₂**

* IAP-AACM accurately captures monthly variability across global GML sites.
* Outperforms CT2022 at non-assimilated sites (e.g., TAP, UTA).

### **2. Vertical Profiles**

* Strong agreement with aircraft observations (GLOBALVIEW).
* Corrects excessive nighttime surface CO₂ in CT2022 by enhancing SBL mixing.

### **3. XCO₂ (Column CO₂)**

* High skill matching OCO-2 retrievals (2015–2019):

  * **r = 0.97**
  * **RMSE = 1.08 ppm**
  * **NMB = 0.06%**
* Successfully reproduces global spatial patterns and seasonal cycles.

### **4. Long-term Stability**

* Ten-year simulation demonstrates robust climatological performance.

---

## 📁 Software Availability

IAP-AACM is developed at the **Institute of Atmospheric Physics, Chinese Academy of Sciences**.

Model source codes are available **upon reasonable request** to the corresponding authors according to institutional policy.

---

## 📂 Data Availability

All datasets used in this research are publicly available:

| Dataset                     | Access Link                                                              |
| --------------------------- | ------------------------------------------------------------------------ |
| CarbonTracker CT2022        | [http://carbontracker.noaa.gov](http://carbontracker.noaa.gov)           |
| OCO-2 XCO₂ V11.1r           | [https://disc.gsfc.nasa.gov](https://disc.gsfc.nasa.gov)                 |
| NOAA GML Surface CO₂        | [https://gml.noaa.gov](https://gml.noaa.gov)                             |
| GLOBALVIEWplus ObsPack v8.0 | [https://gml.noaa.gov/ccgg/obspack/](https://gml.noaa.gov/ccgg/obspack/) |

Details on how these datasets were used can be found in the manuscript.

---

## 📝 Citation

If you use the materials or findings in this repository, please cite:

> *Global Atmospheric CO₂ Simulations with the IAP-AACM Model using an Improved Vertical Diffusion Scheme and Evaluation with Multi-Source Data.*

---

## 👥 Authors

* Zhiyin Zou
* Zhe Wang\*
* Xueshun Chen
* Xu Zhou
* Huansheng Chen
* Zijian Jiang
* Zifa Wang

\*Corresponding authors

---

## 🏛️ Funding

This research was supported by:
**National Key Research and Development Program of China** (2022YFC3703401)

---

## 🙏 Acknowledgments

We acknowledge the support of the
**National Large Scientific and Technological Infrastructure “Earth System Numerical Simulation Facility”**
([https://cstr.cn/31134.02.EL](https://cstr.cn/31134.02.EL)).
