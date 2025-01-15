"""Visualizes data and analysis."""

from __future__ import annotations

import copy
import dataclasses
from typing import ClassVar

import numpy as np
import pandas as pd

from . import core, options, visualize


@dataclasses.dataclass
class ASR(core.Source):
    """_summary_"""
    data: dict[str, pd.DataFrame] = dataclasses.field(default_factory = dict)
    website: ClassVar[str] = 'https://www.icpsr.umich.edu/web/NACJD/series/studies/'
    files: ClassVar[dict[int, int]] = {
        2004: 4460,
        2005: 4715,
        2006: 22404,
        2007: 25108,
        2008: 27642,
        2009: 30761,
        2010: 33521,
        2011: 34580,
        2012: 35017,
        2013: 36115,
        2014: 36394,
        2015: 36794,
        2016: 37056,
        2017: 38740,
        2018: 38743,
        2019: 38779,
        2020: 38787,
        2021: 38795,
        2022: 39062}
    column_names: ClassVar[dict[str, str]] = {}
    column_types: ClassVar[dict[str, type]] = {}
    visuals: ClassVar[list[str]] = []


@dataclasses.dataclass
class LEOKA(core.Source):
    """_summary_"""
    data: dict[str, pd.DataFrame] = dataclasses.field(default_factory = dict)
    website: ClassVar[str] = 'https://www.icpsr.umich.edu/web/NACJD/series/studies/'
    files: ClassVar[dict[int, int]] = {
        2004: 4462,
        2005: 4719,
        2006: 22402,
        2007: 25104,
        2008: 27646,
        2009: 30765,
        2010: 33525,
        2011: 34584,
        2012: 35020,
        2013: 36119,
        2014: 36295,
        2015: 36791,
        2016: 37062,
        2017: 37844,
        2018: 37855,
        2019: 38784,
        2020: 38792,
        2021: 38800,
        2022: 39067}
    column_names: ClassVar[dict[str, str]] = {}
    column_types: ClassVar[dict[str, type]] = {}
    visuals: ClassVar[list[str]] = []


