"""Cleans and organizes data"""

from __future__ import annotations

from numpy import int64
import pandas as pd

from . import options



def remove_comma_separators(df: pd.DataFrame) -> pd.DataFrame:
    """remove_comma_separators _summary_

    Args:
        df: _description_

    Returns:
        _description_
    """
    for column in options.violent_crime_numericals:
        df[column] = df[column].replace(',', '', regex = True)
    return df

def change_types(df: pd.DataFrame) -> pd.DataFrame:
    """change_to_numeric _summary_

    Args:
        df: _description_

    Returns:
        _description_
    """
    for column in options.violent_crime_numericals:
        df[column] = pd.to_numeric(
            df[column],
            errors = 'coerce',
            downcast = 'integer')
    return df

def add_rate_column(
    df: pd.DataFrame,
    count_column: str,
    rate_suffix: str = 'Rate') -> pd.DataFrame:
    """add_rate_column

    Args:
        df: _description_
        count_column: _description_
        rate_suffix: _description_. Defaults to 'Rate'.

    Returns:
        _description_
    """
    rate_column_name = ' '.join([count_column, rate_suffix])
    df[rate_column_name] = df[count_column]/df['Population']*100000
    return df

def add_rate_columns(df: pd.DataFrame) -> pd.DataFrame:
    """add_rate_columns _summary_

    Args:
        df: _description_

    Returns:
        _description_
    """
    for column in options.offenses:
        df = add_rate_column(df, column)
    return df

def reshape_long(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """reshape_long _summary_

    Args:
        df: _description_
        columns: s

    Returns:
        _description_
    """
    return pd.lreshape(df, columns)

def reshape_wide(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """make_wide _summary_

    Args:
        df: _description_
        columns: s

    Returns:
        _description_

    """
    return pd.pivot(df, columns = columns)
