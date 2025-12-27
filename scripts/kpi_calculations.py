"""
KPI Calculations Module
-----------------------
Contains reusable functions for calculating
attendance, WFH, WFO, and leave-based KPIs.
"""

import pandas as pd


def calculate_attendance_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates overall attendance-related KPIs.

    Attendance = Present + Work From Home
    """

    total_days = len(df)

    present = df[df["status"] == "Present"].shape[0]
    wfh = df[df["status"] == "Work From Home"].shape[0]
    wfo = present
    sick = df[df["status"] == "Sick Leave"].shape[0]
    paid = df[df["status"] == "Paid Leave"].shape[0]

    results = {
        "Attendance % (Present + WFH)": round(((present + wfh) / total_days) * 100, 2),
        "WFH % of working days": round((wfh / total_days) * 100, 2),
        "WFO % of working days": round((wfo / total_days) * 100, 2),
        "Sick Leave % of working days": round((sick / total_days) * 100, 2),
        "Paid Leave % of working days": round((paid / total_days) * 100, 2),
    }

    return pd.DataFrame.from_dict(results, orient="index", columns=["Value"])


def monthly_kpi(df: pd.DataFrame, status: str) -> pd.Series:
    """
    Calculates monthly percentage KPI for a given status.
    Example: Sick Leave %, WFH %, Paid Leave %
    """

    monthly = (
        df.assign(flag=df["status"].eq(status))
        .groupby("month")["flag"]
        .mean()
        .mul(100)
        .round(2)
    )

    return monthly

