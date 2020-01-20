# Author Cheng Min
# Date: 2020-01-18

"""This script fetches the online shoppers intetion data from UCI website.
   The description of the data can be found at 
   https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset
   After fetching the data, the data is splitted into training and testing set and 
   stored in the data folder

   Usage: src/fetch_data.py --localpath=<localpath> [--url=<url>]

   Options:
   --localpath=<localpath> Local file path to write the data
   --url=<url> The URL path to the csv file [default: "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"]

"""
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from docopt import docopt

opt = docopt(__doc__)

def main(localpath, url):

   # Check the local path
   if not os.path.exists(localpath):
        os.makedirs(localpath)
   
   # Read the data
   raw_data = pd.read_csv(url)
    
   # Split the data
   X_train, X_test, y_train, y_test = train_test_split(raw_data.drop(columns='Revenue'), 
                                                    raw_data['Revenue'], 
                                                    test_size=0.2, 
                                                    random_state=522)
   localpath_x_train = localpath + "/X_train.csv"
   localpath_y_train = localpath + "/y_train.csv"
   localpath_x_test = localpath + "/X_test.csv"
   localpath_y_test = localpath + "/y_test.csv"
   # Save the data
   X_train.to_csv(localpath_x_train, index=False)
   pd.DataFrame(y_train).to_csv(localpath_y_train, index=False)
   X_test.to_csv(localpath_x_test, index=False)
   pd.DataFrame(y_test).to_csv(localpath_y_test, index=False)

def test_url(url):
   test = np.DataSource()
   assert test.exists(url), "Invilid URL, please check the URL!"

# Set the default values for inputs
if opt["--url"] is None:
   opt["--url"] = "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"
   
test_url(opt["--url"])

if __name__ == "__main__":
   print(opt)
   main(opt["--localpath"], opt["--url"])
 