## 📊 AtliQ HR Attendance Analytics

<p align="center"> <img src="AtliQ_HR_Attendance_Banner_README.jpg" width="800"> </p>



## ✨ Project Highlights

- Converted raw multi-sheet Excel attendance logs into an analysis-ready dataset  
- Built modular Python scripts for data cleaning, KPI calculations, and visualizations  
- Generated monthly insights on attendance, WFH/WFO trends, and sick leave patterns  
- Structured the project for reproducibility using a pipeline script (`run_pipeline.py`)  
- Designed as a portfolio-ready project demonstrating real-world data analytics workflow  



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
![WFH vs WFO](assets/charts/wfh_wfo.png)
 
📊 Insight:

Work-from-Home (WFH) adoption shows a steady upward trend from April to June, increasing from approximately 9% to 15%. Meanwhile, Work-from-Office (WFO) declines correspondingly.

This indicates a gradual organizational shift toward hybrid work flexibility, with employees increasingly adopting remote work over time.

---

### 2️⃣ WFH Trend Over Time
![WFH Trend](assets/charts/wfh_trend.png)

📈 Insight: 

WFH adoption shows a gradual upward trend over time, with noticeable day-to-day fluctuations. The increase becomes more consistent toward June, indicating growing acceptance of remote work.

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


1. Clone the repository

```bash
git clone https://github.com/asimahmedhub/AtliQ-HR-Attendance-Analytics.git
cd AtliQ-HR-Attendance-Analytics

   
2. Install dependencies

   pip install -r requirements.txt


3. Update the Excel file path inside run_pipeline.py

  EXCEL_FILE = Path(r"C:\Users\Asim\Desktop\Attendance-Sheet-2022-2023.xlsx")


4. Run the pipeline

python run_pipeline.py


5. explore the notebook version
jupyter notebook


### Then:
- Scroll down
- Click **Commit changes**
- Use this commit message:
```text
Add how to run section to README
---


## 👨‍💻 Developed By

Asim Ahmed — Data Analyst

📧 Email: asim.atia@gmail.com

🔗 GitHub: https://github.com/asimahmedhub

🔗 LinkedIn: (Add your link)
