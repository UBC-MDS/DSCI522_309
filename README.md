
# Online Shopping Intention Predictor

  - author: Lesley Miller, Cheng Min, Shivam Verma

## About

Here we attempt to build a classification model using the light gradient
boosting algorithm which can use webpage metrics from a given online
shopping website to predict whether the revenue of a new customer is
True (i.e., the customer purchased something) or False (i.e., the
customer did not purchase anything). Our final classifier performed well
on an unseen test data set, with the f1 score of more than \(0.6\) and
the test accuray of \~\(90\)%. The precision and recall of our
classifier on the test set are also around \(0.6\).However, because of
the small target frequency we have a high percentage of incorrect
prediction in FN, we plan to further investigate & improve our model.

The data set used in this project is of online shopping webpage metrics
created by C. Okan Sakar, S. Olcay Polat, Mete Katircioglu & Yomi
Kastro(Sakar et al. 2019). It was sourced from the UCI Machine Learning
Repository(Dua and Graff 2019) and can be found
[here](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset).
Each row in the data set represents summary behavior extracted from the
URL information , including the final action (purchase or not) and
several other measurements (e.g., Number of Distinct Product Related
pages, Time spent on Product Related pages, closeness of site visitng
time to a special day, etc.).

## Report

The final report can be found
[here](https://ttimbers.github.io/breast_cancer_predictor/doc/breast_cancer_predict_report.html).

## Usage

To replicate the analysis, clone this GitHub repository, install the
[dependencies](#dependencies) listed below, and run the following
commands at the command line/terminal from the root directory of this
project:

    # download data
    python src/fetch_data.py --localpath=data/raw
    # pre-process data 
    python src/pre_process.py --input=data/raw/raw_data.csv --out_dir=data/processed 
    # run eda report
    Rscript -e "rmarkdown::render('src/EDA.Rmd')"
    # create exploratory data analysis figure and write to file 
    Rscript src/eda.r --input_dir=data/processed --out_dir=results
    # train and test model
    python src/Modeling.py --datapath=data/processed --out_dir=results
    # render final report
    Rscript -e "rmarkdown::render('doc/milestone2_final_report.Rmd', output_format = 'html_document')"

## Dependencies

Python 3.7.3 and Python packages:

docopt==0.6.2 pandas==0.24.2 numpy==1.17.2 sklearn==0.22.1
lightgbm==2.3.2

R version 3.6.1 and R packages:

knitr==1.26 tidyverse==1.2.1 caret==6.0.84 kableExtra==1.1.0
scales==1.1.0 docopt==0.6.1 testthat==2.3.1 data.table==1.12.6

## License

The Online Shopping Intention Predictor materials here are licensed
under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5
CA). If re-using/re-mixing please provide attribution and link to this
webpage.

# References

<div id="refs" class="references">

<div id="ref-Dua">

Dua, Dheeru, and Casey Graff. 2019. “UCI Machine Learning Repository.”
University of California, Irvine, School of Information; Computer
Sciences. <http://archive.ics.uci.edu/ml>.

</div>

<div id="ref-sakar2019real">

Sakar, C Okan, S Olcay Polat, Mete Katircioglu, and Yomi Kastro. 2019.
“Real-Time Prediction of Online Shoppers’ Purchasing Intention Using
Multilayer Perceptron and Lstm Recurrent Neural Networks.” *Neural
Computing and Applications* 31 (10): 6893–6908.

</div>

</div>
