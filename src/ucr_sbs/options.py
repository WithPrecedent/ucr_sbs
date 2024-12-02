
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

offenses =[
    'Homicide',
    'Rape (original)',
    'Rape (revised)',
    'Robbery',
    'Aggravated Assault',
    'Burglary',
    'Larceny',
    'Auto Theft']

data_path = pathlib.Path('../../data/crime')
violent_crime_states = 'UCR/SBS/1979_to_2023_violent_estimates_by_state.csv'
