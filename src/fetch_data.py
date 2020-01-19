# Author Cheng Min
# Date: 2020-01-18

"""This script fetches the online shoppers intetion data from UCI website.
   The description of the data can be found at 
   https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset
   After fetching the data, the data is splitted into training and testing set and 
   stored in the data folder

   Usage: fetch_data.py [--url=<url>] [--test_size=<test_size>]

   Options:
   --url=<url> The URL path to the csv file [default: "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"]
   --test_size=<test_size> The size of the test size [default: 0.2]

"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from docopt import docopt

opt = docopt(__doc__)

def main(url, test_size):
    # Read the data
    raw_data = pd.read_csv(url)
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(raw_data.drop(columns='Revenue'), 
                                                    raw_data['Revenue'], 
                                                    test_size=test_size, 
                                                    random_state=522)
    
    # Save the data
    X_train.to_csv('data/X_train.csv', index=False)
    pd.DataFrame(y_train).to_csv('data/y_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
    pd.DataFrame(y_test).to_csv('data/y_test.csv', index=False)

def test_url(url):
   test = np.DataSource()
   assert test.exists(url), "Invilid URL, please check the URL!"

# Set the default values for inputs
if opt["--url"] is None:
   opt["--url"] = "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"
if opt["--test_size"] is None:
   opt["--test_size"] = 0.2
   
test_url(opt["--url"])

if __name__ == "__main__":
   main(opt["--url"], float(opt["--test_size"]))
 