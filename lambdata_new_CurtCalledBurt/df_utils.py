"""
utility functions for pandas dataframes
"""

import pandas as pd
import numpy as np

test_df = pd.DataFrame([1, 2, 3, 4, 5, np.nan])
X_df = pd.DataFrame([6, 7, 8, 9, 10, np.nan])
y_df = pd.DataFrame([11, 12, 13, 14, 15, np.nan])

"""
A class that will split a dataframe into 3 (more or less) equal portions
This is probably a terrible thing to do with classes (definitely feels more like a function thing).
But it does work!

If there wasn't already a sklearn function that did a train test split I'd probably kit this out more.
Most notably I'd add a variable number of splits, and
a split method for the y_data after the X_data has been acted on
by split_transform.
"""
class Splitter:
    def __init__(self):
        self.thing = 5
    def split_transform(self, dataframe):
        data_size = len(dataframe)
        num_of_splits = 3
        X_train = dataframe[0:data_size // num_of_splits]
        X_val = dataframe[data_size // 3:2 * data_size // num_of_splits]
        X_test = dataframe[2 * data_size // num_of_splits:]
        return(X_train, X_val, X_test)
    """
    def split(self, dataframe):
        data_size = len(dataframe)
        num_of_splits = 3
        X_train = dataframe[0:data_size // num_of_splits]
        X_val = dataframe[data_size // 3:2 * data_size // num_of_splits]
        X_test = dataframe[2 * data_size // num_of_splits:]
    """


# very basic train/val/test split function
def train_val_test_split(X_dataframe, y_dataframe):
    data_size = len(X_dataframe)
    X_train = X_dataframe[0:data_size // 3]
    X_val = X_dataframe[data_size // 3:2 * data_size // 3]
    X_test = X_dataframe[2 * len(X_dataframe) // 3:]

    data_size = len(y_dataframe)
    y_train = y_dataframe[0:len(y_dataframe) // 3]
    y_val = y_dataframe[len(y_dataframe) // 3: 2 * len(y_dataframe) // 3]
    y_test = y_dataframe[2 * len(y_dataframe) // 3:]

    return X_train, X_val, X_test, y_train, y_val, y_test


# a function that tells you how many nulls are in each column of
# your dataframe
def check_for_null(dataframe):
    for col in dataframe.columns:
        null_ammount = dataframe[col].isna().sum()
        print("There are ", null_ammount, " NaN values in column ", col, ".")
    return None
