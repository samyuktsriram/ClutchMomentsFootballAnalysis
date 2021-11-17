import os
import Beta1
from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
import Shot_Seeker
import Shot_Filter
import Score_Counter
import Beta2

#==================================================================
# The following code will create a csv file with:
# InputTeam, TeamsPlaying, Scoreat80, ScoreatFullTime, p(input_team), p(opponent), GDat80, GDatFT
# for each match

def Team_Names(file):
    
    '''Returns the names of the 2 teams playing the match in a given file.'''

    team_list = []
    df = pandas.read_json(file)
    for i in range(2):
        team_list.append(df.loc[i, 'team']['name'])

    return (team_list[0], team_list[1])

#This step creates a list of all the match files in the folder, will be used to loop over all the files.

events_files = []
for dirpath, dirnames, files in os.walk('./data/events'):
    for file_name in files:
        events_files.append(file_name)


def data_generator(events_files):
    '''Returns a set of all the team names across all the matches in the dataset'''
    auxteam_list = []
    for i in range(len(events_files)):
        auxteam_list.append(Team_Names('./data/events/' + events_files[i])[0])
        auxteam_list.append(Team_Names('./data/events/' + events_files[i])[1])
        print('working')
    global team_list_data
    team_list_data = list(set(auxteam_list))
    return team_list_data

team_list_data = data_generator(events_files)
input_team_list = []
TeamsPlaying_list = []
Scoreat80_list = []
ScoreatFT = []
input_team_P =[]
opponent_P = []
GDat80 = []
GDatFT = []

#input_team = ('Arsenal')
for k in team_list_data:
    print('working on', k)
    input_team = k
    for i in range(len(events_files)):
        if input_team in Team_Names('./data/events/' + events_files[i]):
            print('found!', i)
            p = Beta2.main('./data/events/' + events_files[i], input_team)
            input_team_list.append(p[0])
            TeamsPlaying_list.append(p[1])
            Scoreat80_list.append(p[2])
            ScoreatFT.append(p[3])
            input_team_P.append(p[4])
            opponent_P.append(p[5])
            GDat80.append(p[6])
            GDatFT.append(p[7])

#InputTeam, TeamsPlaying, Scoreat80, ScoreatFullTime, p(input_team), p(opponent), GDat80, GDatFT
Dict1 = {}
Dict1 = {'Team' : input_team_list, 'TeamsPlaying': TeamsPlaying_list, 'Score_at_80':Scoreat80_list, 'Score_at_FT': ScoreatFT, 'GoalLikelihood_Team':input_team_P, 'GoalLikelihood_Opp': opponent_P, 'GoalDiff_at80':GDat80, 'GoalDiff_atFT':GDatFT}
draftdata1 = pandas.DataFrame(Dict1, columns = ['Team', 'TeamsPlaying', 'Score_at_80', 'Score_at_FT', 'GoalLikelihood_Team', 'GoalLikelihood_Opp', 'GoalDiff_at80', 'GoalDiff_atFT'])
draftdata1.head()
draftdata1.to_csv('FullData.csv')

#================================================================================
# The following code loops over a range of matches and provides a report on the shots in the 80+ minutes.

for i in range(200,205): #Set to len(events_files) for entire dataset.
    Beta1.main('./data/events/' + events_files[i], False) #Set to True for pitch visualization

