import os
import Beta1
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


events_files = []
for dirpath, dirnames, files in os.walk('./data/events'):
    for file_name in files:
        events_files.append(file_name)



def data_generator(events_files):
    auxteam_list = []
    for i in range(len(events_files)):
        auxteam_list.append(Team_Names('./data/events/' + events_files[i])[0])
        auxteam_list.append(Team_Names('./data/events/' + events_files[i])[1])
        print('working')
    global team_list_data
    team_list_data = list(set(auxteam_list))
    return team_list_data
#print(len(team_list))

#draftdf = pandas.DataFrame({'Team' : team_list_data}, columns = ['Team'])

#draftdf.to_csv('DraftAnalysis.csv')

input_team = 'Arsenal'

for i in range(len(events_files)):
    if input_team in Team_Names('./data/events/' + events_files[i]):
        Beta1.main('./data/events/' + events_files[i])