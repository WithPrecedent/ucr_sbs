"""Loads data from disk"""

from __future__ import annotations

import dataclasses
import pathlib

import pandas as pd

from . import options


def load_data(path: pathlib.Path) -> pd.DataFrame:
    """load_data

    Args:
        path: _description_

    Returns:
        _description_

    """
    df = pd.read_csv(path)
    df.columns = list(options.violent_crime_labels.values())
    df = df.drop('Caveats', axis = 1)
    return df
