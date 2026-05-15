<p align="center">
  <img src="https://img.shields.io/badge/LANGUAGE-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/DOMAIN-HR%20Analytics-7C3AED?style=for-the-badge" />
  <img src="https://img.shields.io/badge/WORKFLOW-Data%20Pipeline-F97316?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LIBRARY-pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/VISUALIZATION-Matplotlib-2563EB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/STATUS-Completed-16A34A?style=for-the-badge" />
</p>

---

# 📊 AtliQ HR Attendance Analytics

An end-to-end Python analytics project focused on workforce attendance analysis, hybrid work trends, and HR KPI monitoring using data cleaning, transformation, and visualization techniques.

<p align="center">
  <img src="AtliQ_HR_Attendance_Banner_README.jpg" width="850">
</p>

---

## 📌 Problem Statement

Organizations operating in hybrid work environments require visibility into employee attendance behavior, work-from-home adoption, leave trends, and workforce engagement patterns.

AtliQ Technologies needed a data-driven analytics solution capable of transforming raw attendance records into actionable workforce insights to support HR planning and operational decision-making.

---

## 🎯 Project Objective

Design and develop a Python-based HR analytics workflow to:

- Analyze employee attendance trends  
- Monitor Work-from-Home (WFH) adoption patterns  
- Evaluate leave utilization and absenteeism trends  
- Generate KPI-driven workforce insights  
- Support data-driven HR planning and reporting  

---

## ⚡ Solution Overview

Built an end-to-end attendance analytics pipeline using Python and Pandas to process and analyze over 20,000 attendance records across a 3-month period (April–June 2022).

The workflow includes:

- Data cleaning and standardization  
- KPI engineering and trend analysis  
- Attendance and leave behavior analysis  
- Workforce insight generation  
- Data visualization using Matplotlib  

---

## 🚀 Project Highlights

- Processed and analyzed **20,000+ attendance records**
- Built an end-to-end analytics pipeline (**Excel → Python → Insights**)
- Identified increasing hybrid work adoption trends
- Generated workforce KPIs for HR reporting
- Designed modular Python scripts for scalable analysis workflows

---

## 🛠 Tools & Technologies

- **Python** – Data analysis and workflow automation  
- **Pandas** – Data cleaning and transformation  
- **NumPy** – Numerical processing  
- **Matplotlib** – Data visualization and charting  
- **Excel** – Source data management  
- **Jupyter Notebook** – Exploratory analysis and development  

---

## 📌 Key KPIs Generated

### Workforce Metrics
- Attendance %
- Work From Home (WFH) %
- Work From Office (WFO) %
- Sick Leave %
- Paid Leave %

---

## 📊 KPI Summary (3-Month Average)

| KPI | Value |
|---|---|
| Attendance Rate | 91.7% |
| WFH Rate | 10.3% |
| WFO Rate | 81.4% |
| Sick Leave Rate | 1.3% |
| Paid Leave Rate | 4.0% |

---

## 🛠 Analytics Workflow

1. Imported attendance records from Excel  
2. Cleaned and standardized raw datasets  
3. Reshaped attendance data for analysis  
4. Mapped attendance and leave categories  
5. Calculated workforce KPIs  
6. Generated trend visualizations  
7. Derived HR and workforce insights  

---

## 💡 Key Business Insights

### Hybrid Work Trends
- WFH adoption increased steadily from April to June, indicating growing hybrid work flexibility.

### Attendance Behavior
- Slight attendance decline was primarily associated with increased paid leave usage.

### Leave Analysis
- Sick leave peaked during May, potentially reflecting seasonal or workforce health factors.

### Workforce Planning
- Attendance insights can support staffing optimization and workforce planning decisions.

---

## 📈 Visualizations

### WFH vs WFO Analysis
<p align="center">
  <img src="assets/charts/wfh_wfo.png" width="700">
</p>

---

### WFH Trend Over Time
<p align="center">
  <img src="assets/charts/wfh_trend.png" width="700">
</p>

---

### Workforce Absenteeism Analysis
<p align="center">
  <img src="assets/charts/leave_distribution.png" width="400">
</p>

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

## 🤝 Connect With Me
🌐 LinkedIn: https://www.linkedin.com/in/asimahmedio
💻 GitHub: https://github.com/asimahmedhub
✉️ Email: asim.atia@gmail.com
