"""
utility functions for pandas dataframes
"""

import pandas as pd
import numpy as np

"""
a bunch of dataframe's with a different number of nulls in each
column to test the functions with
"""
test_col_1 = [np.nan,      2,      3,      4,      5]
test_col_2 = [np.nan, np.nan,      3,      4,      5]
test_col_3 = [np.nan, np.nan, np.nan,      4,      5]
test_col_4 = [np.nan, np.nan, np.nan, np.nan,      5]
test_col_5 = [np.nan, np.nan, np.nan, np.nan, np.nan]

test_1_df = pd.DataFrame({
    'col_1': test_col_1, 
    'col_2': test_col_2, 
    'col_3': test_col_3,
    'col_4': test_col_4,
    'col_5': test_col_5,
})

test_2_df = pd.DataFrame({
    'col_2': test_col_2, 
    'col_3': test_col_3, 
    'col_4': test_col_4,
    'col_5': test_col_5,
    'col_1': test_col_1,
})

test_3_df = pd.DataFrame({
    'col_3': test_col_3, 
    'col_4': test_col_4, 
    'col_5': test_col_5,
    'col_1': test_col_1,
    'col_2': test_col_2,
})

test_4_df = pd.DataFrame({
    'col_4': test_col_4, 
    'col_5': test_col_5, 
    'col_1': test_col_1,
    'col_2': test_col_2,
    'col_3': test_col_3,
})

test_5_df = pd.DataFrame({
    'col_5': test_col_5, 
    'col_1': test_col_1, 
    'col_2': test_col_2,
    'col_3': test_col_3,
    'col_4': test_col_4,
})


X_df = pd.DataFrame([6, 7, 8, 9, 10, np.nan])
y_df = pd.DataFrame([11, 12, 13, 14, 15, np.nan])

class Splitter:
    """
    A class that will split a dataframe into 3 (more or less) equal portions
    This is probably a terrible thing to do with classes (definitely feels more like a function thing).
    But it does work!

    If there wasn't already a sklearn function that did a train test split I'd probably kit this out more.
    Most notably I'd add a variable to determine the number of splits, and
    a split method called "transform" for the y_data after the X_data has been acted on
    by "split_transform" similar to how category encoders work.
    """
    def __init__(self):
        self.thing = 5
    def split_transform(self, dataframe):
        data_size = len(dataframe)
        num_of_splits = 3
        X_train = dataframe[0:data_size // num_of_splits]
        X_val = dataframe[data_size // 3:2 * data_size // num_of_splits]
        X_test = dataframe[2 * data_size // num_of_splits:]
        return(X_train, X_val, X_test)



# very basic train/val/test split function
def train_val_test_split(X_dataframe, y_dataframe):
    """A function that will split a list into 3 equally sized lists"""
    data_size = len(X_dataframe)
    X_train = X_dataframe[0:data_size // 3]
    X_val = X_dataframe[data_size // 3:2 * data_size // 3]
    X_test = X_dataframe[2 * len(X_dataframe) // 3:]

    data_size = len(y_dataframe)
    y_train = y_dataframe[0:len(y_dataframe) // 3]
    y_val = y_dataframe[len(y_dataframe) // 3: 2 * len(y_dataframe) // 3]
    y_test = y_dataframe[2 * len(y_dataframe) // 3:]

    return X_train, X_val, X_test, y_train, y_val, y_test


def count_nulls(dataframe):
    """
    Prints the number of nulls in each column of a given Dataframe
    as well as returning a list of the number of nulls in each column
    """

    if type(dataframe) == pd.DataFrame:
        nulls = []
        for col in dataframe.columns:
            null_ammount = dataframe[col].isna().sum()
            nulls.append(null_ammount)
            print("There are ", null_ammount, " NaN values in column ", col, ".")
    else: 
        nulls = 0
        for entree in dataframe:
            if np.isnan(entree):
                nulls += 1
    return nulls
