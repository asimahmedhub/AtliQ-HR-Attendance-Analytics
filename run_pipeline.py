"""
AtliQ HR Attendance Analytics (Apr–Jun 2022)
Run Pipeline Script
"""

from pathlib import Path
import pandas as pd

from scripts.data_cleaning import (
    clean_column_names,
    melt_attendance_data,
    map_attendance_status,
)
from scripts.kpi_calculations import (
    calculate_attendance_kpis,
    monthly_kpi,
)
from scripts.visualizations import (
    plot_wfh_wfo_by_month,
    plot_single_kpi_by_month,
)

# =========================
# 1) CONFIG
# =========================


EXCEL_FILE = Path(r"C:\Users\Asim\Desktop\Attendance-Sheet-2022-2023.xlsx")

SHEET_NAMES = {
    "2022-04": "Apr 2022",
    "2022-05": "May 2022",
    "2022-06": "June 2022",
}

HEADER_ROW = 1


def load_month_sheets():
    """Load all monthly sheets"""
    dfs = []

    for month_key, sheet in SHEET_NAMES.items():
        df = pd.read_excel(EXCEL_FILE, sheet_name=sheet, header=HEADER_ROW)
        df = clean_column_names(df)
        df["source_month"] = month_key
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def main():
    if not EXCEL_FILE.exists():
        raise FileNotFoundError(f"File not found: {EXCEL_FILE}")

    # =========================
    # 2) LOAD + CLEAN
    # =========================
    df_all = load_month_sheets()

    # =========================
    # 3) RESHAPE
    # =========================
    df_long = melt_attendance_data(df_all)

    # =========================
    # 4) MAP STATUS
    # =========================
    df_long = map_attendance_status(df_long)

    # Add month column
    df_long["month"] = df_long["date"].dt.to_period("M").astype(str)

    # =========================
    # 5) KPI CALCULATIONS
    # =========================
    overall_kpi = calculate_attendance_kpis(df_long)
    sick_leave = monthly_kpi(df_long, "Sick Leave")

    print("\n=== Overall KPI ===")
    print(overall_kpi)

    print("\n=== Sick Leave % by Month ===")
    print(sick_leave)

    # =========================
    # 6) WFH vs WFO
    # =========================
    wfh_wfo = (
        df_long[df_long["status"].isin(["Present", "Work From Home"])]
        .assign(work_type=lambda x: x["status"].replace({
            "Present": "WFO",
            "Work From Home": "WFH"
        }))
        .groupby(["month", "work_type"])
        .size()
        .groupby(level=0)
        .apply(lambda x: x / x.sum() * 100)
        .unstack()
        .round(2)
    )

    print("\n=== WFH vs WFO % ===")
    print(wfh_wfo)

    # =========================
    # 7) VISUALIZATION
    # =========================
    plot_wfh_wfo_by_month(wfh_wfo)
    plot_single_kpi_by_month(sick_leave, "Sick Leave % by Month")


if __name__ == "__main__":
    main()
