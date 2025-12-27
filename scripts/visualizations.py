"""
visualizations.py
-----------------
All charting/plotting functions for the AtliQ HR Attendance Analytics project.
Uses Matplotlib only (clean + portable for GitHub).
"""

from __future__ import annotations

from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt


def _ensure_month_label_index(df: pd.DataFrame, month_col: str = "month") -> pd.DataFrame:
    """
    Ensures a clean month label index like 'Apr 2022', 'May 2022', etc.
    Accepts either:
      - index as 'YYYY-MM' (string), or
      - a 'month' column containing 'YYYY-MM'
    """
    out = df.copy()

    if month_col in out.columns:
        base = out[month_col].astype(str)
    else:
        base = out.index.astype(str)

    # Convert 'YYYY-MM' -> datetime -> 'Mon YYYY'
    month_dt = pd.to_datetime(base + "-01", errors="coerce")
    month_label = month_dt.dt.strftime("%b %Y")

    # If conversion failed for some reason, fallback to the original string
    month_label = month_label.fillna(base)

    out.index = month_label
    return out


def plot_wfh_wfo_by_month(
    wfh_wfo_month: pd.DataFrame,
    title: str = "WFH vs WFO % by Month",
    figsize: tuple[int, int] = (10, 5),
    rotation: int = 0,
    ylim: Optional[tuple[float, float]] = (0, 100),
) -> None:
    """
    Expects a dataframe like:
        index: month (YYYY-MM or Month labels)
        columns: ['WFH', 'WFO']  (percentages)
    """
    plot_df = _ensure_month_label_index(wfh_wfo_month)

    ax = plot_df.plot(kind="bar", figsize=figsize, title=title)

    ax.set_xlabel("Month")
    ax.set_ylabel("Percentage (%)")
    ax.set_xticklabels(plot_df.index, rotation=rotation)

    if ylim is not None:
        ax.set_ylim(ylim)

    plt.tight_layout()
    plt.show()


def plot_single_kpi_by_month(
    kpi_series: pd.Series,
    title: str = "KPI % by Month",
    ylabel: str = "Percentage (%)",
    figsize: tuple[int, int] = (10, 5),
    rotation: int = 0,
    show_labels: bool = True,
) -> None:
    """
    Plots a single KPI series (e.g., Sick Leave % by month).
    Expects index: 'YYYY-MM' and values as percentage numbers (0-100 or 0-1 depending on your calc).

    If your KPI is 0-100, labels show like 1.29%
    If your KPI is 0-1, multiply before passing or adapt your KPI calculation.
    """
    plot_df = kpi_series.reset_index()
    plot_df.columns = ["month", "value"]

    plot_df["month_label"] = pd.to_datetime(plot_df["month"] + "-01", errors="coerce").dt.strftime("%b %Y")
    plot_df["month_label"] = plot_df["month_label"].fillna(plot_df["month"].astype(str))

    ax = plot_df.plot(
        x="month_label",
        y="value",
        kind="bar",
        figsize=figsize,
        legend=False,
        title=title,
    )

    ax.set_xlabel("Month")
    ax.set_ylabel(ylabel)
    ax.set_xticklabels(plot_df["month_label"], rotation=rotation)

    # Optional % labels above bars
    if show_labels:
        for i, v in enumerate(plot_df["value"].tolist()):
            ax.text(i, v, f"{v:.2f}%", ha="center", va="bottom")

    plt.tight_layout()
    plt.show()

