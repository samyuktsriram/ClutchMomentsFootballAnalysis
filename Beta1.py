from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
from Event_Reporter import Event_Reporter
import Shot_Seeker
import Shot_Filter
import Score_Counter
import Team_Names
import Prob_Math


def main(file):

    TeamA, TeamB = Team_Names.Team_Names(file)
    print('The likelihood of each team scoring a goal in this phase are', Prob_Math.Prob_Math(file, TeamA, TeamB))
    Event_Reporter(file, TeamA, TeamB)
    
#main('/Users/sam/VSCode/Rough/data1.json')