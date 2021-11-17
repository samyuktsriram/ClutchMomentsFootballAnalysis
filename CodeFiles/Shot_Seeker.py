from numpy import NaN
import pandas
from pandas.core.frame import DataFrame


def Shot_Seeker(file):

    '''To open a file, find the positions of all the shots within the file, and return a list with those values.'''

    df = pandas.read_json(file) 
    shot_list = []
    shot_final = []

    for i in range(len(df)):
        if df.loc[i, 'type']['name'] == 'Shot':
            shot_final.append(i)
    
    return shot_final


#Shot_Seeker('/Users/sam/VSCode/Rough/data1.json')