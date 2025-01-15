"""Visualizes data and analysis."""

from __future__ import annotations

from typing import TYPE_CHECKING

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from . import munge, options

if TYPE_CHECKING:
    import pandas as pd


def plot_time_series(
    data: pd.DataFrame,
    crimes: str | list[str] = 'all',
    rape_stats: str = 'original',
    stat_type: str = 'rates') -> None:
    """_summary_

    Args:
        data (pd.DataFrame): _description_
        crimes (str | list[str], optional): _description_. Defaults to 'all'.
        rape_stats (str, optional): _description_. Defaults to 'original'.
        stat_type (str, optional): _description_. Defaults to 'rates'.
    """
    data_subset = _get_data_subset(data, crimes, rape_stats, stat_type)
    ylabel = _get_ylabel(stat_type)
    visual = sns.lineplot(data = data_subset)
    visual.set(xlabel = 'Year', ylabel = ylabel)
    plt.xticks(
        np.arange(min(data['Year']), max(data['Year'] + 1), 1),
        rotation = 45)
    visual.set_ylim(0)
    sns.despine()
    sns.move_legend(visual, 'center left', bbox_to_anchor = (1, .5))
    plt.show()
    return

def plot_total_rate_time_series_original(df: pd.DataFrame) -> None:
    """plot_total_rate_time_series _summary_

    Args:
        df: _description_
    """
    rate_df = munge.get_rate_df(df, columns = 'original_offenses')
    visual = sns.lineplot(data = rate_df)
    visual.set(xlabel = 'Year', ylabel = 'Crime Rate per 100,000 People')
    plt.xticks(
        np.arange(min(df['Year']), max(df['Year'] + 1), 1),
        rotation = 45)
    visual.set_ylim(0)
    sns.despine()
    sns.move_legend(visual, 'center left', bbox_to_anchor = (1, .5))
    plt.show()
    return

def plot_total_rate_time_series_revised(df: pd.DataFrame) -> None:
    """plot_total_rate_time_series _summary_

    Args:
        df: _description_
    """
    rate_df = munge.get_rate_df(df, columns = 'revised_offenses')
    visual = sns.lineplot(data = rate_df)
    visual.set(xlabel = 'Year', ylabel = 'Crime Rate per 100,000 People')
    plt.xticks(
        np.arange(min(df['Year']), max(df['Year'] + 1), 1),
        rotation = 45)
    visual.set_ylim(0)
    sns.despine()
    sns.move_legend(visual, 'center left', bbox_to_anchor = (1, .5))
    plt.show()
    return

def plot_total_rate_percent_change_original(df: pd.DataFrame) -> None:
    """plot_total_rate_time_series _summary_

    Args:
        df: _description_
    """
    rate_df = munge.get_rate_df(df, columns = 'original_offenses')
    percent_change_df = rate_df.pct_change()
    visual = sns.lineplot(data = percent_change_df, legend = 'brief')
    visual.set(
        xlabel = 'Year',
        ylabel = '% Change in Crime Rate from Previous Year')
    plt.xticks(
        np.arange(min(df['Year']), max(df['Year'] + 1), 1),
        rotation = 45)
    sns.despine()
    sns.move_legend(visual, 'center left', bbox_to_anchor = (1, .5))
    plt.show()
    return

def plot_total_rate_percent_change_revised(df: pd.DataFrame) -> None:
    """plot_total_rate_time_series _summary_

    Args:
        df: _description_
    """
    rate_df = munge.get_rate_df(df, columns = 'revised_offenses')
    percent_change_df = rate_df.pct_change()
    visual = sns.lineplot(data = percent_change_df, legend = 'brief')
    visual.set(
        xlabel = 'Year',
        ylabel = '% Change in Crime Rate from Previous Year')
    plt.xticks(
        np.arange(min(df['Year']), max(df['Year'] + 1), 1),
        rotation = 45)
    sns.despine()
    sns.move_legend(visual, 'center left', bbox_to_anchor = (1, .5))
    plt.show()
    return

def plot_aggregate_violent_crime_rate(df: pd.DataFrame) -> None:
    """plot_aggregate_crime_rate _summary_

    Args:
        df: _description_

    """
    rate_df = munge.get_rate_df(
        df,
        columns = ['Year', 'Total Violent Crime Rate'])
    visual = sns.lineplot(data = rate_df, legend = 'brief')
    visual.set(xlabel = 'Year', ylabel = 'Crime Rate per 100,000 People')
    plt.xticks(
        np.arange(min(df['Year']), max(df['Year'] + 1), 1),
        rotation = 45)
    visual.set_ylim(0)
    sns.despine()
    sns.move_legend(visual, 'center left', bbox_to_anchor = (1, .5))
    plt.show()
    return

def plot_aggregate_property_crime_rate(df: pd.DataFrame) -> None:
    """plot_aggregate_crime_rate _summary_

    Args:
        df: _description_

    """
    rate_df = munge.get_rate_df(
        df,
        columns = ['Year', 'Total Property Crime Rate'])
    visual = sns.lineplot(data = rate_df, legend = 'brief')
    visual.set(xlabel = 'Year', ylabel = 'Crime Rate per 100,000 People')
    plt.xticks(
        np.arange(min(df['Year']), max(df['Year'] + 1), 1),
        rotation = 45)
    visual.set_ylim(0)
    sns.despine()
    sns.move_legend(visual, 'center left', bbox_to_anchor = (1, .5))
    plt.show()
    return

