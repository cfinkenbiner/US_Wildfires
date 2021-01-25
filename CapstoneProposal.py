#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:13:02 2021

@author: catiefinkenbiner
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt


### Convert sqlite file to csv
# import sqlite3
# db_file = '/Users/catiefinkenbiner/Documents/JobApps/DataIncubator/FPA_FOD_20170508.sqlite'

# conn = sqlite3.connect(db_file, isolation_level=None,
#                        detect_types=sqlite3.PARSE_COLNAMES)
# df = pd.read_sql_query("select * from fires", conn)
# df.to_csv('WildFires.csv', index=False)


### Read csv
df = pd.read_csv('WildFires.csv', index_col=None)

years = np.arange(1992, 2016)
num_fires = []
for yr in years:
    df_yr = df[df['FIRE_YEAR'] == yr]
    num_fires.append(df_yr['OBJECTID'].nunique())
num_fires = np.array(num_fires)

slope, intercept, r_value, p_value, std_err = stats.linregress(years, num_fires)
print(r_value**2, p_value)

plt.figure()
plt.plot(years, num_fires, 'r^-')
plt.plot(years, years*slope+intercept, 'k-')

plt.text(1992, 85000, r'$r^2$= %.3f' % r_value**2)
plt.text(1992, 80000, r'p-value= %.3f' % p_value)
plt.ylabel('Number of Reported Fires')
plt.tight_layout()
plt.show() ; plt.close()


## Number of fires per state
states = df['STATE'].unique()
num_fires = []
for s in states:
    df_s = df[df['STATE'] == s]
    num_fires.append(df_s['OBJECTID'].nunique())
num_fires = np.array(num_fires)

plt.figure(figsize=(9,3))
plt.bar(states, num_fires, color='orange')

plt.xticks(rotation = 90)
plt.ylabel('Number of Reported Fires')
plt.tight_layout()
plt.savefig('Fig2_numfires_per_state.png',dpi=300)
plt.show() ; plt.close()


## Correlation between 'Latitude' and 'Fire Year'
slope, intercept, r_value, p_value, std_err = stats.linregress(df['LATITUDE'], df['FIRE_YEAR'])
print('r2=', r_value**2, 'p-value=', p_value)


## NLDAS Soils Dataset
import xarray as xr

soil_tex_netcdf4 = xr.open_dataset('NLDAS_masks-veg-soil.nc4')

# Start with OR
df_OR = df[df['STATE'] == 'OR']

soiltex = [] ; fire_yr = []
for l in np.arange(10000):
    dstex = soil_tex_netcdf4.sel(lon=df_OR['LONGITUDE'].iloc[l], lat=df_OR['LATITUDE'].iloc[l], method='nearest')
    soiltex.append(dstex['NLDAS_soil'].values)
    fire_yr.append(df_OR['FIRE_YEAR'].iloc[l])
soiltex = (np.array(soiltex)).ravel()

## Correlation between 'Latitude' and 'Soil Type'
slope, intercept, r_value, p_value, std_err = stats.linregress(soiltex, df_OR['FIRE_YEAR'].iloc[:10000])
print('r2=', r_value**2, 'p-value=', p_value)

df_OR_soil = pd.DataFrame({'lat':df_OR['LATITUDE'].iloc[:10000], 'lon':df_OR['LONGITUDE'].iloc[:10000], 
                           'fire_year':df_OR['FIRE_YEAR'].iloc[:10000], 'fire_class':df_OR['FIRE_SIZE_CLASS'].iloc[:10000],
                           'soil':soiltex})
df_OR_soil.head()

plt.figure()
plt.subplot(1,2,1)
plt.plot(df_OR_soil['soil'], df_OR_soil['fire_class'], 'co')
plt.xlabel('Soil Type')
plt.ylabel('Fire Class')

plt.subplot(1,2,2)
plt.plot(df_OR_soil['soil'], df_OR_soil['fire_year'], 'mo')
plt.xlabel('Soil Type')
plt.ylabel('Fire Year')

plt.tight_layout()
plt.savefig('Fig3_OR_soils.png',dpi=300)
plt.show() ; plt.close()