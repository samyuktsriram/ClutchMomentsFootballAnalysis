from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
import Shot_Seeker
import Shot_Filter
import Score_Counter

file = '/Users/sam/VSCode/Rough/data1.json'

def Event_Reporter(file, team1, team2):

    '''Presents a list of 'clutch' events and their impact on the score'''

    df = pandas.read_json(file)
    score = Score_Counter.Score_Counter(file, 80)
    print('The score at the 80th minute was' , score) # print something like "The score at the 80th minute was:"

    events = Shot_Filter.Shot_Filter(file)
    
    TeamA = team1
    TeamB = team2

    Score1 = score[team1]
    Score2 = score[team2]

    for i in events:
        #This piece of code looks for goals
        if (df.loc[i, 'shot']['outcome']['id']) == 97: #this is the id for goal
            if (df.loc[i, 'possession_team']['name']) == TeamA:
                print(TeamA, 'scored a goal!')
                Score1 = Score1 + 1
            elif (df.loc[i, 'possession_team']['name']) == TeamB:
                Score2 = Score2 + 1
                print(TeamB, 'scored a goal!')
        


        #elif (df.loc[i, 'shot']['outcome']['id']) == 97: #Look for the code for one-on-ones
    
    score_final = Score_Counter.Score_Counter(file, 150) #150 is just a really big number, no football games go on that long
    print('The final score was' , score_final)




#Event_Reporter(file, 'Barcelona', 'Real Sociedad')