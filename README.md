![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Wind Power Density Calculator
 
*For renewable energy analysts and wind farm planners: enter average wind speed and Weibull shape factor to instantly compute wind power density and turbine class suitability.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Renewable Energy Site Assessment
 
The tool computes wind power density (WPD) at hub height from user-supplied wind statistics. Inputs: (1) average wind speed (m/s, float 0-30, required), (2) Weibull shape parameter k (float 1.0-3.5, default 2.0), (3) air density ρ (kg/m³, float 0.8-1.5, default 1.225). Core logic: From average wind speed V_avg and shape k, estimate the Weibull scale parameter c = V_avg / Γ(1 + 1/k). Then mean of cubed wind speed E[v³] = c³ * Γ(1 + 3/k). WPD = 0.5 * ρ * E[v³], output in W/m². Classification uses standard NREL wind power class boundaries: Class 1 (<200), Class 2 (200-300), Class 3 (300-400), Class 4 (400-500), Class 5 (500-600), Class 6 (600-800), Class 7 (≥800). Additionally, if class ≥3, show 'Suitable for utility-scale turbines'; otherwise 'Marginal / small turbines only'. Gradio UI layout: three numeric input boxes in a row (wind speed, shape k, air density) with a 'Calculate' button. Outputs appear below: (a) large numeric readout of WPD with label 'Wind Power Density (W/m²)', (b) a plain-text classification line (e.g., 'Class 4: Good'), (c) a suitability statement, and (d) a horizontal bar chart (using matplotlib) showing the WPD value as a colored bar over the class thresholds, with dashed lines at each class boundary. No AI/ML component—pure deterministic calculation using the gamma function.
 
## Run it
 
```bash
docker build -t wind-power-density-calculator .
docker run -p 7860:7860 wind-power-density-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-23.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