@dataclasses.dataclass
class OKCA(core.Source):
    """_summary_"""
    data: dict[str, pd.DataFrame] = dataclasses.field(default_factory = dict)
    website: ClassVar[str] = 'https://www.icpsr.umich.edu/web/NACJD/series/studies/'
    files: ClassVar[dict[int, int]] = {
        2004: 4459,
        2005: 4721,
        2006: 22400,
        2007: 25101,
        2008: 27648,
        2009: 30766,
        2010: 33526,
        2011: 34586,
        2012: 35021,
        2013: 36122,
        2014: 36391,
        2015: 36789,
        2016: 37061,
        2017: 37906,
        2018: 37911,
        2019: 38783,
        2020: 38791,
        2021: 38799,
        2022: 39066}
    column_names: ClassVar[dict[str, str]] = {
        'V2': 'State Number',
        'V3': 'ORI Number',
        'V5': 'Region Number',
        'V6': 'Year',
        'V9': 'Covered by Another Agency',
        'V12': 'Months Reported',
        'V14': 'Population',
        'V26': 'Agency',
        'V70': 'Jan Murder',
        'V71': 'Jan Manslaughter',
        'V72': 'Jan Rape',
        'V75': 'Jan Robbery',
        'V80': 'Jan Total Assault',
        'V85': 'Jan Simple Assault',
        'V86': 'Jan Burglary',
        'V90': 'Jan Larceny',
        'V91': 'Jan Vehicle Theft',
        'V96': 'Jan Murder Arrest Clearances',
        'V97': 'Jan Manslaughter Arrest Clearances',
        'V98': 'Jan Rape Arrest Clearances',
        'V101': 'Jan Robbery Arrest Clearances',
        'V106': 'Jan Total Assault Arrest Clearances',
        'V111': 'Jan Simple Assault Arrest Clearances',
        'V112': 'Jan Burglary Arrest Clearances',
        'V116': 'Jan Larceny Arrest Clearances',
        'V117': 'Jan Vehicle Theft Arrest Clearances',
        'V188': 'Feb Murder',
        'V189': 'Feb Manslaughter',
        'V190': 'Feb Rape',
        'V193': 'Feb Robbery',
        'V198': 'Feb Total Assault',
        'V203': 'Feb Simple Assault',
        'V204': 'Feb Burglary',
        'V208': 'Feb Larceny',
        'V209': 'Feb Vehicle Theft',
        'V214': 'Feb Murder Arrest Clearances',
        'V215': 'Feb Manslaughter Arrest Clearances',
        'V216': 'Feb Rape Arrest Clearances',
        'V219': 'Feb Robbery Arrest Clearances',
        'V224': 'Feb Total Assault Arrest Clearances',
        'V229': 'Feb Simple Assault Arrest Clearances',
        'V230': 'Feb Burglary Arrest Clearances',
        'V234': 'Feb Larceny Arrest Clearances',
        'V235': 'Feb Vehicle Theft Arrest Clearances',
        'V306': 'Mar Murder',
        'V307': 'Mar Manslaughter',
        'V308': 'Mar Rape',
        'V311': 'Mar Robbery',
        'V316': 'Mar Total Assault',
        'V321': 'Mar Simple Assault',
        'V322': 'Mar Burglary',
        'V326': 'Mar Larceny',
        'V327': 'Mar Vehicle Theft',
        'V332': 'Mar Murder Arrest Clearances',
        'V333': 'Mar Manslaughter Arrest Clearances',
        'V334': 'Mar Rape Arrest Clearances',
        'V337': 'Mar Robbery Arrest Clearances',
        'V342': 'Mar Total Assault Arrest Clearances',
        'V347': 'Mar Simple Assault Arrest Clearances',
        'V348': 'Mar Burglary Arrest Clearances',
        'V352': 'Mar Larceny Arrest Clearances',
        'V353': 'Mar Vehicle Theft Arrest Clearances',
        'V424': 'Apr Murder',
        'V425': 'Apr Manslaughter',
        'V426': 'Apr Rape',
        'V429': 'Apr Robbery',
        'V434': 'Apr Total Assault',
        'V439': 'Apr Simple Assault',
        'V440': 'Apr Burglary',
        'V444': 'Apr Larceny',
        'V445': 'Apr Vehicle Theft',
        'V450': 'Apr Murder Arrest Clearances',
        'V451': 'Apr Manslaughter Arrest Clearances',
        'V452': 'Apr Rape Arrest Clearances',
        'V455': 'Apr Robbery Arrest Clearances',
        'V460': 'Apr Total Assault Arrest Clearances',
        'V465': 'Apr Simple Assault Arrest Clearances',
        'V466': 'Apr Burglary Arrest Clearances',
        'V470': 'Apr Larceny Arrest Clearances',
        'V471': 'Apr Vehicle Theft Arrest Clearances',
        'V542': 'May Murder',
        'V543': 'May Manslaughter',
        'V544': 'May Rape',
        'V547': 'May Robbery',
        'V552': 'May Total Assault',
        'V557': 'May Simple Assault',
        'V558': 'May Burglary',
        'V562': 'May Larceny',
        'V563': 'May Vehicle Theft',
        'V568': 'May Murder Arrest Clearances',
        'V569': 'May Manslaughter Arrest Clearances',
        'V570': 'May Rape Arrest Clearances',
        'V573': 'May Robbery Arrest Clearances',
        'V578': 'May Total Assault Arrest Clearances',
        'V583': 'May Simple Assault Arrest Clearances',
        'V584': 'May Burglary Arrest Clearances',
        'V588': 'May Larceny Arrest Clearances',
        'V589': 'May Vehicle Theft Arrest Clearances',
        'V660': 'Jun Murder',
        'V661': 'Jun Manslaughter',
        'V662': 'Jun Rape',
        'V665': 'Jun Robbery',
        'V670': 'Jun Total Assault',
        'V675': 'Jun Simple Assault',
        'V676': 'Jun Burglary',
        'V680': 'Jun Larceny',
        'V681': 'Jun Vehicle Theft',
        'V686': 'Jun Murder Arrest Clearances',
        'V687': 'Jun Manslaughter Arrest Clearances',
        'V688': 'Jun Rape Arrest Clearances',
        'V691': 'Jun Robbery Arrest Clearances',
        'V696': 'Jun Total Assault Arrest Clearances',
        'V701': 'Jun Simple Assault Arrest Clearances',
        'V702': 'Jun Burglary Arrest Clearances',
        'V706': 'Jun Larceny Arrest Clearances',
        'V707': 'Jun Vehicle Theft Arrest Clearances',
        'V778': 'Jul Murder',
        'V779': 'Jul Manslaughter',
        'V780': 'Jul Rape',
        'V783': 'Jul Robbery',
        'V788': 'Jul Total Assault',
        'V793': 'Jul Simple Assault',
        'V794': 'Jul Burglary',
        'V798': 'Jul Larceny',
        'V799': 'Jul Vehicle Theft',
        'V804': 'Jul Murder Arrest Clearances',
        'V805': 'Jul Manslaughter Arrest Clearances',
        'V806': 'Jul Rape Arrest Clearances',
        'V809': 'Jul Robbery Arrest Clearances',
        'V814': 'Jul Total Assault Arrest Clearances',
        'V819': 'Jul Simple Assault Arrest Clearances',
        'V820': 'Jul Burglary Arrest Clearances',
        'V824': 'Jul Larceny Arrest Clearances',
        'V825': 'Jul Vehicle Theft Arrest Clearances',
        'V896': 'Aug Murder',
        'V897': 'Aug Manslaughter',
        'V898': 'Aug Rape',
        'V901': 'Aug Robbery',
        'V906': 'Aug Total Assault',
        'V911': 'Aug Simple Assault',
        'V912': 'Aug Burglary',
        'V916': 'Aug Larceny',
        'V917': 'Aug Vehicle Theft',
        'V922': 'Aug Murder Arrest Clearances',
        'V923': 'Aug Manslaughter Arrest Clearances',
        'V924': 'Aug Rape Arrest Clearances',
        'V927': 'Aug Robbery Arrest Clearances',
        'V932': 'Aug Total Assault Arrest Clearances',
        'V937': 'Aug Simple Assault Arrest Clearances',
        'V938': 'Aug Burglary Arrest Clearances',
        'V942': 'Aug Larceny Arrest Clearances',
        'V943': 'Aug Vehicle Theft Arrest Clearances',
        'V1014': 'Sep Murder',
        'V1015': 'Sep Manslaughter',
        'V1016': 'Sep Rape',
        'V1019': 'Sep Robbery',
        'V1024': 'Sep Total Assault',
        'V1029': 'Sep Simple Assault',
        'V1030': 'Sep Burglary',
        'V1034': 'Sep Larceny',
        'V1035': 'Sep Vehicle Theft',
        'V1040': 'Sep Murder Arrest Clearances',
        'V1041': 'Sep Manslaughter Arrest Clearances',
        'V1042': 'Sep Rape Arrest Clearances',
        'V1045': 'Sep Robbery Arrest Clearances',
        'V1050': 'Sep Total Assault Arrest Clearances',
        'V1055': 'Sep Simple Assault Arrest Clearances',
        'V1056': 'Sep Burglary Arrest Clearances',
        'V1060': 'Sep Larceny Arrest Clearances',
        'V1061': 'Sep Vehicle Theft Arrest Clearances',
        'V1132': 'Oct Murder',
        'V1133': 'Oct Manslaughter',
        'V1134': 'Oct Rape',
        'V1137': 'Oct Robbery',
        'V1142': 'Oct Total Assault',
        'V1147': 'Oct Simple Assault',
        'V1148': 'Oct Burglary',
        'V1152': 'Oct Larceny',
        'V1153': 'Oct Vehicle Theft',
        'V1158': 'Oct Murder Arrest Clearances',
        'V1159': 'Oct Manslaughter Arrest Clearances',
        'V1160': 'Oct Rape Arrest Clearances',
        'V1163': 'Oct Robbery Arrest Clearances',
        'V1168': 'Oct Total Assault Arrest Clearances',
        'V1173': 'Oct Simple Assault Arrest Clearances',
        'V1174': 'Oct Burglary Arrest Clearances',
        'V1178': 'Oct Larceny Arrest Clearances',
        'V1179': 'Oct Vehicle Theft Arrest Clearances',
        'V1250': 'Nov Murder',
        'V1251': 'Nov Manslaughter',
        'V1252': 'Nov Rape',
        'V1255': 'Nov Robbery',
        'V1260': 'Nov Total Assault',
        'V1265': 'Nov Simple Assault',
        'V1266': 'Nov Burglary',
        'V1270': 'Nov Larceny',
        'V1271': 'Nov Vehicle Theft',
        'V1276': 'Nov Murder Arrest Clearances',
        'V1277': 'Nov Manslaughter Arrest Clearances',
        'V1278': 'Nov Rape Arrest Clearances',
        'V1281': 'Nov Robbery Arrest Clearances',
        'V1286': 'Nov Total Assault Arrest Clearances',
        'V1291': 'Nov Simple Assault Arrest Clearances',
        'V1292': 'Nov Burglary Arrest Clearances',
        'V1296': 'Nov Larceny Arrest Clearances',
        'V1297': 'Nov Vehicle Theft Arrest Clearances',
        'V1368': 'Dec Murder',
        'V1369': 'Dec Manslaughter',
        'V1370': 'Dec Rape',
        'V1373': 'Dec Robbery',
        'V1378': 'Dec Total Assault',
        'V1383': 'Dec Simple Assault',
        'V1384': 'Dec Burglary',
        'V1388': 'Dec Larceny',
        'V1389': 'Dec Vehicle Theft',
        'V1394': 'Dec Murder Arrest Clearances',
        'V1395': 'Dec Manslaughter Arrest Clearances',
        'V1396': 'Dec Rape Arrest Clearances',
        'V1399': 'Dec Robbery Arrest Clearances',
        'V1404': 'Dec Total Assault Arrest Clearances',
        'V1409': 'Dec Simple Assault Arrest Clearances',
        'V1410': 'Dec Burglary Arrest Clearances',
        'V1414': 'Dec Larceny Arrest Clearances',
        'V1415': 'Dec Vehicle Theft Arrest Clearances'}
    column_types: ClassVar[dict[str, type]] = {
        'State Number': int,
        'ORI Number': int,
        'Region Number': int,
        'Year': int,
        'Covered by Another Agency': str,
        'Months Reported': int,
        'Population': int,
        'Agency': str,
        'Murder': int,
        'Manslaughter': int,
        'Rape': int,
        'Robbery': int,
        'Total Assault': int,
        'Simple Assault': int,
        'Burglary': int,
        'Larceny': int,
        'Vehicle Theft': int,
        'Murder Arrest Clearances': int,
        'Manslaughter Arrest Clearances': int,
        'Rape Arrest Clearances': int,
        'Robbery Arrest Clearances': int,
        'Total Assault Arrest Clearances': int,
        'Simple Assault Arrest Clearances': int,
        'Burglary Arrest Clearances': int,
        'Larceny Arrest Clearances': int,
        'Vehicle Theft Arrest Clearances': int}


