from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
from Event_Reporter import Event_Reporter
import Shot_Seeker
import Shot_Filter
import Score_Counter
import Team_Names
import Prob_Math


def main(file, V=False):
    '''Beta1: Data Visualization and Extraction
  1. Accepts a .json files from Statsbomb's Open Data source, containing event data for each match.
  2. Finds and filters out shots made in the 80th+ minute, high Expected Goal (xG) Blocks, one-on-one opportunities, etc.
  3. Analyse whether/ how the match was decided in the 80th+ minutes, calculating the likelihood of a goal being scored by each team in that time.
  4. Return the information on the event(s) that decided the outcome of the match. Present a visual of match-scoring goal(s).'''

    TeamA, TeamB = Team_Names.Team_Names(file)
    print('This is a match between', TeamA, 'and', TeamB)
    print('The likelihood of each team scoring a goal in this phase are', Prob_Math.Prob_Math(file, TeamA, TeamB))
    Event_Reporter(file, TeamA, TeamB, V)