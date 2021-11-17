from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
import Shot_Seeker
import Shot_Filter
import Score_Counter
import Team_Names
import Prob_Math


def main(file, input_team):

    '''Beta2: Data Engineering
  1. Uses a list of teams in the dataset to find and sort games based on teams in the dataset.
  2. Creates a new database with the following information for every game: 'Team', 'TeamsPlaying', 'Score_at_80', 'Score_at_FT', 'GoalLikelihood_Team', 'GoalLikelihood_Opp', 'GoalDiff_at80', 'GoalDiff_atFT '
  3. Exports this new database to excel, csv. This dashboard can be used to examine team performance, find avarages, standard deviations in GoalLikelihoods across teams, further analysis over the entire set of matches.'''

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

    return (input_team, (input_team, opponent), score_80, score_ft, p[input_team], p[opponent], gd_80, gd_FT)
    #InputTeam, TeamsPlaying, Scoreat80, ScoreatFullTime, p(input_team), p(opponent), GDat80, GDatFT