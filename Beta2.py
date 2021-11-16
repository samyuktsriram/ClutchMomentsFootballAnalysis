from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
from Event_Reporter import Event_Reporter
import Shot_Seeker
import Shot_Filter
import Score_Counter
import Team_Names
import Prob_Math


def main(file, input_team):

    TeamA, TeamB = Team_Names.Team_Names(file)
    if TeamA == input_team:
        input_team = TeamA
        opponent = TeamB
    if TeamB == input_team:
        input_team = TeamB
        opponent = TeamA
    score_80 = Score_Counter.Score_Counter(file, 80)
    score_ft = Score_Counter.Score_Counter(file, 150)
    gd_80 = score_80[input_team] - score_80[opponent]
    gd_FT = score_ft[input_team] - score_ft[opponent]
    p = Prob_Math.Prob_Math(file, input_team, opponent)
    #desc = Event_Reporter(file, input_team, opponent, False)

    return (input_team, (input_team, opponent), score_80, score_ft, p[input_team], p[opponent], gd_80, gd_FT)
    #InputTeam, TeamsPlaying, Scoreat80, ScoreatFullTime, p(input_team), p(opponent), GDat80, GDatFT
#main('/Users/sam/VSCode/Rough/data1.json', 'Barcelona')