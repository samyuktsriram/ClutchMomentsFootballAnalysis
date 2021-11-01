from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
import Shot_Seeker

def Shot_Filter(file):
    '''to filter out the shots after the 80th minute
    Takes in a .json file from StatsBomb's Open Datatset and returns a list of dictionary items for each shot'''


    df = pandas.read_json(file)

    required_shots = Shot_Seeker.Shot_Seeker(file)
    shots_80 = []

    for i in required_shots:
        if df.loc[i, 'minute'] > 80:
            shots_80.append(i)
    return shots_80

#Shot_Filter(file)
