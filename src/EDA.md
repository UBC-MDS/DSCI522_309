Exploratory Data Analysis
================

## Summary

  - Each row represent a session by a user.  
  - Each user has only 1 session in the dataset.  
  - The data is for 1-year period.  
  - \~15% sessions resulted in a
purchase.

## Description of the variables, [data source](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset)

| S No. | Variable                  | Description                                                                                                                                                                          |
| ----- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | `Administrative`          | Number of Distinct administrative pages                                                                                                                                              |
| 2     | `Informational`           | Number of Distinct Informational pages                                                                                                                                               |
| 3     | `ProductRelated`          | Number of Distinct Product Related pages                                                                                                                                             |
| 4     | `Administrative_Duration` | Time(in seconds) spent on Administrative pages                                                                                                                                       |
| 5     | `Informational_Duration`  | Time(in seconds) spent on Informational pages                                                                                                                                        |
| 6     | `ProductRelated_Duration` | Time(in seconds) spent on Product Related pages                                                                                                                                      |
| 7     | `BounceRates`             | Average bounce rate of all web-pages visited by user. For a web-page its the percentage of people who visit the website from that webpage and left without raising any other request |
| 8     | `ExitRates`               | Average exit rate of all web-pages visited by user: For a web-page its the percentage of people who exited the website from that webpage                                             |
| 9     | `PageValues`              | Average page value of all web-pages visited by user: For a web-page its the average dollar-value of that page which the user visited before completing the transaction               |
| 10    | `SpecialDay`              | The closeness of site visitng time to a special day (higher chances of a session resulting in a transaction)                                                                         |
| 11    | `OperatingSystems`        | Operating system used by the user                                                                                                                                                    |
| 12    | `Month`                   | Month of Year                                                                                                                                                                        |
| 13    | `Browser`                 | Browser used by the user                                                                                                                                                             |
| 14    | `Region`                  | Geographic region                                                                                                                                                                    |
| 15    | `TrafficType`             | Type of Channel user by the user to arrive at the website                                                                                                                            |
| 16    | `VisitorType`             | Type of the visitor                                                                                                                                                                  |
| 17    | `Weekend`                 | Weekend indicator                                                                                                                                                                    |
| 18    | `Revenue`                 | Revenue transaction indicator                                                                                                                                                        |

``` r
mydata <- suppressMessages(read_csv("../data/processed/training_for_eda.csv"))
setDT(mydata)

num_vars_1 <- c("Administrative", "Informational", "ProductRelated")
num_vars_2 <- c("Administrative_Duration", "Informational_Duration", "ProductRelated_Duration", 
                "BounceRates", "ExitRates", 
                "PageValues", "ProductRelated")
target <- "Revenue"
cat_vars <- setdiff(names(mydata), c(num_vars_1, num_vars_2, target))

x <- sapply(mydata, function(x) sum(is.na(x)))
col_na <- names(x[x>0])

if (is_empty(col_na)){
  print("There is no missing value in this data set.")
} else{
  print(paste("Variables with NA values:", col_na))
}
```

    ## [1] "There is no missing value in this data set."

``` r
plot_1 <- ggplot(mydata, aes(Administrative)) + 
  geom_histogram(binwidth = 1, color = 'white') + 
  theme_bw()
plot_2 <- ggplot(mydata, aes(Informational)) + 
  geom_histogram(binwidth = 1, color = 'white') + 
  theme_bw()
plot_3 <- mydata %>% 
  ggplot(aes(x = ProductRelated, y = stat(count) / sum(count), color=Revenue)) + 
  geom_freqpoly(binwidth = 1) + 
  scale_y_continuous(labels = scales::percent) +
  labs(
    title = "Frequency polygons of ProductRelated"
  ) + theme_bw()
options(repr.plot.width = 30, repr.plot.height = 6)
p <- plot_grid(plot_1, plot_2, nrow=1)
title <- ggdraw() + draw_label("Histograms of Administrative and Informationa", fontface='bold')
plot_grid(title, p, ncol=1, rel_heights=c(0.1, 1))
```

![](EDA_files/figure-gfm/loading%20the%20data-1.png)<!-- -->

``` r
plot_3
```

![](EDA_files/figure-gfm/loading%20the%20data-2.png)<!-- -->

> There are over 700 classes in the ProductRelated feature, it is
> possible to treat this feature as categorical or numerical feature.
> This needs to be decided during the model and feature selection step
> of this project.

## Summary of Numeric Variables

``` r
quantile_dist <- sapply(num_vars_2, FUN=function(x) {
  print(paste("Mean of", x, "is", round(mydata[, mean(get(x))], digits=3), 
              "and standard deviation is", round(mydata[, sd(get(x))], digits=3)))
  mydata[, round(quantile(get(x), probs=seq(0,1,0.05)), digits=3)]
})
```

    ## [1] "Mean of Administrative_Duration is 82.436 and standard deviation is 179.302"
    ## [1] "Mean of Informational_Duration is 34.623 and standard deviation is 141.693"
    ## [1] "Mean of ProductRelated_Duration is 1195.198 and standard deviation is 1915.06"
    ## [1] "Mean of BounceRates is 0.022 and standard deviation is 0.049"
    ## [1] "Mean of ExitRates is 0.043 and standard deviation is 0.049"
    ## [1] "Mean of PageValues is 5.997 and standard deviation is 18.64"
    ## [1] "Mean of ProductRelated is 31.82 and standard deviation is 44.681"

