from numpy import NaN
import pandas
from pandas.core.frame import DataFrame


def Shot_Seeker(file):

    '''To open a file, find the positions of all the shots within the file, and return a list with those values.'''

    df = pandas.read_json(file) 
    shot_list = []
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
    
    return shot_final


#Shot_Seeker('/Users/sam/VSCode/Rough/data1.json')