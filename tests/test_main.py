"""Main file for unit tests."""

from __future__ import annotations

import ucr_sbs

def test_ucr_sbs() -> None:
    violent_crime_path = ucr_sbs.options.data_path / ucr_sbs.options.violent_crime_states
    df = ucr_sbs.core.load_data(violent_crime_path)
    df = ucr_sbs.munge.remove_comma_separators(df)
    df = ucr_sbs.munge.change_types(df)
    df = ucr_sbs.munge.add_rate_columns(df)
    # df = ucr_sbs.munge.reshape_wide(df, ['Year', 'State'])
    print(df.head())
    return

if __name__ == '__main__':
    test_ucr_sbs()
