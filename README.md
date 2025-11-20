# IAP-AACM: Aerosol and Atmospheric Chemistry Model

**Institute of Atmospheric Physics, Chinese Academy of Sciences**

---

## 🌍 Model Overview

**IAP-AACM** (Institute of Atmospheric Physics Aerosol and Atmospheric Chemistry Model) is an atmospheric chemistry and aerosol model independently developed by the **Institute of Atmospheric Physics, Chinese Academy of Sciences (CAS)**.  
It originated from the **Global Nested Air Quality Prediction Modeling System (GNAQPMS)** — a three-dimensional Eulerian atmospheric chemical transport model with multi-scale grid resolution based on the continuity equation  
(*Z. Wang et al., 2014; Chen et al., 2015; Wei et al., 2019*).

---

## ⚙️ Model Improvement

In this study, we improve **IAP-AACM** by implementing a **new vertical diffusion scheme** based on **Mixing-Length Theory** under **stable boundary layer (SBL)** conditions.  
This new scheme corrects the common **overestimation of CO₂ concentrations within the SBL**.

---

## 🧪 Model Validation

We validated the model against a suite of multi-source observations, including:
- Ground-based stations  
- Aircraft measurements  
- Satellite observations  
- Reanalysis datasets  

Compared to the **CarbonTracker reanalysis**, which tends to overestimate CO₂ at several non-assimilated ground sites, **IAP-AACM** shows:
- Superior agreement with ground and aircraft observations  
- High accuracy against satellite-derived **XCO₂** values  
  - **Correlation (R): 0.97**  
  - **RMSE: 1.08 ppm**  
  - **NMB: 0.06%**

---

## 📈 Key Results

**IAP-AACM** effectively captures:
- Global spatial distribution of CO₂  
- Temporal variability of atmospheric CO₂  

These results establish **IAP-AACM** as a robust and reliable tool for **carbon cycle research** and **climate mitigation analysis**.

---

## 📚 References

> Wei et al., 2019  
> Wang, Z. et al., 2014  
> Chen, et al., 2015  

---

## 🧑‍💻 Contact

For questions, collaboration, or data requests, please contact:  
📧 [IAPZZY@icloud.com](mailto:IAPZZY@icloud.com)

---

## 🪪 License

This repository and associated materials are released under the **MIT License** (see `LICENSE` for details).
