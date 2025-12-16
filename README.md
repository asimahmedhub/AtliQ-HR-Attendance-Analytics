📊 AtliQ HR Attendance Analytics
<p align="center"> <img src="https://raw.githubusercontent.com/asimahmedhub/AtliQ-HR-Attendance-Analytics/main/Phoenix_10_A_clean_modern_2D_digital_banner_for_a_data_analyti_3.jpg" alt="AtliQ HR Attendance Analytics Banner" width="100%"> </p>

## 🧠 Python-Based Attendance Insights (Apr–Jun 2022)

This project analyzes 3 months of employee attendance data for AtliQ Technologies, delivering insights on:

🟢 Attendance patterns

🏠 WFH vs WFO trends

🤒 Sick leave behavior

⚠️ Potential early retention-risk signals

📈 Month-wise KPI tracking

📊 Quarterly summary dashboard


## The analysis was performed entirely using Python (Pandas, Matplotlib) to demonstrate:

✔ End-to-end data cleaning
✔ Transformation & preparation
✔ KPI generation
✔ Visualization
✔ Insight extraction

📁 Project Structure
📦 AtliQ-HR-Attendance-Analytics
│
├── 01_AtliQ_HR_Attendance_EDA.ipynb                 → Data cleaning & preparation

├── 02_AtliQ_HR_Attendance_Visualization.ipynb       → KPI charts & insights

├── attendance_data.xlsx                              → Raw dataset

├── Phoenix_10_A_clean_modern_banner.jpg             → Project banner

├── utils.py                                          → Helper functions

└── README.md                                         → Documentation


## 🔧 Technologies Used
Category	Tools
Language	Python
Libraries	Pandas, NumPy, Matplotlib
Environment	Jupyter Notebook
Techniques	Data Cleaning, KPI Engineering, Visualization


## 📌 Key KPIs Generated
Monthly KPIs
KPI	Description
Attendance %	Present + Work From Home
WFH %	Hybrid work trend
WFO %	Office attendance trend
Sick Leave %	Health leave trend
Paid Leave %	Scheduled leave impact


# 📊 KPI Dashboard (Apr–Jun 2022)

(Add your exported KPI dashboard image here once ready)

Example placeholder:

<p align="center"> <img src="kpi_dashboard.png" width="80%"> </p>


## 📈 Monthly Visualizations
✔ WFH vs WFO % by Month

Shows shift toward increasing hybrid work.

✔ Sick Leave % by Month

Highlights spikes that may indicate burnout or seasonal illness.

✔ Attendance Behavior

Breakdown of presence, leave types, and work modes.

All charts are included in the visualization notebook.


## 🧹 Data Preparation Summary

This project included full data-wrangling steps:

Removed unwanted formatting from Excel sheets

Standardized column names across all months

Combined April, May, and June sheets into one dataset

Normalized attendance codes (P, WO, WFH, SL, PL, etc.)

Converted date columns to proper datetime

Melted daily columns into a tidy long format

Added month & week fields for analysis

Computed working day percentages and all KPIs



## 📌 3-Month Summary (Quarterly Insights)

Some example insights:

WFH increased month-over-month, reaching its highest in June

Sick Leave peaked in May, indicating possible workload stress

Average attendance remained above 90%, showing consistent workforce reliability

Paid Leave increased in June, aligning with mid-year leave cycles



## 🧑‍💻 Developed By

Asim Ahmed — Data Analyst
Python • Data Cleaning • Attendance Analytics • Visualization
