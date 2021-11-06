from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
import Shot_Seeker
import Shot_Filter
import Score_Counter

def Team_Names(file):
    

    team_list = []
    df = pandas.read_json(file)
    for i in range(2):
        team_list.append(df.loc[i, 'team']['name'])

    return (team_list[0], team_list[1])

Team_Names('/Users/sam/VSCode/Rough/data1.json')