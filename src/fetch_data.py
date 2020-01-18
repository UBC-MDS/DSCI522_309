# Author Cheng Min
# Date: 2020-01-17

"""This script fetches the online shoppers intetion data from UCI website.
   The description of the data can be found at 
   https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset
   After fetching the data, the data is splitted into training and testing set and 
   stored in the data folder

Usage: python fetch_data.py
"""
import pandas as pd
from sklearn.model_selection import train_test_split

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"
raw_data = pd.read_csv(url)

# Data split
X_train, X_test, y_train, y_test = train_test_split(raw_data.drop(columns='Revenue'), 
                                                    raw_data['Revenue'], 
                                                    test_size=0.20, 
                                                    random_state=522)

# Store the splitted data
X_train.to_csv('../data/X_train.csv', index=False)
pd.DataFrame(y_train).to_csv('../data/y_train.csv', index=False)
X_test.to_csv('../data/X_test.csv', index=False)
pd.DataFrame(y_test).to_csv('../data/y_test.csv', index=False)

