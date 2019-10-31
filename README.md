# lambdata_new_CurtCalledBurt

This package is comprised of two parts:
1) A function and class that will split a Dataframe into 3 equal parts for a primitive train/val/test split.

2) A function that takes a DataFrame or list and will print the the names of each column in the DataFrame along with the number of NaNs in each column. 
    In the case of a DataFrame it returns a list containing the number of NaNs in each column, if a list it will simply return the number of NaNs.