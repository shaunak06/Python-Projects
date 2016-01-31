import pandas
from pandas import Series, DataFrame
import matplotlib as plt

sp=pandas.read_csv(r'C:\Users\Shaunak\Documents\Python Snakes\sp.csv')
ag=pandas.read_csv(r'C:\Users\Shaunak\Documents\Python Snakes\ag.csv')

s=sp['Close']
b=ag['Close']

portfolios = [(75,20,5), (60,35,5), (50,50,0)]

for pf in portfolios:
    spos, bpos, cpos = pf
    pvalue =s*spos/s[len(sp)-1] + b*bpos/b[len(sp)-1] + cpos
    print "Stock = {}, Bond = {}, Cash = {}, Value = {}".format(spos, bpos, cpos, pvalue[0])
    pvalue.plot()

#both=s*75/s[len(sp)-1] + b*20/b[len(sp)-1] + 5
#print both

#stock_pos=75/sp[-1:]['Close']
#bond_pos=75/ag[-1:]['Close']
