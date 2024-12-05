"""Main file for unit tests."""

from __future__ import annotations

import ucr_sbs

def test_ucr_sbs() -> None:
    violent_crime_path = ucr_sbs.options.data_path / ucr_sbs.options.violent_crime_states
    df = ucr_sbs.core.load_data(violent_crime_path)
    df = ucr_sbs.munge.remove_comma_separators(df)
    df = ucr_sbs.munge.change_types(df)
    df = ucr_sbs.munge.add_rate_columns(df)
    total, states = ucr_sbs.munge.separate_total_data(df)
    states = ucr_sbs.munge.add_missing_rape_data(states, total)
    total = ucr_sbs.munge.add_missing_rape_data(total, total)
    print(states.columns)
    print(states.head())
    print(total.head())
    ucr_sbs.visualize.plot_total_rate_time_series(total)
    return

if __name__ == '__main__':
    test_ucr_sbs()
