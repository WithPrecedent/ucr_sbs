
import pathlib

import numpy as np
import pandas as pd


violent_crime_numericals = [
    'Year',
    'Population',
    'Total Violent Crime',
    'Homicide',
    'Rape (original)',
    'Rape (revised)',
    'Robbery',
    'Aggravated Assault',
    'Total Property Crime',
    'Burglary',
    'Larceny',
    'Auto Theft']

violent_crime_labels = {
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

offenses = [
    'Homicide',
    'Rape (original)',
    'Rape (revised)',
    'Robbery',
    'Aggravated Assault',
    'Burglary',
    'Larceny',
    'Auto Theft']

violent_offenses = [
    'Homicide',
    'Rape (original)',
    'Rape (revised)',
    'Robbery',
    'Aggravated Assault']

property_offenses = [
    'Burglary',
    'Larceny',
    'Auto Theft']

rate_suffix = 'Rate'
data_path = pathlib.Path('../../data/crime')
violent_crime_states = 'UCR/SBS/1979_to_2023_violent_estimates_by_state.csv'

states = {
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
