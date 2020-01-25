# Author Cheng Min
# Date: 2020-01-13

"""This script fetches the online shoppers intetion data from UCI website.
   The description of the data can be found at 
   https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset
   and stored in the data folder specified by argument localpath

   Usage: src/fetch_data.py --localpath=<localpath> [--url=<url>]

   Options:
   --localpath=<localpath> Local file path to folder in which data csvs will be written
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

   raw_data.to_csv(localpath + "/raw_data.csv", index = False) 

def test_url(url):
   test = np.DataSource()
   assert test.exists(url), "Invilid URL, please check the URL!"

# Set the default values for inputs
if opt["--url"] is None:
   opt["--url"] = "https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv"
   
test_url(opt["--url"])

if __name__ == "__main__":
   main(opt["--localpath"], opt["--url"])
 