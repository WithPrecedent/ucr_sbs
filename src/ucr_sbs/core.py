"""Loads data from disk"""

from __future__ import annotations

import abc
import dataclasses
import pathlib
from typing import ClassVar

import pandas as pd

from . import options


@dataclasses.dataclass
class Source(abc.ABC):
    """_summary_"""
    data: dict[str, pd.DataFrame] = dataclasses.field(default_factory = dict)
    website: ClassVar[str] = ''
    files: ClassVar[dict[int, int]] = {}
    column_names: ClassVar[dict[str, str]] = {}
    column_types: ClassVar[dict[str, type]] = {}
    visuals: ClassVar[list[str]] = []

    """ Properties """

    @property
    def maximum(self) -> int:
        """_summary_

        Returns:
            _type_: _description_
        """
        return max(self.files.keys())

    @property
    def minimum(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return min(self.files.keys())

    """ Abstract Methods """

    @abc.abstractmethod
    def clean(self, data: pd.DataFrame) -> pd.DataFrame:
        """_summary_

        Args:
            data (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """

    @abc.abstractmethod
    def load(self) -> pd.DataFrame:
        """_summary_

        Returns:
            pd.DataFrame: _description_
        """


    @abc.abstractmethod
    def munge(self, data: pd.DataFrame) -> pd.DataFrame:
        """_summary_

        Args:
            data (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """

    @abc.abstractmethod
    def visualize(self, data: pd.DataFrame) -> pd.DataFrame:
        """_summary_

        Args:
            data (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """


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
