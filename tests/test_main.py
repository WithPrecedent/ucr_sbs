"""Main file for unit tests."""

from __future__ import annotations

import ucr_sbs

def test_ucr_sbs() -> None:
    srs = ucr_sbs.sources.SRS()
    srs.load()
    srs.clean()
    srs.data['cleaned'] = srs.data['cleaned'][srs.data['cleaned']['Year'] >= 2004]
    srs.split()
    srs.munge()
    srs.visualize(dataset = 'Total')
    srs.visualize(dataset = 'Total', stat_type = 'normalized')
    # df = ucr_sbs.core.load_data(violent_crime_path)
    # df = ucr_sbs.munge.remove_comma_separators(df)
    # df = ucr_sbs.munge.change_types_to_numerics(df)
    # df = ucr_sbs.munge.drop_before_start_date(df)
    # df = ucr_sbs.munge.add_rate_columns(df)
    # df = ucr_sbs.munge.add_missing_state_names(df)
    # df = ucr_sbs.munge.trim_state_names(df)
    # total, states = ucr_sbs.munge.separate_total_data(df)
    # states = ucr_sbs.munge.add_missing_rape_data(states, total)
    # total = ucr_sbs.munge.add_missing_rape_data(total, total)
    # total = ucr_sbs.munge.add_normalized_columns(total)
    # states = ucr_sbs.munge.add_normalized_columns(states)
    # ucr_sbs.visualize.plot_total_rate_time_series_original(total)
    # ucr_sbs.visualize.plot_total_rate_percent_change_original(total)
    # ucr_sbs.visualize.plot_aggregate_violent_crime_rate(total)
    # ucr_sbs.visualize.plot_aggregate_property_crime_rate(total)
    # ucr_sbs.visualize.plot_boxplot_state_crime_rate(
    #     states,
    #     offenses = ['Homicide', 'Rape (original)'],
    #     year = 2023)
    # ucr_sbs.visualize.plot_normalized_violinplot_state_rates(
    #     states,
    #     offenses = ucr_sbs.options.original_offenses,
    #     year = 2012)
    # ucr_sbs.visualize.plot_normalized_swarmplot_state_rates(
    #     states,
    #     offenses = ucr_sbs.options.original_offenses,
    #     year = 2012)
    # states = states.drop(states[states['State'] == 'DC'].index)
    # ucr_sbs.visualize.plot_state_rate_time_series_original(
    #     states,
    #     offense = 'Rape (original)')
    # ucr_sbs.visualize.plot_state_rate_time_series_original(
    #     states,
    #     offense = 'Homicide')
    # ucr_sbs.visualize.plot_state_rate_percent_change_original(
    #     states,
    #     offense = 'Rape (original)')
    # ucr_sbs.visualize.plot_state_rate_percent_change_original(
    #     states,
    #     offense = 'Homicide')
    return

if __name__ == '__main__':
    test_ucr_sbs()
