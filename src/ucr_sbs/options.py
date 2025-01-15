"""General settings for UCR data files."""

from __future__ import annotations

import pathlib

from sklearn import preprocessing

scalers: dict[str, type] = {
    'normalized': preprocessing.Normalizer,
    'standard': preprocessing.StandardScaler,
    'robust': preprocessing.RobustScaler}

indexes: list[str] = ['Year', 'State Name', 'Agency Name']

offenses: dict[str, str] = {
    'Homicide': 'violent',
    'Rape (original)': 'violent',
    'Rape (revised)': 'violent',
    'Robbery': 'violent',
    'Aggravated Assault': 'violent',
    'Burglary': 'property',
    'Larceny': 'property',
    'Auto Theft': 'property'}

totals: dict[str] = {
    'Total Violent Crime': 'violent',
    'Total Property Crime': 'property'}

transitional: list[str] = ['Population', 'State']

normalized_suffix: str = 'Normalized'
rate_suffix: str = 'Rate'
data_path: pathlib.Path = pathlib.Path('../../data/crime/')

state_abbreviations: dict[str, str] = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'}

state_numbers: dict[int, str] = {
    1: 'Alabama',
    2: 'Arizona',
    3: 'Arkansas',
    4: 'California',
    5: 'Colorado',
    6: 'Connecticut',
    7: 'Delaware',
    8: 'District of Columbia',
    9: 'Florida',
    10: 'Georgia',
    11: 'Idaho',
    12: 'Illinois',
    13: 'Indiana',
    14: 'Iowa',
    15: 'Kansas',
    16: 'Kentucky',
    17: 'Louisiana',
    18: 'Maine',
    19: 'Maryland',
    20: 'Massachusetts',
    21: 'Michigan',
    22: 'Minnesota',
    23: 'Mississippi',
    24: 'Missouri',
    25: 'Montana',
    26: 'Nebraska',
    27: 'Nevada',
    28: 'New Hampshire',
    29: 'New Jersey',
    30: 'New Mexico',
    31: 'New York',
    32: 'North Carolina',
    33: 'North Dakota',
    34: 'Ohio',
    35: 'Oklahoma',
    36: 'Oregon',
    37: 'Pennsylvania',
    38: 'Rhode Island',
    39: 'South Carolina',
    40: 'South Dakota',
    41: 'Tennessee',
    42: 'Texas',
    43: 'Utah',
    44: 'Vermont',
    45: 'Virginia',
    46: 'Washington',
    47: 'West Virginia',
    48: 'Wisconsin',
    49: 'Wyoming',
    50: 'Alaska',
    51: 'Hawaii',
    52: 'Canal Zone',
    53: 'Puerto Rico',
    54: 'American Samoa',
    55: 'Guam',
    62: 'Virgin Islands'}

region_numbers: dict[int, str] = {
    0: 'Possessions',
    1: 'New England',
    2: 'Middle Atlantic',
    3: 'East North Central',
    4: 'West North Central',
    5: 'South Atlantic',
    6: 'East South Central',
    7: 'West South Central',
    8: 'Mountain',
    9: 'Pacific'}

month_prefixes: list[str] = [
    'Jan ',
    'Feb ',
    'Mar ',
    'Apr ',
    'May ',
    'Jun ',
    'Jul ',
    'Aug ',
    'Sep ',
    'Oct ',
    'Nov ',
    'Dec ']
