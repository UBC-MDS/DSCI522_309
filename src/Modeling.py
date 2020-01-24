# Author Shivam Verma
# Date: 2020-01-23

"""This script builds a Light GBM model to predict shoppers tendancy to buy:
   Writes the performance metrics(f1-score, ROC-AUC, precision, recall), feature Importance and predicted probability on training and test data to separate csv files.

   Usage: src/Modeling.py --datapath=<datapath> --out_dir=<out_dir>

   Options:
    --datapath=<datapath>       Directory path to transformed data after preprocessing, filename should not be included
    --out_dir=<out_dir>         Path to directory where all the results should be written

"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from collections import Counter
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score, f1_score, precision_score, recall_score
import os
from docopt import docopt

opt = docopt(__doc__)

def main(input_url, out_dir):
    # Check the out_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    print(input_url + '/X_train.csv')

    # Read the data from the raw data
    X_train = pd.read_csv(input_url + '/X_train.csv')
    y_train = pd.read_csv(input_url + '/y_train.csv')

    X_test = pd.read_csv(input_url + '/X_test.csv')
    y_test = pd.read_csv(input_url + '/y_test.csv')

    # Separate numerical and categorical varibles
    target = "Revenue"

    # Light Gradient Boosting
    parameters = {'n_estimators':np.arange(100,210,10), 'max_depth':np.arange(5,10,1), 'class_weight':['balanced', None]}
    lgbm = LGBMClassifier(num_leaves = 50, random_state=123)
    clf = GridSearchCV(lgbm, parameters, refit=True, cv=5, return_train_score=True)
    clf.fit(X_train, y_train)

    # Saving Feature Importance
    Feature_Imp = pd.DataFrame({'Feature_Imp':clf.best_estimator_.feature_importances_, 'col_names':X_train.columns})
    Feature_Imp.to_csv(out_dir+'/Feature_Imp.csv', index=False)

    # Saving Hyper parameter optimization results
    Hyp_opt_result = pd.DataFrame(clf.cv_results_)
    Hyp_opt_result = Hyp_opt_result[["param_class_weight","param_max_depth","param_n_estimators","mean_train_score","std_train_score","mean_test_score","std_test_score"]].iloc[clf.best_index_,]
    Hyp_opt_result.to_csv(out_dir+'/GridSearchCV.csv', index=False)
    print("The best parameters from GridSearch are: ", clf.best_params_)
    print("The error on Train is: ", 1-clf.score(X_train, y_train), "and test is: ", 1-clf.score(X_test, y_test))

    # Saving ROC
    fpr, tpr, thresholds = roc_curve(y_train, clf.predict_proba(X_train)[:,1])
    ROC_train_data = pd.DataFrame({'fpr': fpr, 'tpr':tpr, 'thresholds':thresholds, 'AUC':roc_auc_score(y_train, clf.predict_proba(X_train)[:,1])})
    ROC_train_data.to_csv(out_dir+'/ROC_train_data.csv', index=False)

    fpr, tpr, thresholds = roc_curve(y_test, clf.predict_proba(X_test)[:,1])
    ROC_test_data = pd.DataFrame({'fpr': fpr, 'tpr':tpr, 'thresholds':thresholds, 'AUC':roc_auc_score(y_test, clf.predict_proba(X_test)[:,1])})
    ROC_test_data.to_csv(out_dir+'/ROC_test_data.csv', index=False)


    # Saving predictions
    pred_train = X_train.copy()
    pred_train['predict_proba'] = clf.predict_proba(X_train)[:,1]
    pred_train['skl_predict'] = clf.predict(X_train)
    pred_train[target] = y_train
    pred_train.to_csv(out_dir+'/Training_pred.csv', index=False)

    pred_test = X_test.copy()
    pred_test['predict_proba'] = clf.predict_proba(X_test)[:,1]
    pred_test['skl_predict'] = clf.predict(X_test)
    pred_test[target] = y_test
    pred_test.to_csv(out_dir+'/Test_pred.csv', index=False)

    # Saving How Performance metric changes with threshold
    threshold_list = np.arange(np.min(pred_train['predict_proba']), np.max(pred_train['predict_proba']), 0.01)
    f1_score_train = [f1_score(y_pred = pred_train['predict_proba']>t, y_true = y_train) for t in threshold_list]
    precision_score_train = [precision_score(y_pred = pred_train['predict_proba']>t, y_true = y_train) for t in threshold_list]
    recall_score_train = [recall_score(y_pred = pred_train['predict_proba']>t, y_true = y_train) for t in threshold_list]
    metric_threshold_train = pd.DataFrame({'threshold': threshold_list, 'f1_score_train':f1_score_train, 'precision_score_train':precision_score_train, 'recall_score_train':recall_score_train})
    metric_threshold_train.to_csv(out_dir+'/metric_by_threshold_train.csv', index=False)

    threshold_list = np.arange(np.min(pred_test['predict_proba']), np.max(pred_test['predict_proba']), 0.01)
    f1_score_test = [f1_score(y_pred = pred_test['predict_proba']>t, y_true = y_test) for t in threshold_list]
    precision_score_test = [precision_score(y_pred = pred_test['predict_proba']>t, y_true = y_test) for t in threshold_list]
    recall_score_test = [recall_score(y_pred = pred_test['predict_proba']>t, y_true = y_test) for t in threshold_list]
    metric_threshold_test = pd.DataFrame({'threshold': threshold_list, 'f1_score_test':f1_score_test, 'precision_score_test':precision_score_test, 'recall_score_test':recall_score_test})
    metric_threshold_test.to_csv(out_dir+'/metric_by_threshold_test.csv', index=False)

    # print(classification_report(clf.predict(X_train), y_train))
    print("---------------------")
    print("Confusion Matrix of Train Data")
    print(pd.DataFrame(data=confusion_matrix(y_pred = pred_train['skl_predict'], y_true = y_train), 
                    index=['Actual_Negative', 'Actual_Positive'], 
                    columns=['Predict_Negative', 'Predict_Positive']))
    print("---------------------")
    print(classification_report(clf.predict(X_test), y_test))
    print("---------------------")
    print("Confusion Matrix of Test Data")
    print(pd.DataFrame(data=confusion_matrix(y_pred = pred_test['skl_predict'], y_true = y_test), 
                    index=['Actual_Negative', 'Actual_Positive'], 
                    columns=['Predict_Negative', 'Predict_Positive']))

if __name__ == "__main__":
    print(opt["--datapath"] + '/X_train.csv')
    main(opt["--datapath"], opt["--out_dir"])
