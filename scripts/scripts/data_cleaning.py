"""
data_cleaning.py
----------------
Handles data loading, column standardization, date parsing,
reshaping (melt), and attendance status mapping.
"""

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Strip spaces and standardize column names."""
    df.columns = df.columns.astype(str).str.strip()
    return df


def identify_date_columns(df: pd.DataFrame) -> list:
    """Identify columns that represent dates."""
    return [
        col for col in df.columns
        if col not in ['Employee Code', 'Name', 'source_month']
        and pd.to_datetime(col, errors='coerce') is not pd.NaT
    ]


def melt_attendance_data(df: pd.DataFrame) -> pd.DataFrame:
    """Convert wide attendance table into long format."""
    date_columns = identify_date_columns(df)

    df_melted = df.melt(
        id_vars=['Employee Code', 'Name', 'source_month'],
        value_vars=date_columns,
        var_name='date',
        value_name='status'
    )

    df_melted['date'] = pd.to_datetime(df_melted['date'], errors='coerce')
    return df_melted


def map_attendance_status(df: pd.DataFrame) -> pd.DataFrame:
    """Map raw attendance codes to readable labels."""
    status_map = {
        'P': 'Present',
        'WFH': 'Work From Home',
        'WO': 'Week Off',
        'PL': 'Paid Leave',
        'SL': 'Sick Leave',
        'LWP': 'Leave Without Pay',
        'ML': 'Maternity Leave',
        'BL': 'Bereavement Leave',
        'FFL': 'Festival Leave'
    }

    df['status'] = df['status'].map(status_map)
    return df
