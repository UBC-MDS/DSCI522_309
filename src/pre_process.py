# Author Cheng Min
# Date: 2020-01-23

"""Cleans, splits and pre-processes (scales) the online shoppers intetion data from UCI website:
   https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset
   Writes the training and test data to separate csv files.
   The column names of the data should be: "Administrative", "Informational", "ProductRelated",
   "Administrative_Duration", "Informational_Duration", "ProductRelated_Duration", "BounceRates", 
   "ExitRates", "PageValues", "ProductRelated" (for numerical variables) and "Revenue" (for labels).

   Usage: src/pre_process.py --input=<input> --out_dir=<out_dir>

   Options:
    --input=<input>       Path to raw data, filename should be included
    --out_dir=<out_dir>   Local file path to folder in which the processed data csvs will be written

"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import QuantileTransformer, OneHotEncoder
from sklearn.compose import ColumnTransformer
import os
from docopt import docopt

opt = docopt(__doc__)

def main(input_data, out_dir):
    # Check the out_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Read the data from the raw data
    raw_data = pd.read_csv(input_data)

    # Split the data
    training, test = train_test_split(raw_data, test_size=0.2, random_state=522)

    # Save the data
    training.to_csv(out_dir + "/training_for_eda.csv", index=False)

    # Split the data to features and reponses
    X_train = training.drop(columns = "Revenue")
    y_train = training["Revenue"]

    X_test = test.drop(columns = "Revenue")
    y_test = test["Revenue"]

    # Separate numerical and categorical varibles
    num_vars_1 = ["Administrative", "Informational", "ProductRelated"]
    num_vars_2 = ["Administrative_Duration", "Informational_Duration", "ProductRelated_Duration", 
                    "BounceRates", "ExitRates", 
                    "PageValues", "ProductRelated"]
    target = "Revenue"
    cat_vars = list(set(X_train.columns)-set(num_vars_1) - set(num_vars_2) - set(target))
    num_vars = list(set(X_train.columns) - set(cat_vars))

    # Pre-process the data
    # Use QuantileTransformer for numerical variables
    # Use OneHotEncoder for categorical variables
    preprocessor = ColumnTransformer(transformers=[
        ('qt_transform', QuantileTransformer(random_state=0), num_vars),
        ('ohe', OneHotEncoder(drop='first'), cat_vars)])

    # Fit and transform the training data
    transformed_data = preprocessor.fit_transform(X_train)
    col_names = (num_vars + list(preprocessor.named_transformers_['ohe'].get_feature_names(cat_vars)))

    # Save the transformed data as data frames
    X_train = pd.DataFrame(transformed_data.toarray(), index=X_train.index, columns=col_names)
    X_test = pd.DataFrame(preprocessor.transform(X_test).toarray(), index=X_test.index, columns=col_names)

    # Write the data to the disc
    X_train.to_csv(out_dir + "/X_train.csv", index=False)
    pd.DataFrame(y_train).to_csv(out_dir + "/y_train.csv", index=False)
    X_test.to_csv(out_dir + "/X_test.csv", index=False)
    pd.DataFrame(y_test).to_csv(out_dir + "/y_test.csv", index=False)

if __name__ == "__main__":
    main(opt["--input"], opt["--out_dir"])