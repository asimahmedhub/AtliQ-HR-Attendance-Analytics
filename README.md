## 📊 AtliQ HR Attendance Analytics

<p align="center"> <img src="AtliQ_HR_Attendance_Banner_README.jpg" width="800"> </p>




## 📊 Python-Based HR Attendance Insights (Apr–Jun 2022)

This project analyzes 3 months of employee attendance data for AtliQ Technologies, delivering insights into:

📅 Monthly attendance patterns

🏠 WFH vs 🏢 WFO behavior

🤒 Sick leave trends

🎯 Productivity & leave impact

📉 Early warning indicators for employee disengagement

---

The full analysis was performed using Python (Pandas, NumPy, Matplotlib) to demonstrate end-to-end:

✔ Data cleaning

✔ Data transformation

✔ KPI engineering

✔ Insights & visualization

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

Average Attendance %: 91.70%

Average WFH %: 10.28%

Average WFO %: 81.42%

Average Sick Leave %: 1.29%

Average Paid Leave %: 3.95%

---

## 🛠 Project Workflow

Steps	Description
1. Data Import	Loaded April, May, June sheets from Excel

2. Cleaning & Standardization	Fixed column names, removed noise, unified date formats

3. Reshaping Data	Converted daily attendance columns → long-format dataset

4. Status Mapping	Replaced codes (P, WFH, SL, etc.) with meaningful labels

5. KPI Calculation	Monthly & overall KPIs computed dynamically

6. Visualizations	Trend charts & summary dashboards

7. Insight Building	Identified patterns & HR-relevant findings

---
 
## 💡 Insights Overview

Here are examples of insights revealed:

📈 WFH increased month-by-month, indicating rising hybrid adoption

🏢 WFO steadily decreased, hinting at shifting workforce preference

🤒 Sick leave spiked in May, suggesting wellness issues or seasonal patterns

📉 Attendance dipped slightly, driven mostly by paid leave

---

## 📈 Visualizations & Insights

### 1️⃣ WFH vs WFO % by Month
<img src="assets/charts/wfh_wfo_monthly.png" width="500"/>

**Insight:**  
A clear upward trend in **WFH adoption** is observed from April to June, while WFO gradually declines — indicating increasing hybrid flexibility.

---

### 2️⃣ Sick Leave % by Month
<img src="assets/charts/sick_leave_monthly.png" width="500"/>

**Insight:**  
Sick leave peaks in May and stabilizes in June, which could indicate seasonal or workload-related factors.

---

## 📂 Repository Structure
AtliQ-HR-Attendance-Analytics/
│

├── notebooks/
│   └── AtliQ_HR_Attendance_Analysis.ipynb
│

├── scripts/

│  ├── data_cleaning.py
│  ├── kpi_calculations.py
│  ├── visualizations.py
│  └── utils.py

│
├── assets/│   

├── AtliQ_HR_Attendance_Banner_README.jpg
│   └── charts/
│      ├── wfh_wfo_monthly.png
│     └── sick_leave_monthly.png
│

├── README.md

└── requirements.txt

---

## 🧠 Code Structure

- `notebooks/` → Exploratory analysis & KPI derivation
- `scripts/` → Modular Python code for cleaning, KPI calculation, and visualization
- `assets/` → Charts and visual assets used in the analysis

---

## 👨‍💻 Developed By

Asim Ahmed — Data Analyst

📧 Email: asim.atia@gmail.com

🔗 GitHub: https://github.com/asimahmedhub

🔗 LinkedIn: (Add your link)
