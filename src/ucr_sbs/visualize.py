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
    for offense in options.violent_offenses:
        rate_column = ' '.join([offense, options.rate_suffix])
        sns.lineplot(x = "Year", y = rate_column, data = df)
    plt.show()
    return