@dataclasses.dataclass
class SRS(core.Source):
    """_summary_"""
    data: dict[str, pd.DataFrame] = dataclasses.field(default_factory = dict)
    splits: list[str] = dataclasses.field(default_factory = lambda: [
        'raw', 'cleaned', 'total', 'states', 'normalized_states'])
    website: ClassVar[str | None] = None
    files: ClassVar[str | dict[int, int]] = 'UCR/SRS/1979_to_2023_violent_estimates_by_state.csv'
    column_names: ClassVar[dict[str, str]] = {
        'year': 'Year',
        'state_abbr': 'State',
        'state_name': 'State Name',
        'population': 'Population',
        'violent_crime': 'Total Violent Crime',
        'homicide': 'Homicide',
        'rape_legacy': 'Rape (original)',
        'rape_revised': 'Rape (revised)',
        'robbery': 'Robbery',
        'aggravated_assault': 'Aggravated Assault',
        'property_crime': 'Total Property Crime',
        'burglary': 'Burglary',
        'larceny': 'Larceny',
        'motor_vehicle_theft': 'Auto Theft',
        'caveats': 'Caveats'}
    column_types: ClassVar[dict[str, type]] = {
        'Year': int,
        'State': str,
        'State Name': str,
        'Population': int,
        'Total Violent Crime': int,
        'Homicide': int,
        'Rape (original)': int,
        'Rape (revised)': int,
        'Robbery': int,
        'Aggravated Assault': int,
        'Total Property Crime': int,
        'Burglary': int,
        'Larceny': int,
        'Auto Theft': int}
    visuals: ClassVar[list[str]] = []

    def clean(self):
        """_summary_"""
        self.data['cleaned'] = copy.deepcopy(self.data['raw'])
        self.data['cleaned'].columns = list(self.column_names.values())
        self.data['cleaned'] = self.data['cleaned'].drop('Caveats', axis = 1)
        for column, column_type in self.column_types.items():
            if column_type is int:
                self.data['cleaned'][column] = self.data['cleaned'][column].replace(',', '', regex = True)
                self.data['cleaned'][column] = pd.to_numeric(self.data['cleaned'][column], errors = 'coerce', downcast = 'integer')
        self.data['cleaned'] = self.data['cleaned'].apply(_add_missing_state_name, axis = 1)
        self.data['cleaned']['State Name'] = self.data['cleaned']['State Name'].apply(lambda x: x.strip())
        return

    def load(self, files: str | None = None) -> None:
        """_summary_

        Args:
            files (str | None, optional): _description_. Defaults to None.

        Returns:
            pd.DataFrame: _description_

        """
        pd.options.mode.chained_assignment = None
        files = files or self.files
        path = options.data_path / files
        self.data['raw'] = pd.read_csv(path)
        return

    def munge(self) -> None:
        """_summary_"""
        offense_columns = list(options.offenses.keys())
        offense_columns.extend(list(options.totals.keys()))
        rate_columns = [
            ' '.join([x, options.rate_suffix]) for x in offense_columns]
        for dataset in ['Total', 'States']:
            for column in offense_columns:
                self.data[dataset] = _add_rate_column(
                    self.data[dataset],
                    column)
            for column in rate_columns:
                self.data[dataset] = _add_normalized_column(
                    self.data[dataset],
                    column)
            ratio = _get_rape_original_to_revised_ratio(self.data['Total'])
            self.data[dataset] = self.data[dataset].apply(
                _impute_rape_data,
                axis = 1,
                ratio = ratio)
        return

    def split(self) -> None:
        """_summary_"""
        self.data['Total'] = self.data['cleaned'][self.data['cleaned']['State'] == 'US']
        self.data['Total'].set_index(['Year'])
        self.data['States'] = self.data['cleaned'].drop(self.data['cleaned'][self.data['cleaned']['State'] == 'US'].index)
        self.data['States'].set_index(['Year', 'State Name'])
        return

    def visualize(
        self,
        dataset: str,
        crimes: str | list[str] = 'all',
        rape_stats: str = 'original',
        stat_type: str = 'rates') -> None:
        """_summary_

        Args:
            dataset (str): _description_
            crimes (str | list[str], optional): _description_. Defaults to 'all'.
            rape_stats (str, optional): _description_. Defaults to 'original'.
            stat_type (str, optional): _description_. Defaults to 'rates'.
        """
        visualize.plot_time_series(
            data = self.data[dataset],
            crimes = crimes,
            rape_stats = rape_stats,
            stat_type = stat_type)
        return


