from numpy import NaN
import pandas
from pandas.core.frame import DataFrame

df = pandas.read_json("/Users/sam/VSCode/Rough/data1.json") 
#df.to_csv('data1.csv')
#df.info()
#print(type(df.iloc[650, 26]))
shot_list = []
#for i in range(4209):
    #print(df.iloc[i, 26])

#figure out a way to get this list!!
#shot_position_csv=[647, 819, 1761, 1982, 1986, 2525, 2754, 2828, 2868, 2889, 2955, 2993, 2998, 3105, 3111, 3343, 3703, 3973, 4157, 4195]
shot_final = []

for i in range(4209):
    shot_list.append(df.iloc[i, 26])

def shotsAnalysis(shotdict, k):
    try:
        y = (shotdict[k]['outcome'])
        shot_final.append(k)
    finally:
        return
    return

for k in range(len(shot_list)):
    shotsAnalysis(shot_list, k)
len(shot_final)