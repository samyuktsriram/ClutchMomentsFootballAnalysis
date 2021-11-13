from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
import Shot_Seeker
import Shot_Filter
import Score_Counter
import socplot

file = '/Users/sam/VSCode/Rough/data1.json'

def Event_Reporter(file, team1, team2):

    '''Presents a list of 'clutch' events and their impact on the score'''

    pitch = socplot.Pitch()

    df = pandas.read_json(file)
    score = Score_Counter.Score_Counter(file, 80)
    print('The score at the 80th minute was' , score) # print something like "The score at the 80th minute was:"

    events = Shot_Filter.Shot_Filter(file)
    
    TeamA = team1
    TeamB = team2

    Score1 = score[team1]
    Score2 = score[team2]
    #The following code extracts information about the shots and their outcomes, and prints them
    for i in events:
        #This piece of code looks for goals
        if (df.loc[i, 'shot']['outcome']['id']) == 97: #this is the id for goal
            if (df.loc[i, 'possession_team']['name']) == TeamA:
                if 'deflected' in  df.loc[i, 'shot']:
                    if df.loc[i, 'shot']['deflected'] == True:
                        print(TeamA, 'scored a goal with a deflected shot!')        
                else: print(TeamA, 'scored a goal!')
                Score1 = Score1 + 1
                x = ((df.loc[i,'location'][0]), 80 - (df.loc[i,'location'][1]))
                y = ((df.loc[i, 'shot']['end_location'][0]), 80 - (df.loc[i, 'shot']['end_location'][1]))
                pitch.plot_pass(x,y)
            elif (df.loc[i, 'possession_team']['name']) == TeamB:
                Score2 = Score2 + 1
                if 'deflected' in  df.loc[i, 'shot']:
                    if df.loc[i, 'shot']['deflected'] == True:
                        print(TeamB, 'scored a goal with a deflected shot!')        
                else: print(TeamB, 'scored a goal!')
                x = ((df.loc[i,'location'][0]), 80 -(df.loc[i,'location'][1]))
                y = ((df.loc[i, 'shot']['end_location'][0]), 80 -(df.loc[i, 'shot']['end_location'][1]))
                pitch.plot_pass(x,y, color = 'red')
        
        if (df.loc[i, 'shot']['outcome']['id']) != 97:
            if 'one_on_one' in df.loc[i, 'shot']:
                if df.loc[i, 'shot']['one_on_one'] == True:
                    if (df.loc[i, 'possession_team']['name']) == TeamA:
                        print(TeamA, 'missed a one-on-one!')
                    elif (df.loc[i, 'possession_team']['name']) == TeamB:
                        print(TeamB, 'missed a one-on-one!')

        if df.loc[i, 'shot']['outcome']['name'] == 'Saved':
            if (df.loc[i, 'possession_team']['name']) == TeamA:
                print(TeamA, 'had a shot saved!')
            elif (df.loc[i, 'possession_team']['name']) == TeamB:
                print(TeamB, 'had a shot saved!')
        
        if df.loc[i, 'shot']['outcome']['name'] == 'Off T':
            if (df.loc[i, 'possession_team']['name']) == TeamA:
                print(TeamA, 'took a shot, but it was off target.')
            elif (df.loc[i, 'possession_team']['name']) == TeamB:
                print(TeamB, 'took a shot, but it was off target.')

        if df.loc[i, 'shot']['outcome']['name'] == 'Blocked':
            if (df.loc[i, 'possession_team']['name']) == TeamA:
                print(TeamA, 'took a shot, but it was blocked.')
            elif (df.loc[i, 'possession_team']['name']) == TeamB:
                print(TeamB, 'took a shot, but it was blocked.')

        if df.loc[i, 'shot']['outcome']['name'] == 'Post':
            if (df.loc[i, 'possession_team']['name']) == TeamA:
                print(TeamA, 'took a shot, but it hit the post!')
            elif (df.loc[i, 'possession_team']['name']) == TeamB:
                print(TeamB, 'took a shot, but it hit the post!')
    
    score_final = Score_Counter.Score_Counter(file, 150) #150 is just a really big number, no football games go on that long
    print('The final score was' , score_final)
    pitch.show()




Event_Reporter(file, 'Barcelona', 'Real Sociedad')