def _add_missing_state_name(row: pd.Series) -> pd.Series:
    """_summary_

    Args:
        row: _description_

    """
    if row['State'] is np.nan:
        row['State'] = 'US'
        row['State Name'] = 'United States'
    elif row['State Name'] is np.nan:
        row['State Name'] = options.state_abbreviations[row['State']]
    return row

def _add_rate_column(
    data: pd.DataFrame,
    count_column: str,
    rate_suffix: str = options.rate_suffix) -> pd.DataFrame:
    """add_rate_column

    Args:
        data: _description_
        count_column: _description_
        rate_suffix: _description_. Defaults to 'Rate'.

    Returns:
        _description_
    """
    rate_column_name = ' '.join([count_column, rate_suffix])
    data[rate_column_name] = data[count_column]/data['Population']*100000
    return data

def _add_normalized_column(
    df: pd.DataFrame,
    rate_column: str,
    normalized_suffix: str = options.normalized_suffix) -> pd.DataFrame:
    """add_normalized_column

    Args:
        df: _description_
        rate_column: _description_
        normalized_suffix: _description_. Defaults to 'Rate'.

    Returns:
        _description_

    """
    minimum = df[rate_column].min()
    maximum = df[rate_column].max()
    normalized_column_name = ' '.join([rate_column, normalized_suffix])
    df[normalized_column_name] = (df[rate_column] - minimum)/(maximum - minimum)
    return df

def _get_rape_original_to_revised_ratio(df: pd. DataFrame) -> float:
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

def _impute_rape_data(row: pd.Series, ratio: float) -> pd.Series:
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