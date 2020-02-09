
# Online Shopping Intention Predictor

  - author: Lesley Miller, Cheng Min, Shivam Verma

## About

Here we attempt to build a classification model using the light gradient
boosting algorithm which can use webpage metrics from a given online
shopping website to predict whether the final action of a new customer
is purchasing (i.e., Revenue is TRUE) or not (i.e., Revenue is FALSE).
Our final classifier performed well on an unseen test data set, with the
F1 score of 0.646 and the test accuray calculated to be 90.9%. The
precision and recall of our classifier on the test set are 0.699 and 0.6
respectively. Due to substantially high number of false positives &
negatives, we recommend further iteration to improve this model.

The data set used in this project is of online shopping webpage metrics
created by C. Okan Sakar, S. Olcay Polat, Mete Katircioglu & Yomi
Kastro(Sakar et al. 2019). It was sourced from the UCI Machine Learning
Repository(Dua and Graff 2019) and can be found
[here](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset).
Each row in the data set represents summary behavior extracted from the
URL information ,including the final action (purchase or not) and
several other measurements (e.g., Number of Distinct Product Related
pages, Time spent on Product Related pages, closeness of site visitng
time to a special day, etc.).

## Report

The final report can be found
[here](https://ubc-mds.github.io/DSCI522_309/doc/final_report.html).

### Diagrams

The dependency diagram below illustrates script orders and dependencies
for our Makefile and was created using `makefile2graph`, click
[here](https://ubc-mds.github.io/DSCI522_309/results/img/Makefile.png)
for the original graph:

<img src="results/img/Makefile.png" width="1200" height="500"/>

### Usage:

To replicate the analysis, there are two suggested ways to run this
analysis:

#### 1\. Using Docker

*note - the instructions in this section also depends on running this in
a unix shell (e.g., terminal or Git Bash), if you are using Windows
Command Prompt, replace `/$(pwd)` with PATH\_ON\_YOUR\_COMPUTER.*

1.  Install [Docker](https://www.docker.com/get-started)
2.  Download/clone this repository
3.  Use the command line to navigate to the root of this
    downloaded/cloned repo
4.  Type the
    following:

<!-- end list -->

    docker run --rm -v /$(pwd):"/DSCI522_309" chengmin/dsci522-group309:v1.0 bash -c "make -C /DSCI522_309 all"

5.  To reset/undo the analysis, type the
    following:

<!-- end list -->

    docker run --rm -v /$(pwd):"/DSCI522_309" chengmin/dsci522-group309:v1.0 bash -c "make -C /DSCI522_309 clean"

#### 2\. After installing all [dependencies](#dependencies) (does not depend on Docker)

1.  Clone this repo, and using the command line, navigate to the root of
    this project.
2.  To run the analysis, type the following commands:

<!-- end list -->

    make all

3.  To reset/undo the analysis, type the following commands:

<!-- end list -->

    make clean

## Dependencies

  - Python 3.7.4 and Python packages:
      - docopt==0.6.2
      - pandas==1.0.0
      - numpy==1.17.2
      - sklearn==0.22.1
      - lightgbm==2.3.0
  - R version 3.6.2 and R packages:
      - knitr==1.27
      - tidyverse==1.3.0
      - caret==6.0.85
      - kableExtra==1.1.0
      - scales==1.1.0
      - docopt==0.6.1
      - testthat==2.3.1
      - data.table==1.12.8
      - here==0.1
      - pheatmap==1.0.12
  - GNU make 4.2.1

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
