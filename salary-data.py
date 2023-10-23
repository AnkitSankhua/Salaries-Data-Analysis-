# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:22:26 2023

@author: ankit
"""

import pandas as pd

df = pd.read_csv('salary_data.csv')

df['continent_name'] = df['continent_name'].replace('Caribbean','North America')
df['continent_name'] = df['continent_name'].replace('Northern America','North America')
df['continent_name'] = df['continent_name'].replace('Central America','North America')

df['continent_name'] = df['continent_name'].replace('Oceania','Australia/Oceania')


df.to_csv('modified_data.csv', index=False)

