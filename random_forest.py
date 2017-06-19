"""
A random forest classifier aimed at determining whether a stock will be higher or lower after some given amount of days.
Replication of Khaidem, Saha, & Roy Dey (2016)

Documentation on functions:
http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html
"""

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

'''
### Outline ###
We need to create labels defined as Sign(Close at predicted day - Close price some D days before predicted price)
    Therefore, we will have to drop out the first few days of each stock for the same reason that we had to drop the
    first few days for the indicators (there won't be enough data to calculate the label)
When we train the classifier, we input the "Close price some D days before predicted price", and split based on the
    values of the technical indicators
We need to create a DecisionTreeClassifier with the gini impurity separator and other parameters that match the paper
We then create a BaggingClassifier and input the DecisionTreeClassifier as the base_estimator
'''
prediction_window = 30

decision_tree = DecisionTreeClassifier(criterion='gini', max_depth=None) # max_depth can be controlled if we desire
# oob_score same as paper, verbose so we know what's going on
random_forest = BaggingClassifier(base_estimator=decision_tree, bootstrap=True, oob_score=True, verbose=1)

random_forest.fit(prices, labels)