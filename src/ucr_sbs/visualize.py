"""Visualizes data and analysis"""

from __future__ import annotations

import dataclasses

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from . import options


def plot_total_rate_time_series(df: pd.DataFrame) -> None:
    """plot_total_rate_time_series _summary_

    Args:
        df: _description_
    """
    columns = ['Year']
    violent = [
        ' '.join([c, options.rate_suffix]) for c in options.violent_offenses]
    columns.extend(violent)
    rate_df = df[columns].set_index("Year")
    sns.lineplot(data = rate_df)
    plt.show()
    return

def plot_total_rate_percent_change(df: pd.DataFrame) -> None:
    """plot_total_rate_time_series _summary_

    Args:
        df: _description_
    """
    columns = ['Year']
    violent = [
        ' '.join([c, options.rate_suffix]) for c in options.offenses]
    columns.extend(violent)
    print('test columns', columns)
    rate_df = df[columns].set_index("Year")
    percent_change_df = rate_df.pct_change()
    visual = sns.lineplot(
        data = percent_change_df,
        legend = 'brief')
    visual.set(xlabel='Year', ylabel='% Change in Crime Rate from Previous Year')
    plt.show()
    return

def plot_aggregate_violent_crime_rate(df: pd.DataFrame) -> None:
    """plot_aggregate_crime_rate _summary_

    Args:
        df: _description_

    """
    columns = ['Year', 'Total Violent Crime Rate']
    rate_df = df[columns].set_index("Year")
    visual = sns.lineplot(
        data = rate_df,
        legend = 'brief')
    visual.set(xlabel='Year', ylabel='Crime Rate per 100,000 People')
    plt.show()
    return

def plot_aggregate_property_crime_rate(df: pd.DataFrame) -> None:
    """plot_aggregate_crime_rate _summary_

    Args:
        df: _description_

    """
    columns = ['Year', 'Total Property Crime Rate']
    rate_df = df[columns].set_index("Year")
    visual = sns.lineplot(
        data = rate_df,
        legend = 'brief')
    visual.set(xlabel='Year', ylabel='Crime Rate per 100,000 People')
    plt.show()
    return
