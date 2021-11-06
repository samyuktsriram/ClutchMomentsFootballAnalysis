from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
import Shot_Seeker
import Shot_Filter
from Team_Names import Team_Names

def Score_Counter(file, time):
    '''to keep track of the score of a match before the 'time' minute'''

    df = pandas.read_json(file)

    required_shots = Shot_Seeker.Shot_Seeker(file)

    shots_80 = []
    row_shots = []

    Team1 , Team2  = Team_Names(file)

    global Score1
    global Score2
    Score1 = 0
    Score2 = 0

    for i in required_shots:
        if df.loc[i, 'minute'] <= time:
            shots_80.append(df.loc[i, 'shot'])
            row_shots.append(i)

    
    for i in row_shots:
        if (df.loc[i, 'shot']['outcome']['id']) == 97: #this is the id for goal
            if (df.loc[i, 'possession_team']['name']) == Team1:
                Score1 = Score1 + 1
            elif (df.loc[i, 'possession_team']['name']) == Team2:
                Score2 = Score2 + 1

    return {Team1 : Score1, Team2 : Score2}



#Score_Counter('/Users/sam/VSCode/Rough/data1.json', 40)
#Score_Counter('/Users/sam/VSCode/Rough/data1.json', 70)
#Score_Counter('/Users/sam/VSCode/Rough/data1.json', 90)
#Score_Counter('/Users/sam/VSCode/Rough/data1.json', 100)