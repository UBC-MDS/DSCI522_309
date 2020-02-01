# Driver script
# Team 309 Jan 2020
#
# This driver script completes the final report of the Online Shopping Intention P
# redictor and creates figures and .csv files needed for the final report.
# This script takes no arguments.
#
# usage: make all
#			To run all analysis
#		 make clean
#			To clean up all the intermediate and results files
#		 make clean_part
#			To clean up files that do not affect the modeling procedure
#			since train the model takes a while

# run all analysis and generate the final report
all: doc/final_report.html

# fetch the data
data/raw/raw_data.csv : src/fetch_data.py
	python src/fetch_data.py --localpath=data/raw

# pre-process the data	
data/processed/training_for_eda.csv  data/processed/X_train.csv data/processed/X_test.csv data/processed/y_train.csv data/processed/y_test.csv : data/raw/raw_data.csv src/pre_process.py
	python src/pre_process.py --input=data/raw/raw_data.csv --out_dir=data/processed 

# create EDA figures, .csv files and .rds files for the final report
results/img/cat_vars_dist_plot.png results/img/corr_plot.png results/img/num_vars_dist_plot.png results/cat_vars_expo.rds results/quantile_dist.csv: data/processed/training_for_eda.csv src/eda.r
	Rscript src/eda.r --input_dir=data/processed --out_dir=results

# create modeling results and save as .csv files
results/Feature_Imp.csv results/GridSearchCV.csv results/metric_by_threshold_test.csv results/metric_by_threshold_train.csv results/ROC_test_data.csv results/ROC_train_data.csv results/Test_pred.csv results/Training_pred.csv:  data/processed/X_train.csv data/processed/X_test.csv data/processed/y_train.csv data/processed/y_test.csv src/Modeling.py
	python src/Modeling.py --datapath=data/processed --out_dir=results

# render report	
doc/final_report.html : doc/final_report.Rmd results/img/cat_vars_dist_plot.png results/img/num_vars_dist_plot.png results/Feature_Imp.csv results/GridSearchCV.csv results/metric_by_threshold_test.csv results/metric_by_threshold_train.csv results/ROC_test_data.csv results/ROC_train_data.csv results/Test_pred.csv results/Training_pred.csv doc/citations.bib
	Rscript -e "rmarkdown::render('doc/final_report.Rmd')"

# Clean up intermediate and results files
clean : 
	rm -f data/processed/*.csv
	rm -f results/*.csv
	rm -f results/*.rds
	rm -f results/img/*.png
	rm -f doc/final_report.html

clean_part :
	rm -f results/img/*.png
	rm -f doc/final_report.html