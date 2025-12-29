"""
AtliQ HR Attendance Analytics (Apr–Jun 2022)
Run Pipeline Script

This script demonstrates how to use the modular code inside /scripts:
- data_cleaning.py
- kpi_calculations.py
- visualizations.py

Note:
You must update EXCEL_FILE and SHEET_NAMES to match your local file path and sheet names.
"""

from pathlib import Path

import pandas as pd

from scripts.data_cleaning import (
    standardize_columns,
    reshape_attendance_to_long,
    map_status_codes,
)
from scripts.kpi_calculations import (
    monthly_kpis,
    wfh_wfo_monthly_percent,
    sick_leave_monthly_percent,
)
from scripts.visualizations import (
    plot_wfh_wfo_by_month,
    plot_sick_leave_by_month,
)

# =========================
# 1) CONFIG (EDIT THESE)
# =========================
EXCEL_FILE = Path("attendance_data.xlsx")  # <-- change to your real file name/path
SHEET_NAMES = {
    "2022-04": "Apr 2022",
    "2022-05": "May 2022",
    "2022-06": "June 2022",
}
HEADER_ROW = 1  # <-- if your headers start on row 2 in Excel, header=1 is correct


def load_month_sheets(excel_path: Path, sheet_names: dict, header_row: int = 1) -> list[pd.DataFrame]:
    """Load each month sheet and add source_month column."""
    dfs = []
    for month_key, sheet in sheet_names.items():
        df = pd.read_excel(excel_path, sheet_name=sheet, header=header_row)
        df = standardize_columns(df)
        df["source_month"] = month_key
        dfs.append(df)
    return dfs


def main():
    if not EXCEL_FILE.exists():
        raise FileNotFoundError(
            f"Excel file not found: {EXCEL_FILE}\n"
            "Update EXCEL_FILE to the correct file name/path."
        )

    # =========================
    # 2) LOAD + CLEAN
    # =========================
    dfs = load_month_sheets(EXCEL_FILE, SHEET_NAMES, header_row=HEADER_ROW)
    df_all = pd.concat(dfs, ignore_index=True)

    # =========================
    # 3) RESHAPE (MELT)
    # =========================
    df_long = reshape_attendance_to_long(df_all)

    # =========================
    # 4) MAP STATUS CODES
    # =========================
    df_long = map_status_codes(df_long)

    # =========================
    # 5) KPI CALCULATIONS
    # =========================
    kpis = monthly_kpis(df_long)
    wfh_wfo = wfh_wfo_monthly_percent(df_long)
    sick_leave = sick_leave_monthly_percent(df_long)

    print("\n=== Monthly KPI Summary ===")
    print(kpis)

    print("\n=== WFH vs WFO % by Month ===")
    print(wfh_wfo)

    print("\n=== Sick Leave % by Month ===")
    print(sick_leave)

    # =========================
    # 6) PLOTS
    # =========================
    plot_wfh_wfo_by_month(wfh_wfo)
    plot_sick_leave_by_month(sick_leave)


if __name__ == "__main__":
    main()
