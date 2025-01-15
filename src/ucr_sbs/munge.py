"""Cleans and organizes data"""

from __future__ import annotations

import copy

import numpy as np
import pandas as pd

from . import options

# def remove_comma_separators(df: pd.DataFrame) -> pd.DataFrame:
#     """remove_comma_separators _summary_

#     Args:
#         df: _description_

#     Returns:
#         _description_
#     """
#     for column in options.violent_crime_numericals:
#         df[column] = df[column].replace(',', '', regex = True)
#     return df

# def trim_state_names(df: pd.DataFrame) -> pd.DataFrame:
#     """_summary_

#     Args:
#         df (pd.DataFrame): _description_

#     Returns:
#         pd.DataFrame: _description_

#     """
#     df['State Name'] = df['State Name'].apply(lambda x: x.strip())
#     return df

# def change_types_to_numerics(df: pd.DataFrame) -> pd.DataFrame:
#     """change_to_numeric _summary_

#     Args:
#         df: _description_

#     Returns:
#         _description_
#     """
#     for column in options.violent_crime_numericals:
#         df[column] = pd.to_numeric(
#             df[column],
#             errors = 'coerce',
#             downcast = 'integer')
#     return df

# def add_rate_column(
#     df: pd.DataFrame,
#     count_column: str,
#     rate_suffix: str = options.rate_suffix) -> pd.DataFrame:
#     """add_rate_column

#     Args:
#         df: _description_
#         count_column: _description_
#         rate_suffix: _description_. Defaults to 'Rate'.

#     Returns:
#         _description_
#     """
#     rate_column_name = ' '.join([count_column, rate_suffix])
#     df[rate_column_name] = df[count_column]/df['Population']*100000
#     return df

# def add_rate_columns(df: pd.DataFrame) -> pd.DataFrame:
#     """add_rate_columns _summary_

#     Args:
#         df: _description_

#     Returns:
#         _description_
#     """
#     columns = copy.deepcopy(options.offenses)
#     columns.extend(['Total Violent Crime', 'Total Property Crime'])
#     for column in columns:
#         df = add_rate_column(df, column)
#     return df

# def add_normalized_column(
#     df: pd.DataFrame,
#     rate_column: str,
#     normalized_suffix: str = options.normalized_suffix) -> pd.DataFrame:
#     """add_normalized_column

#     Args:
#         df: _description_
#         count_column: _description_
#         rate_suffix: _description_. Defaults to 'Rate'.

#     Returns:
#         _description_

#     """
#     minimum = df[rate_column].min()
#     maximum = df[rate_column].max()
#     normalized_column_name = ' '.join([rate_column, normalized_suffix])
#     df[normalized_column_name] = (df[rate_column] - minimum)/(maximum - minimum)
#     return df

# def add_normalized_columns(df: pd.DataFrame) -> pd.DataFrame:
#     """add_rate_columns _summary_

#     Args:
#         df: _description_

#     Returns:
#         _description_
#     """
#     columns = copy.deepcopy(options.offenses)
#     columns.extend(['Total Violent Crime', 'Total Property Crime'])
#     rate_columns = [' '.join([x, options.rate_suffix]) for x in columns]
#     for column in rate_columns:
#         df = add_normalized_column(df, column)
#         column_name = ' '.join([column, options.normalized_suffix])
#         print('test norm max', column_name, ' ', df[column_name].max())
#     return df

# def add_missing_state_name(row: pd.Series) -> pd.Series:
#     """_summary_

#     Args:
#         row: _description_

#     """
#     if row['State'] is np.nan:
#         row['State'] = 'US'
#         row['State Name'] = 'United States'
#     elif row['State Name'] is np.nan:
#         row['State Name'] = options.state_abbreviations[row['State']]
#     return row

# def add_missing_state_names(df: pd.DataFrame) -> pd.DataFrame:
#     """_summary_

#     Args:
#         df (pd.DataFrame): _description_

#     Returns:
#         pd.DataFrame: _description_

#     """
#     return df.apply(add_missing_state_name, axis = 1)

# def separate_total_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
#     """separate_total_data _summary_

#     Args:
#         df: _description_

#     Returns:
#         _description_
#     """
#     total = df[df['State'] == 'US']
#     states = df.drop(df[df['State'] == 'US'].index)
#     return total, states

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

def get_rate_df(df: pd.DataFrame, columns: str | list[str]) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        columns: _description_

    Returns:
        pd.DataFrame: _description_
    """
    if isinstance(columns, str):
        offenses = getattr(options, columns)
        columns = ['Year']
        rate_offenses = [' '.join([c, options.rate_suffix]) for c in offenses]
        columns.extend(rate_offenses)
    return df[columns].set_index('Year')


def get_state_rate_df(
    df: pd.DataFrame,
    columns: str | list[str]) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        columns: _description_

    Returns:
        pd.DataFrame: _description_
    """
    if isinstance(columns, str):
        offenses = getattr(options, columns)
        columns = ['Year', 'State Name']
        rate_offenses = [' '.join([c, options.rate_suffix]) for c in offenses]
        columns.extend(rate_offenses)
    return df[columns].set_index(['Year', 'State Name'])

def get_state_normalized_df(
    df: pd.DataFrame,
    columns: str | list[str]) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        columns: _description_

    Returns:
        pd.DataFrame: _description_
    """
    if isinstance(columns, str):
        offenses = getattr(options, columns)
        columns = ['Year', 'State Name']
        normal_offenses = [
            ' '.join([c, options.normalized_suffix]) for c in offenses]
        columns.extend(normal_offenses)
    return df[columns].set_index(['Year', 'State Name'])

def drop_before_start_date(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    return df[df['Year'] >= options.start_year]
