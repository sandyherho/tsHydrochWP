'''
Exploratory Data Analysis
Sandy Herho <herho@umd.edu>
2021/03/31
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
from sklearn import preprocessing
plt.style.use('ggplot')

ds = xr.open_dataset('../data/era51979_2020.nc')
pr = ds['tp']

prSpa = pr.mean('latitude').mean('longitude').to_dataframe()
prSpa.to_csv('../data/precipWestPapua.csv')

plt.figure(figsize = (15,6))
data = pr.groupby('time.month').mean('time', skipna = True).\
mean('latitude').mean('longitude').to_dataframe()
dataNP = np.array(data['tp'])
norm = np.linalg.norm(dataNP)
dataNPnorm = dataNP/norm
data = pd.DataFrame(dataNPnorm,
                    index = ['Jan', 'Feb', 'Mar', 'Apr', 'May',\
                             'Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
data.columns = ['Normalized precipitation']
data.index.rename('month', inplace=True)
data['month'] = data.index
sns.barplot(x = 'month', y = 'Normalized precipitation', data = data, color = 'steelblue');
plt.savefig('../figs/fig3.eps', format = 'eps')

x = prSpa.values
min_max_scaler = preprocessing.MinMaxScaler()
pr_scaled = min_max_scaler.fit_transform(x).flatten()
date = np.arange('1979-01', '2021-01', dtype='datetime64[M]')

plt.figure(figsize=(15,6));
plt.plot(date, pr_scaled);
plt.xlabel('time (month)');
plt.ylabel('Normalized precipitation');
plt.savefig('../figs/fig1.eps', format = 'eps')