``` r
print(quantile_dist)
```

    ##      Administrative_Duration Informational_Duration ProductRelated_Duration
    ## 0%                     0.000                  0.000                   0.000
    ## 5%                     0.000                  0.000                   0.000
    ## 10%                    0.000                  0.000                  36.000
    ## 15%                    0.000                  0.000                  77.000
    ## 20%                    0.000                  0.000                 128.000
    ## 25%                    0.000                  0.000                 181.500
    ## 30%                    0.000                  0.000                 243.983
    ## 35%                    0.000                  0.000                 315.000
    ## 40%                    0.000                  0.000                 402.009
    ## 45%                    0.000                  0.000                 493.640
    ## 50%                    8.000                  0.000                 598.600
    ## 55%                   22.971                  0.000                 718.855
    ## 60%                   38.000                  0.000                 855.133
    ## 65%                   54.500                  0.000                1029.246
    ## 70%                   73.020                  0.000                1229.497
    ## 75%                   95.763                  0.000                1473.834
    ## 80%                  124.640                  0.000                1784.082
    ## 85%                  165.388                 25.185                2210.075
    ## 90%                  228.320                 70.000                2905.811
    ## 95%                  354.752                193.463                4322.162
    ## 100%                3398.750               2549.375               63973.522
    ##      BounceRates ExitRates PageValues ProductRelated
    ## 0%         0.000     0.000      0.000              0
    ## 5%         0.000     0.005      0.000              1
    ## 10%        0.000     0.007      0.000              3
    ## 15%        0.000     0.010      0.000              4
    ## 20%        0.000     0.012      0.000              6
    ## 25%        0.000     0.014      0.000              7
    ## 30%        0.000     0.016      0.000              9
    ## 35%        0.000     0.018      0.000             11
    ## 40%        0.000     0.020      0.000             13
    ## 45%        0.000     0.023      0.000             15
    ## 50%        0.003     0.025      0.000             18
    ## 55%        0.005     0.029      0.000             21
    ## 60%        0.007     0.032      0.000             24
    ## 65%        0.010     0.036      0.000             28
    ## 70%        0.013     0.041      0.000             32
    ## 75%        0.017     0.050      0.000             38
    ## 80%        0.023     0.058      3.454             45
    ## 85%        0.033     0.073      9.927             57
    ## 90%        0.059     0.100     19.227             74
    ## 95%        0.200     0.200     38.880            111
    ## 100%       0.200     0.200    361.764            705

## Percentage of rows for categories of categorical variables

``` r
# Percentage of rows for categories of categorical variables

sapply(c(cat_vars, target), FUN=function(x) {
  round(mydata[, table(get(x))]/nrow(mydata), digits=3)*100
})
```

    ## $SpecialDay
    ## 
    ##    0  0.2  0.4  0.6  0.8    1 
    ## 89.8  1.3  2.0  3.0  2.5  1.3 
    ## 
    ## $Month
    ## 
    ##  Aug  Dec  Feb  Jul June  Mar  May  Nov  Oct  Sep 
    ##  3.3 14.0  1.4  3.5  2.5 15.4 27.5 24.5  4.5  3.5 
    ## 
    ## $OperatingSystems
    ## 
    ##    1    2    3    4    5    6    7    8 
    ## 21.2 53.2 20.9  3.8  0.1  0.2  0.0  0.6 
    ## 
    ## $Browser
    ## 
    ##    1    2    3    4    5    6    7    8    9   10   11   12   13 
    ## 20.0 64.5  0.8  5.8  3.8  1.4  0.4  1.2  0.0  1.4  0.1  0.1  0.5 
    ## 
    ## $Region
    ## 
    ##    1    2    3    4    5    6    7    8    9 
    ## 38.8  9.0 19.4  9.6  2.7  6.7  6.3  3.3  4.1 
    ## 
    ## $TrafficType
    ## 
    ##    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16 
    ## 19.7 32.1 16.4  8.7  2.1  3.5  0.3  2.9  0.3  3.7  2.0  0.0  6.0  0.1  0.3  0.0 
    ##   17   18   19   20 
    ##  0.0  0.1  0.2  1.5 
    ## 
    ## $VisitorType
    ## 
    ##       New_Visitor             Other Returning_Visitor 
    ##              13.9               0.7              85.4 
    ## 
    ## $Weekend
    ## 
    ## FALSE  TRUE 
    ##  76.4  23.6 
    ## 
    ## $Revenue
    ## 
    ## FALSE  TRUE 
    ##  84.1  15.9

## Target vs Other Variables

``` r
mydata %>% 
  select(num_vars_2, Revenue) %>% 
  gather("num_vars", "values", -Revenue) %>% 
  ggplot(aes(y=values, x=Revenue)) +
  geom_violin(mapping = aes(fill = Revenue),  show.legend = FALSE) +
  facet_wrap(~num_vars, scales = "free", nrow = 3) +
  labs(
    title = "Distributions of the numerical variables"
  ) + 
  theme_bw()
```

![](EDA_files/figure-gfm/Target%20vs%20Other%20Variables-1.png)<!-- -->

``` r
mydata %>% 
  select(cat_vars, Revenue) %>% 
  gather("num_vars", "values", -Revenue) %>% 
  group_by(Revenue, values, num_vars) %>% 
  summarise(n = n()) %>% 
  group_by(Revenue, num_vars) %>% 
  mutate(freq = n / sum(n)) %>% 
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
```

![](EDA_files/figure-gfm/Target%20vs%20Other%20Variables-2.png)<!-- -->
