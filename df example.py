import pandas
from pandas import Series, DataFrame
import numpy as np

#index=['a','b','c','d']
#s=Series(range(4), index=index)
#s2=Series(np.random.randn(3), name='B', index=index[1:])
#d={'A':s,'B':s2}
#df=DataFrame(d)
#
#dt=['2013/07/29','2013/07/30','2013/07/31','2013/08/01','2013/08/02']
#pr=[67.24,64.73,73.29,70.41,69.23]
#stk='Bad Stock'
#s1=Series(pr, index=dt)
#pr2=[90.23,88.23,91.23,91.46,95.22]
#stk2='Good Stock'
#s2=Series(pr2,index=dt)
#d={stk:s1,stk2:s2}
#sd=DataFrame(d)
#
#


#Homework plot bond data with the same way and then make the plots so that they are not backwards

sp=pandas.read_csv(r'C:\Users\Shaunak\Documents\Python Snakes\sp.csv')
ag=pandas.read_csv(r'C:\Users\Shaunak\Documents\Python Snakes\ag.csv')
#stk1='S&P500'
#stk2='Aggregiate'
#sp_index=['spDate', 'spOpen', 'spHigh', 'spLow', 'spClose', 'spVolume', 'spAdj Close']
#ag_index=['agDate', 'agOpen', 'agHigh', 'agLow', 'agClose', 'agVolume', 'agAdj Close']
#sp.columns=sp_index
#ag.columns=ag_index

#s1=Series('agClose'], index='agDate')
#d={stk:s1}
#sd=DataFrame(d)
#sd.sort()

#to get the stock prices change with 