def plot_state_rate_time_series_original(df: pd.DataFrame, offense: str) -> None:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        offense: s

    """
    rate_column = ' '.join([offense, options.rate_suffix])
    columns = ['Year', 'State Name', rate_column]
    rate_df = munge.get_state_rate_df(df, columns = columns)
    visual = sns.relplot(
        data = rate_df,
        x = 'Year',
        y = rate_column,
        col = 'State Name',
        kind = 'line',
        height = 1,
        col_wrap = 5,
        aspect = 2)
    visual.set_titles(col_template = '{col_name}')
    visual.set_axis_labels(
        x_var = 'Year',
        y_var = 'Crime Rate',
        clear_inner = True)
    plt.show()
    return

def plot_state_rate_percent_change_original(
    df: pd.DataFrame,
    offense: str) -> None:
    """plot_total_rate_time_series _summary_

    Args:
        df: _description_
        offense: s

    """
    rate_column = ' '.join([offense, options.rate_suffix])
    columns = ['Year', 'State Name', rate_column]
    rate_df = munge.get_state_rate_df(df, columns = columns)
    percent_change_df = rate_df.pct_change()
    visual = sns.relplot(
        data = percent_change_df,
        x = 'Year',
        y = rate_column,
        col = 'State Name',
        kind = 'line',
        height = 1,
        col_wrap = 5,
        aspect = 2)
    visual.set_titles(col_template = '{col_name}')
    visual.set_axis_labels(
        x_var = 'Year',
        y_var = '% Change',
        clear_inner = True)
    plt.show()
    return

def plot_boxplot_state_crime_rate(
    df: pd.DataFrame,
    offenses: list[str],
    year: int) -> None:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        offenses (list[str]): _description_
        year (int): _description_
    """
    df = df[df['Year'] == year]
    columns = [' '.join([x, options.rate_suffix]) for x in offenses]
    df = df[columns]
    visual = sns.violinplot(data = df)
    visual.set(xlabel = 'Crime', ylabel = 'Crime Rate per 100,000 People')
    sns.despine()
    plt.show()
    return

def plot_normalized_violinplot_state_rates(
    df: pd.DataFrame,
    offenses: list[str],
    year: int) -> None:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        offenses (list[str]): _description_
        year (int): _description_
    """
    df = df[df['Year'] == year]
    df = munge.add_normalized_columns(df)
    columns = [
        ' '.join([x, options.rate_suffix, options.normalized_suffix])
        for x in offenses]
    df = df[columns]
    visual = sns.violinplot(data = df, cut = 0, native_scale = True, orient = 'h')
    visual.set(xlabel = 'Normalized Crime Rate')
    visual.set_yticklabels(offenses)
    visual.xaxis.set_major_formatter(mpl.ticker.PercentFormatter(1))
    sns.despine()
    plt.show()
    return

def plot_normalized_swarmplot_state_rates(
    df: pd.DataFrame,
    offenses: list[str],
    year: int) -> None:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        offenses (list[str]): _description_
        year (int): _description_
    """
    df = df[df['Year'] == year]
    df = munge.add_normalized_columns(df)
    columns = [
        ' '.join([x, options.rate_suffix, options.normalized_suffix])
        for x in offenses]
    df = df[columns]
    visual = sns.swarmplot(data = df, native_scale = True, orient = 'h')
    visual.set(xlabel = 'Normalized Crime Rate')
    visual.set_yticklabels(offenses)
    visual.xaxis.set_major_formatter(mpl.ticker.PercentFormatter(1))
    sns.despine()
    plt.show()
    return

def _get_data_subset(
    data: pd.DataFrame,
    crimes: str | list[str] = 'all',
    rape_stats: str = 'original',
    stat_type: str = 'rates') -> list[str]:
    """_summary_

    Args:
        data (pd.DataFrame): _description_
        crimes (str | list[str]): _description_
        rape_stats (str, optional): _description_. Defaults to 'original'.
        stat_type (str, optional): _description_. Defaults to 'rates'.

    Returns:
        list[str]: _description_
    """
    columns = ['Year']
    if isinstance(crimes, str):
        if crimes == 'violent':
            offenses = [
                k for k, v in options.offenses.items() if v == 'violent']
        elif crimes == 'property':
            offenses = [
                k for k, v in options.offenses.items() if v == 'property']
        elif crimes == 'all':
            offenses = list(options.offenses.keys())
        if rape_stats == 'original' and crimes != 'property':
            offenses.remove('Rape (revised)')
        elif rape_stats == 'revised' and crimes != 'property':
            offenses.remove('Rape (original)')
    print('test columns', data.columns)
    if stat_type == 'counts':
        columns.extend(offenses)
    elif stat_type == 'rates':
        rate_offenses = [' '.join([c, options.rate_suffix]) for c in offenses]
        columns.extend(rate_offenses)
    elif stat_type == 'normalized':
        normalized_offenses = [' '.join([c, options.rate_suffix, options.normalized_suffix]) for c in offenses]
        columns.extend(normalized_offenses)
    return data[columns].set_index(['Year'])

def _get_ylabel(stat_type: str) -> str:
    """_summary_

    Args:
        stat_type (str): _description_

    Returns:
        str: _description_
    """
    if stat_type == 'rates':
        return 'Reported Crime Rate per 100,000 People'
    elif stat_type == 'normalized':
        return 'Normalized Reported Crime Rate'
    elif stat_type == 'counts':
        return 'Number of Reported Crimes'
    raise ValueError(f'{stat_type} is not a valid crime stat type')

