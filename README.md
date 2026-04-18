![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📊 End-to-End HR Attendance Analytics (Python Project)
📊 Python | Pandas | Data Analytics | HR Insights

<p align="center">
  <img src="AtliQ_HR_Attendance_Banner_README.jpg" width="800">
</p>
 


---

## 📌 Project Overview

This project analyzes employee attendance data for AtliQ Technologies over a 3-month period (April–June 2022).

The goal is to uncover workforce behavior patterns, measure hybrid work adoption, and provide data-driven insights to support HR decision-making.

Key focus areas include:
- Attendance performance tracking  
- Work-from-Home (WFH) vs Work-from-Office (WFO) trends  
- Leave behavior analysis (Sick Leave & Paid Leave)  
- Workforce engagement insights  

The project is built as an end-to-end Python analytics pipeline, covering data cleaning, transformation, KPI engineering, and visualization.

---

## 🚀 Project Highlights

- 📊 Processed and analyzed **20,000+ attendance records**
- 🔄 Built an **end-to-end data pipeline** (Excel → Python → Insights)
- 📈 Identified **increasing WFH adoption trend (~50% growth)**
- 🧠 Generated **actionable HR insights for workforce planning**
- 🛠 Designed **modular, production-style Python code structure**

---

## 🛠 Technologies Used

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib  
- **Environment:** Jupyter Notebook  
- **Techniques:**  
  - Data Cleaning & Transformation  
  - KPI Engineering  
  - Time-Series Analysis  
  - Data Visualization  

---

## 📌 Key KPIs Generated

### Monthly KPIs
- **Attendance %** (Present + Work From Home)
- **WFH %** — Hybrid work adoption trend
- **WFO %** — Office attendance trend
- **Sick Leave %** — Health-related leave behavior
- **Paid Leave %** — Scheduled leave impact

---


## 🧮 3-Month KPI Summary (Overall)

- **Average Attendance:** 91.7%  
- **Average WFH:** 10.3%  
- **Average WFO:** 81.4%  
- **Average Sick Leave:** 1.3%  
- **Average Paid Leave:** 4.0%  

---

## 🛠 Project Workflow

1. **Data Import** — Loaded April, May, June sheets from Excel  
2. **Cleaning & Standardization** — Fixed column names and formats  
3. **Reshaping Data** — Converted wide → long format  
4. **Status Mapping** — Replaced codes (P, WFH, SL) with labels  
5. **KPI Calculation** — Computed monthly and overall metrics  
6. **Visualization** — Generated trend charts  
7. **Insight Generation** — Derived HR insights  

---
 
## 💡 Insights Overview

- 📈 WFH adoption increased steadily, indicating a shift toward hybrid work  
- 🏢 WFO declined correspondingly, reflecting changing workplace preferences  
- 🤒 Sick leave peaked in May, suggesting potential seasonal or health-related factors  
- 📉 Slight attendance dip observed, primarily driven by paid leave usage  

---

## 📸 Dashboard Preview

<p align="center">
  <img src="assets/charts/wfh_wfo.png" width="600">
</p>

---

## 📈 Visualizations & Insights

### 1️⃣ WFH vs WFO % by Month
<p align="center">
  <img src="assets/charts/wfh_wfo.png" width="650">
</p>
 
📊 Insight:

Work-from-Home (WFH) adoption increases steadily from April to June, indicating a shift toward hybrid work flexibility.

---

### 2️⃣ WFH Trend Over Time
<p align="center">
  <img src="assets/charts/wfh_trend.png" width="650">
</p>

📈 Insight: 

WFH usage shows consistent growth with daily fluctuations, becoming more prominent toward June.

---

### 3️⃣ Workforce Absenteeism Analysis
<p align="center">
  <img src="assets/charts/leave_distribution.png" width="350">
</p>

📉 Insight:

Sick Leave (SL) represents the largest share of absences, highlighting health-related factors as the primary driver of employee absence.

---


## 📂 Repository Structure

<pre>
AtliQ-HR-Attendance-Analytics/
│
├── data/
│   └── attendance_data.xlsx
│
├── notebooks/
│   └── AtliQ_HR_Attendance_Analysis.ipynb
│
├── scripts/
│   ├── data_cleaning.py
│   ├── kpi_calculations.py
│   ├── visualizations.py
│   └── utils.py
│
├── assets/
│   ├── AtliQ_HR_Attendance_Banner_README.jpg
│   └── charts/
│       ├── wfh_wfo.png
│       ├── wfh_trend.png
│       └── leave_distribution.png
│
├── run_pipeline.py
├── requirements.txt
└── README.md
</pre>

---

## 🧠 Code Structure

- `notebooks/` → Exploratory analysis & KPI derivation
- `scripts/` → Modular Python code for cleaning, KPI calculation, and visualization
- `assets/` → Charts and visual assets used in the analysis

---

## 🧩 Python Code Organization

- **`data_cleaning.py`**  
  Handles column standardization, date parsing, reshaping (melt), and status mapping.

- **`kpi_calculations.py`**  
  Contains reusable functions for calculating attendance, WFH, WFO, sick leave, and paid leave KPIs.

- **`visualizations.py`**  
  Generates all charts used in the analysis using Matplotlib.

- **`utils.py`**  
  Helper functions to keep code modular and clean.

---

## 🚀 How to Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/asimahmedhub/AtliQ-HR-Attendance-Analytics.git
cd AtliQ-HR-Attendance-Analytics

```

### 2. Install dependencies
```bash
pip install -r requirements.txt

```

### 3. Update the Excel file path inside run_pipeline.py
```python
 EXCEL_FILE = Path("data/attendance_data.xlsx")

```

### 4. Run the pipeline
```bash
python run_pipeline.py

```

### 5. Explore the notebook version
```bash
jupyter notebook

```


---

## 🎯 Business Recommendations

- Encourage flexible work policies to support increasing WFH adoption  
- Monitor sick leave trends to identify potential health risks  
- Use attendance insights for workforce planning and resource allocation  

---

## 👨‍💻 Developed By

Asim Ahmed  
📊 Data Analyst | Aspiring Data Engineer  

📧 Email: asim.atia@gmail.com

🔗 GitHub: https://github.com/asimahmedhub

🔗 LinkedIn: https://www.linkedin.com/in/asimahmedio
