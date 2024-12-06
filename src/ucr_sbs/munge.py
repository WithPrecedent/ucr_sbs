"""Cleans and organizes data"""

from __future__ import annotations
import copy

import numpy as np
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
    columns = copy.deepcopy(options.offenses)
    columns.extend(['Total Violent Crime', 'Total Property Crime'])
    for column in columns:
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

def separate_total_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """separate_total_data _summary_

    Args:
        df: _description_

    Returns:
        _description_
    """
    total = df[df['State'].isna()]
    total = total.assign(State = 'US')
    total = total.assign(**{'State Name': 'United States'})
    original = df.drop(df[df['State'].isna()].index)
    return total, original

def get_rape_original_to_revised_ratio(df: pd. DataFrame) -> float:
    """get_rape_original_to_revised_ratio _summary_

    Args:
        df: _description_

    Returns:
        _description_
    """
    revised = df.loc[
        df['Rape (revised) Rate'].notna() & df['Rape (original) Rate'].notna(),
        'Rape (revised) Rate'].mean()
    original = df.loc[
        df['Rape (original) Rate'].notna() & df['Rape (revised) Rate'].notna(),
        'Rape (original) Rate'].mean()
    return original/revised

def impute_missing_rape_data(row: pd.Series, ratio: float) -> pd.Series:
    """impute_missing_rape_data _summary_

    Args:
        row: _description_
        ratio: _description_

    Returns:
        _description_
    """
    if row['Rape (revised) Rate'] and pd.isna(row['Rape (original) Rate']):
        row['Rape (original) Rate'] = ratio * row['Rape (revised) Rate']
    elif pd.isna(row['Rape (revised) Rate']) and row['Rape (original) Rate']:
        row['Rape (revised) Rate'] = row['Rape (original) Rate'] / ratio
    return row

def add_missing_rape_data(df: pd.DataFrame, total: pd.DataFrame) -> pd.DataFrame:
    """add_missing_data _summary_

    Args:
        df: _description_
        total: _description_

    Returns:
        _description_
    """
    ratio = get_rape_original_to_revised_ratio(total)
    return df.apply(impute_missing_rape_data, axis = 1, ratio = ratio)

