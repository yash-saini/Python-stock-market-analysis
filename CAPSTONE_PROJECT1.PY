
""" This project analyzes the stocks of three different car companies 
    Tesla,Ford and General Motors by plotting different graphs, calculating
    returns and cumulative returns and plotting them. 
"""

import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import pandas_datareader
import pandas_datareader.data as web
from pandas.plotting import scatter_matrix
from mpl_finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY

start=datetime.datetime(2012,1,1)
end=datetime.datetime(2017,1,1)
#Reading data 
tesla=web.DataReader('TSLA','yahoo',start,end)
ford=web.DataReader('F','yahoo',start,end)
gm=web.DataReader('GM','yahoo',start,end)

#De-comment below to see the graphs
#Plotting data (Opening of stocks)
'''
tesla['Open'].plot(label="Tesla",figsize=(16,8),title="Opening Prices")
ford['Open'].plot(label="Ford",figsize=(16,8),title="Opening Prices")
gm['Open'].plot(label="Gm",figsize=(16,8),title="Opening Prices")
plt.legend()
plt.show()
#Plotting Volume of data
tesla['Volume'].plot(label="Tesla",figsize=(16,8),title="Volume")
ford['Volume'].plot(label="Ford",figsize=(16,8),title="Volume")
gm['Volume'].plot(label="Gm",figsize=(16,8),title="Volume")
plt.legend()
plt.show()
'''
# Maximum volume of Ford's traded in 2014 
print ("Maximum Volume of stock traded for ford is on:-",ford['Volume'].idxmax())

#Total money traded =Opening * Volume of stocks
tesla['Total Traded']=tesla['Open'] * tesla['Volume']
ford['Total Traded']=ford['Open'] * ford['Volume']
gm['Total Traded']=gm['Open'] * gm['Volume']

# PLot of total trading that happened
'''
tesla['Total Traded'].plot(label="Tesla",figsize=(16,8),title="Total traded")
ford['Total Traded'].plot(label="Ford",figsize=(16,8),title="Total traded")
gm['Total Traded'].plot(label="Gm",figsize=(16,8),title="Total traded")
plt.legend()
plt.show()
'''
# Concatenating the Open prices of tesla,ford,gm
car_comp=pd.concat([tesla["Open"],gm["Open"],ford["Open"]],axis=1)
car_comp.columns=['Tesla Open','GM Open', 'Ford Open']

'''
scatter_matrix(car_comp,figsize=(8,8),alpha=0.2,hist_kwds={'bins':50})
'''


"""
#CandleStick Chart
ford_reset=ford.loc['2012-01'].reset_index()
ford_reset['date_ax']=ford_reset['Date'].apply(lambda date:date2num(date))
l=['date_ax','Open','High','Low','Close']
ford_values=[tuple(vals) for vals in ford_reset[l].values]

mondays=WeekdayLocator(MONDAY)
alldays=DayLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter= DateFormatter('%d')
fig,ax=plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
candlestick_ohlc(ax,ford_values,width=0.6,colorup='g',colordown='r')
"""


"""FINANCIAL ANALYSIS"""
# Use this tesla['returns']=(tesla['Close']/tesla['Close'].shift(1))-1 or the given formula
tesla['returns']=tesla['Close'].pct_change(1)
ford['returns']=ford['Close'].pct_change(1)
gm['returns']=gm['Close'].pct_change(1)

tesla['returns'].hist(bins=100,label='tesla',figsize=(10,10)) #Use alpha=0.4 for lighter image of the plot.
ford['returns'].hist(bins=100,label='ford')
gm['returns'].hist(bins=100,label='gm')
plt.legend()
plt.show()

#Density Plot
''' Here spike of ford signifies it to be stable , wide margin in Tesla signifying more volatility.'''
tesla['returns'].plot(kind='kde',label='Tesla',figsize=(10,8))
ford['returns'].plot(kind='kde',label='Ford',figsize=(10,8))
gm['returns'].plot(kind='kde',label='GM',figsize=(10,8))
plt.legend()
plt.show()

#Box plots
box_df=pd.concat([tesla['returns'],ford['returns'],gm['returns']],axis=1)
box_df.columns=['Tesla Ret','Ford Ret','GM Ret']
box_df.plot(kind='box',figsize=(10,10))
plt.legend()
plt.show()
'''
#Scatter-matrix of returns
scatter_matrix(box_df,figsize=(10,10),alpha=0.2,hist_kwds={'bins':50})

'''

""" 
It is seen that ford and gm returns are related to each other , looks like linear regression
plot them as box_df.plot(kind="scatter",x="Ford Ret",y="GM Ret")
"""

""" Cumulative Return"""
""" PLOT SHOWS THAT TESLA HAS HIGHEST RETURN. """

tesla['Cumulative Return'] = (1+tesla['returns']).cumprod()
ford['Cumulative Return'] = (1+ford['returns']).cumprod()
gm['Cumulative Return'] = (1+gm['returns']).cumprod()

# PLot of CUMULATIVE RETURNS 
tesla['Cumulative Return'].plot(label="Tesla",figsize=(10,10))
gm['Cumulative Return'].plot(label="gm",figsize=(10,10))
ford['Cumulative Return'].plot(label="ford",figsize=(10,10))
plt.legend()
plt.show()

























