from numpy import NaN
import pandas
from pandas.core.frame import DataFrame
import Shot_Seeker

def Shot_Filter(file):
    '''to filter out the shots after the 80th minute'''


    df = pandas.read_json(file)

    required_shots = Shot_Seeker.Shot_Seeker(file)
    shots_80 = []

    for i in required_shots:
        if df.loc[i, 'minute'] > 80:
            shots_80.append(i)
    return shots_80

#file = '/Users/sam/VSCode/Rough/data2.json'
#Shot_Filter(file)