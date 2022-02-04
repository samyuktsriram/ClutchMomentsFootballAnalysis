from numpy import size
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_clean(t1, t2):
    '''Opens Team_Performance_Beta2.xlsx, does some additional cleaning, and return a tuple for input into the plot function
    Inputs:
        Names of the 2 teams that we are interested in as strings.
    Returns:
        A tuple consisting of 2 cleaned dataframes, and 2 team names. Can be used for the plot function below'''

    data = pd.read_excel('Team_Performance_Beta2.xlsx')

    team_1 = t1
    team_2 = t2

    condition = ((data['GoalDiff_at80'].isin([1,0,-1])) & (data['Team'].isin([team_1])))
    condition2 = ((data['GoalDiff_at80'].isin([1,0,-1])) & (data['Team'].isin([team_2])))

    data_filtered_1 = data[condition]
    data_filtered_2 = data[condition2]

    data_filtered_1['GoalDiff_at80'] = data_filtered_1['GoalDiff_at80'].astype('category')
    data_filtered_2['GoalDiff_at80'] = data_filtered_2['GoalDiff_at80'].astype('category')

    return (data_filtered_1, data_filtered_2, t1, t2)


def plot(data_tuple):
    '''Plots the Goal Likelihoods of 2 input teams when the score at the 80th minute is -1, 0, 1.

    Parameters:
        A tuple containing 2 dataframes that have been cleaned by read_clean function, along with the team names for each dataframe.
    Returns:
        A graph with the plot.'''    
    

    #Aesthetic parameters

    sns.set_style('dark')
    color = sns.color_palette("flare")

    #Plotting the figures

    fig, ax = plt.subplots(ncols =2, sharex=True, sharey=True)

    sns.stripplot(y = 'GoalLikelihood_Team', x ='GoalDiff_at80', data = data_tuple[0],\
        jitter = True, palette=color, ax = ax[0])

    sns.stripplot(y = 'GoalLikelihood_Team', x ='GoalDiff_at80', data = data_tuple[1],\
        jitter = True, palette=color, ax = ax[1])

    sns.despine()

    #set the larger axis labels

    fig.supxlabel('Score at the 80th Minute')
    fig.supylabel('Goal Scoring Likelihood')
    fig.suptitle('Goal Scoring Likelihood Distributions', size = 15)
    ax[0].set_title(data_tuple[2] + ' - ' + str(data_tuple[0].count()[0]) + ' games')
    ax[1].set_title(data_tuple[3] + ' - ' + str(data_tuple[1].count()[0]) + ' games')

    #Remove the individual axis lables
    ax[0].set_ylabel('')
    ax[0].set_xlabel('')
    ax[1].set_ylabel('')
    ax[1].set_xlabel('')
    plt.show()


plot(read_clean('Arsenal', 'Real Madrid'))