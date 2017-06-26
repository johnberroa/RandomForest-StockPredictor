"""
A random forest classifier aimed at determining whether a stock will be higher or lower after some given amount of days.
Replication of Khaidem, Saha, & Roy Dey (2016)

Documentation on function:
http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier as make_forest
import numpy as np

'''
### Outline ###
We have a bunch of columns of different length target values
We drop all target values except the ones we want to analyze (or else when we remove NA we will remove too much data)
We then input the data and features in to the first .fit parameter, and the labels in the second
'''

num_features = 4
prediction_window = 10
full_data = pd.read_csv('data_preprocessed.csv')


# drop all target columns not to be analyzed
headers = full_data.columns.values
headers = headers[12:] # should return just the headers of the DI-# (target values) FIXED
headers = headers[headers!='DI-'+str(prediction_window)]
selected_data = full_data.drop(headers, axis=1) # dunno if axis 1 is right
selected_data = selected_data.dropna(axis=0, how='any') # using the subset parameter might allow us to skip dropping other targets?

selected_data.drop(["Unnamed: 0"], axis = 1, inplace = True)
selected_data.drop(["Date"], axis = 1, inplace = True)
selected_data.drop(["Symbol"], axis = 1, inplace = True)

# Split in Test-x and Test-y
data_y = selected_data['DI-'+str(prediction_window)].as_matrix()
#print(data_y)
selected_data.drop(['DI-'+str(prediction_window)], axis = 1, inplace = True)
data_x = selected_data.as_matrix()
#print(data_x)

# Ignore the warning. Works anyway
Random_Forest = make_forest(max_features=num_features, bootstrap=True, oob_score=True, verbose=1)

Random_Forest.fit(data_x, data_y)

# Test using 1D array, should be 2d but yeah. Works. Just for the sake of it
print("TEST: TREE VS ORIGINAL")
print(str(Random_Forest.predict(data_x[10])) + " vs. " + str(data_y[10]))
