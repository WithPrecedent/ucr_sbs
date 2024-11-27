"""Main file for unit tests."""

from __future__ import annotations

import ucr_sbs

def test_ucr_sbs() -> None:
    violent_crime_path = ucr_sbs.options.data_path / ucr_sbs.options.violent_crime_states
    df = ucr_sbs.core.load_data(violent_crime_path)
    print(df.head())
    return

if __name__ == '__main__':
    test_ucr_sbs()
