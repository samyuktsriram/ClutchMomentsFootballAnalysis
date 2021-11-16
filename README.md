# ClutchMomentsFootball Analysis: 
An ongoing project to identify and analyse decisive goals and plays made in high-pressure moments of a football match.

This is a personal project to gain exposure to data-driven analysis, data visualization and engineering, sports related data science and gain hands-on experience working on a data science project. The project employs python and pandas to conduct the analysis.

The data used is from Statsbomb's Open Data, found here: https://github.com/statsbomb/open-data

The goal of the project is to create 2 programs:

Beta1: Data Visualization and Extraction
  1. Accepts a list of .json files from Statsbomb's Open Data source, containing event data for each match.
  2. Finds and filters out shots made in the 80th+ minute, high Expected Goal (xG) Blocks, one-on-one opportunities, etc.
  3. Analyse whether/ how the match was decided in the 80th+ minutes, calculating the likelihood of a goal being scored by each team in that time.
  4. Return the information on the event(s) that decided the outcome of the match. Present a visual of match-scoring goal(s).

Beta2: Data Engineering
  1. Uses a list of teams in the dataset to find and sort games based on teams in the dataset.
  2. Creates a new database with the following information for every game: 'Team', 'TeamsPlaying', 'Score_at_80', 'Score_at_FT', 'GoalLikelihood_Team', 'GoalLikelihood_Opp', 'GoalDiff_at80', 'GoalDiff_atFT '
  3. Exports this new database to excel, csv. The above information can be used to find avarages, standard deviations in GoalLikelihoods across teams, further analysis over the entire set of matches.


Documentation of code:
  1. Shot_Seeker.py : To open a .json file from StatsBomb's Open Dataset, find the positions of all the shots within the file, and return a list with those values, to be used in subsequent analysis.
  2. Shot_Filter.py : To open a .json database and filter out the shots after the 80th minute.
  3. Score_Counter.py : To open a .json database, identify goals scored along with their timestamp, filter out goals scored before an inputable time, and return a dictionary containing the scoreline of the match at that time.
  4. Event_Reporter.py : To identify and present crucial events (goals, blocks, etc) in the match from the 80th minute onwards. Uses Statsbomb's pitch visualization code to present each goal on a pitch.
  5. Prob_Math.py : To calculate the expected goals in the 80th minute onwards based on the Statsbomb xG of the shots taken.
  6. Team_Names.py : To extract the names of the teams playing from the .json database.
  7. Beta1.py : To analyse a specific match's events. Calculates the expected goals in the 80th minute onwards phase for each team, presents any goals scored in that time, and finally presents the final score of the match.
  8. File_Looper.py : To loop over all the 941 events files in the dataset and prepare them for further analysis, through Beta1.py or Beta2.py. Can also be used to find a specific team's games in the dataset. Includes code to create a set of teams that are present in the dataset.
  9. socplot.py : Statsbomb's pitch visualization tool, used in Event_Reporter.py
  10. Beta2.py : To create a new database. This will contain the following data for every team's match: 'Team', 'TeamsPlaying', 'Score_at_80', 'Score_at_FT', 'GoalLikelihood_Team', 'GoalLikelihood_Opp', 'GoalDiff_at80', 'GoalDiff_atFT'. Export to csv or excel to be used as dashboard for further insights.
