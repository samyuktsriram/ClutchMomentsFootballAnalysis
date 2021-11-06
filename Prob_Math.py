from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
import Shot_Seeker
import Shot_Filter
import Score_Counter

def Prob_Math(file, team1, team2):

    '''Calculates the expected value of scoring 1 goal through all the chances for each team in the last minute'''
    events = Shot_Filter.Shot_Filter(file)
    print(events)
    df = pandas.read_json(file)

    TeamA = team1
    TeamB = team2

    NotGoalA = 1
    NotGoalB = 1

    for i in events:
        if (df.loc[i, 'possession_team']['name']) == TeamA:
            k = df.loc[i, 'shot']['statsbomb_xg']
            NotGoalA = NotGoalA * (1 - k)

        elif (df.loc[i, 'possession_team']['name']) == TeamB:
            p = df.loc[i, 'shot']['statsbomb_xg']
            NotGoalB = NotGoalB * (1-p)
    
    return {TeamA: 1 - NotGoalA, TeamB: 1 - NotGoalB} 


#Prob_Math('/Users/sam/VSCode/Rough/data1.json')