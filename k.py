# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:25:46 2020

@author: py
"""

import pandas as pd
from matplotlib.dates import \
    DateFormatter, WeekdayLocator, DayLocator, MONDAY, date2num
from datetime import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.pyplot as plt

#%% 处理格式
ssec2015 = pd.read_csv('ssec2015.csv')
ssec2015 = ssec2015.iloc[:, 1:]
print(ssec2015.head())
ssec2015.Date = [date2num(datetime.strptime(date, '%Y-%m-%d'))\
                         for date in ssec2015.Date]
print(ssec2015.head())
ssec2015_list = []
for i in range(len(ssec2015)):
    ssec2015_list.append(ssec2015.iloc[i,:])

#%% 绘图
ax = plt.subplot()
mondays = WeekdayLocator(MONDAY)
weekFormatter = DateFormatter('%y %b %d')
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(DayLocator())
ax.xaxis.set_major_formatter(weekFormatter)
plt.rcParams['font.sans-serif']=['SimHei']
ax.set_title('上证综指2015年3月份K线图')