# DSCI522_309
Workflows Analysis Project for DSCI 522

# Project Proposal

## Data Source
The data for this project was obtained from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset) and consists of webpage metrics from an online shopping website. 

## Research Question 
The central question of this project will be predictive. Based on webpage visit duration, proximity to a holiday and additional variables can we accuratley identify which shopping sessions will end in a sale?

## Analysis Plan 
The main objective will be to build a binary classification model. 

Our preprocessing and analysis plan should consist of the following activities:

- We need to study how the skewness in the explanatory variables will affect our modeling. For example, 75% of the data has PageValues of 0.
- Standardize/Normalize variables because variables have very different scales
- Merge categorical variables to balance the categories. For e.g. OperatingSystems variable with categories [4,5,6,7] constitute only ~5% of the data.
- Tackle class imbalance in the response variable since the target has only 15% of positive responses
- Decide a methodology for outlier treatment & feature selection


## Exploratory Data Analysis
We plan to show a grid of bar plots detailing the frequency distributions of the 8 categorical variables. It will be a series of side-by-side barplots, one plot for each variable. For example, with type of web browser the plot would show the number of sessions with a specific brower for sales and no sales. 

One data table we plan to show is the cumulative quantile distribution for the quantitative variables. For example, the table would show the cumulative distribution of users' time duration spent on the webpage.

## Analysis Outputs 
We plan to provide tables of the following as the outputs of our analysis: 
- ROC curve 
- F1 score 
- Predictor importance 

In additiona we plan to show the following figure:
- Confusion Matrix plot