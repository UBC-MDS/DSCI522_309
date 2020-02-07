# author: Cheng Min
# date: 2020-01-30

"Creates eda plots and tables for the un-pre-processed and pre-processed training data of the online shoppers intetion data from UCI website (https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset).
Saves the plots as png files and save the tables as .csv files

Usage: src/eda.r --input_dir=<input_dir> --out_dir=<out_dir>
  
Options:
--input_dir=<input_dir>    Path to training data (filename should not be included)
--out_dir=<out_dir> Path to directory where the plots and tables should be saved
" -> doc

library(data.table, quietly = TRUE)
library(tidyverse, quietly = TRUE)
library(plotly, quietly = TRUE)
library(cowplot, quietly = TRUE)
library(scales, quietly = TRUE)
library(pheatmap, quietly = TRUE)
library(testthat, quietly = TRUE)
library(docopt)

opt <- docopt(doc)

main <- function(input_dir, out_dir) {
  
  # Read the training data without pre-processing
  mydata <- suppressMessages(read_csv(paste0(input_dir, "/training_for_eda.csv")))
  setDT(mydata)
  
  # Define the numerical and categorical features
  num_vars_1 <- c("Administrative", "Informational", "ProductRelated")
  num_vars_2 <- c("Administrative_Duration", "Informational_Duration", "ProductRelated_Duration", 
                  "BounceRates", "ExitRates", 
                  "PageValues", "ProductRelated")

  num_vars_2_units <- c("sec", "sec", "sec", 
                  "percent", "percent", 
                  "dollars", "Count")
  units <- tibble(num_vars = num_vars_2, num_vars_2_units=num_vars_2_units)

  target <- "Revenue"
  cat_vars <- setdiff(names(mydata), c(num_vars_1, num_vars_2, target))
  
  # Create a table for quantile distribution and save it in a .csv file
  quantile_dist <- sapply(num_vars_2, FUN=function(x) {
    print(paste("Mean of", x, "is", round(mydata[, mean(get(x))], digits=3), 
                "and standard deviation is", round(mydata[, sd(get(x))], digits=3)))
    mydata[, round(quantile(get(x), probs=seq(0,1,0.05)), digits=3)]
  })
  
  quantile_dist <- as_tibble(quantile_dist)
  
  quantile_dist$probs <-  seq(0,1,0.05)
  
  quantile_dist <- quantile_dist %>% 
    select(probs, num_vars_2)
  write_csv(quantile_dist, paste0(out_dir, "/quantile_dist.csv"))
  
  # Save percentage of rows for categories of categorical variables in a .rds file
  cat_vars_expo <- sapply(c(cat_vars, target), FUN=function(x) {
    round(mydata[, table(get(x))]/nrow(mydata), digits=3)*100
  })
  
  saveRDS(cat_vars_expo, paste0(out_dir, "/cat_vars_expo.rds"))
  
  # Save the distribution plot for numerical variables
  temp <- mydata %>% 
    select(num_vars_2, Revenue) %>% 
    gather("num_vars", "values", -Revenue) %>% 
    mutate(values = values+0.001) 

  temp <- left_join(temp, units)  
  temp <- temp %>% mutate(num_vars = paste(num_vars, num_vars_2_units, sep=", "))

  num_vars_dist_plot <- temp %>%
    ggplot(aes(y=values, x=Revenue)) +
    geom_violin(mapping = aes(fill = Revenue),  show.legend = FALSE) +
    scale_y_log10(labels = scales::comma) + 
    facet_wrap(~num_vars, scales = "free", nrow = 3) +
    labs(
      title = "Distributions of the numerical variables",
      x = "",
      y = "Log Scaled Value"
    ) + 
    theme_bw()
  
  ggsave(paste0(out_dir, "/img/num_vars_dist_plot.png"), num_vars_dist_plot)
  
  # Save the distribution plot for categorical variables
  my_level <- c(seq(0,0.8,0.2),seq(1,20),c("Feb", "Mar", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Returning_Visitor", "New_Visitor", "Other", "FALSE", "TRUE"))
  
  cat_vars_dist_plot <- mydata %>% 
    select(cat_vars, Revenue) %>%
    gather("num_vars", "values", -Revenue) %>% 
    group_by(Revenue, values, num_vars) %>% 
    summarise(n = n()) %>% 
    group_by(Revenue, num_vars) %>% 
    mutate(freq = n / sum(n),
           values = factor(values, levels = my_level)) %>% 
    ggplot(aes(x=values, y=freq, fill=Revenue)) +
    geom_col(position = "dodge")+
    scale_y_continuous(labels = scales::percent) +
    facet_wrap(~num_vars, scales  ="free", nrow = 4) +
    labs(
      title = "Distributions of the categorical variables",
      x = "Categorical variables",
      y = "Frequency"
    ) + 
    theme_bw()
  
  ggsave(paste0(out_dir, "/img/cat_vars_dist_plot.png"), cat_vars_dist_plot, width = 22, height = 15, units = "cm")
  
  # Plot the correlation after pre-process and save the plot
  X_train <- read_csv(paste0(input_dir, "/X_train.csv"))
  y_train <- read_csv(paste0(input_dir, "/y_train.csv"))
  
  training <- cbind(X_train, y_train)

  corr_mat <- training %>% 
    select(num_vars_1, num_vars_2, Revenue) %>% 
    cor()

  corr_mat[lower.tri(corr_mat)] <- NA

  melt_corr_mat <- melt(corr_mat, na.rm=TRUE)
  melt_corr_mat <- melt_corr_mat %>% filter(Var1!=Var2)

  corr_plot <- melt_corr_mat %>%
    ggplot(aes(Var2, Var1, fill = value))+
    geom_tile(color = "white")+
    scale_fill_gradient(low = "#56B1F7", high = "#132B43", name="Pearson\nCorrelation") +
    labs(x="", y="")+
    ggtitle("Correlation between target and numerical variables")+
    theme_minimal()+ 
    theme(axis.text.x = element_text(angle = 45, vjust = 1, size = 12, hjust = 1), axis.text.y = element_text(size = 12))+
    coord_fixed()

  ggsave(paste0(out_dir, "/img/corr_plot.png"), corr_plot)
}

test_inputs <- function(input, output){
  test_that("The path to training data is wrong!", {
    expect_true(dir.exists(input))
  })
  
  test_that("The path to store the results is wrong!", {
    expect_true(dir.exists(output))
  })
  
  test_that("The file needed does not exist! You may need to run fetch_data.py and pre_process.py first.", {
    expect_true(file.exists(paste0(input, "/training_for_eda.csv")))
  })
}

test_inputs(opt[["--input_dir"]], opt[["--out_dir"]])

main(opt[["--input_dir"]], opt[["--out_dir"]])