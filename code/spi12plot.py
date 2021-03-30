'''
SPI-12 Plot
Sandy Herho <herho@umd.edu>
2021/03/31
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

spi = pd.read_csv('../data/spi12.csv')[1:]
spi = spi['SPI12'].to_numpy().flatten()

fig = plt.figure(figsize=(15,8));
ax = fig.add_subplot(111);
xtime = np.linspace(1, spi.shape[0], spi.shape[0])
ax.plot(xtime, spi, 'black', alpha=1, linewidth=2);
ax.fill_between(xtime, 0., spi, spi > 0, color = '#54e1e3');
ax.fill_between(xtime, 0., spi, spi < 0, color = '#b81402');

plt.xlabel('time (month)');
plt.ylabel('Standardized Precipitation Index - 12');
ax.set_xlim(0, spi.shape[0]);
ax.set_xticklabels(['1980', '1988', '1996', '2005', '2013']);

plt.savefig('../data/fig4.eps', format = 'eps');
