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
X_train <- suppressMessages(read_csv("../data/X_train.csv"))
y_train <- suppressMessages(read_csv("../data/y_train.csv"))

mydata <- cbind(X_train, y_train)
setDT(mydata)

num_vars_1 <- c("Administrative", "Informational", "ProductRelated")
num_vars_2 <- c("Administrative_Duration", "Informational_Duration", "ProductRelated_Duration", 
                "BounceRates", "ExitRates", 
                "PageValues", "ProductRelated")
target <- "Revenue"
cat_vars <- setdiff(names(mydata), c(num_vars_1, num_vars_2, target))

x <- sapply(mydata, function(x) sum(is.na(x)))
col_na <- names(x[x>0])
print(paste("Variables with NA values:", col_na))
```

    ## [1] "Variables with NA values: "

``` r
ggplot(mydata, aes(Administrative)) + geom_histogram(binwidth = 1)
```

![](EDA_files/figure-gfm/loading%20the%20data-1.png)<!-- -->

``` r
ggplot(mydata, aes(Informational)) + geom_histogram(binwidth = 1)
```

![](EDA_files/figure-gfm/loading%20the%20data-2.png)<!-- -->

``` r
ggplot(mydata, aes(ProductRelated)) + geom_histogram(binwidth = 1)
```

![](EDA_files/figure-gfm/loading%20the%20data-3.png)<!-- -->

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

    ##      Administrative_Duration Informational_Duration
    ## 0%                     0.000                  0.000
    ## 5%                     0.000                  0.000
    ## 10%                    0.000                  0.000
    ## 15%                    0.000                  0.000
    ## 20%                    0.000                  0.000
    ## 25%                    0.000                  0.000
    ## 30%                    0.000                  0.000
    ## 35%                    0.000                  0.000
    ## 40%                    0.000                  0.000
    ## 45%                    0.000                  0.000
    ## 50%                    8.000                  0.000
    ## 55%                   22.971                  0.000
    ## 60%                   38.000                  0.000
    ## 65%                   54.500                  0.000
    ## 70%                   73.020                  0.000
    ## 75%                   95.763                  0.000
    ## 80%                  124.640                  0.000
    ## 85%                  165.388                 25.185
    ## 90%                  228.320                 70.000
    ## 95%                  354.752                193.463
    ## 100%                3398.750               2549.375
    ##      ProductRelated_Duration BounceRates ExitRates PageValues
    ## 0%                     0.000       0.000     0.000      0.000
    ## 5%                     0.000       0.000     0.005      0.000
    ## 10%                   36.000       0.000     0.007      0.000
    ## 15%                   77.000       0.000     0.010      0.000
    ## 20%                  128.000       0.000     0.012      0.000
    ## 25%                  181.500       0.000     0.014      0.000
    ## 30%                  243.983       0.000     0.016      0.000
    ## 35%                  315.000       0.000     0.018      0.000
    ## 40%                  402.009       0.000     0.020      0.000
    ## 45%                  493.640       0.000     0.023      0.000
    ## 50%                  598.600       0.003     0.025      0.000
    ## 55%                  718.855       0.005     0.029      0.000
    ## 60%                  855.133       0.007     0.032      0.000
    ## 65%                 1029.246       0.010     0.036      0.000
    ## 70%                 1229.497       0.013     0.041      0.000
    ## 75%                 1473.834       0.017     0.050      0.000
    ## 80%                 1784.082       0.023     0.058      3.454
    ## 85%                 2210.075       0.033     0.073      9.927
    ## 90%                 2905.811       0.059     0.100     19.227
    ## 95%                 4322.162       0.200     0.200     38.880
    ## 100%               63973.522       0.200     0.200    361.764
    ##      ProductRelated
    ## 0%                0
    ## 5%                1
    ## 10%               3
    ## 15%               4
    ## 20%               6
    ## 25%               7
    ## 30%               9
    ## 35%              11
    ## 40%              13
    ## 45%              15
    ## 50%              18
    ## 55%              21
    ## 60%              24
    ## 65%              28
    ## 70%              32
    ## 75%              38
    ## 80%              45
    ## 85%              57
    ## 90%              74
    ## 95%             111
    ## 100%            705

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
    ##    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15 
    ## 19.7 32.1 16.4  8.7  2.1  3.5  0.3  2.9  0.3  3.7  2.0  0.0  6.0  0.1  0.3 
    ##   16   17   18   19   20 
    ##  0.0  0.0  0.1  0.2  1.5 
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
chart1 <- ggplot(mydata, aes(Revenue, Administrative_Duration, fill=Revenue)) + geom_boxplot()
chart2 <- ggplot(mydata, aes(Revenue, Informational_Duration, fill=Revenue)) + geom_boxplot()
chart3 <- ggplot(mydata, aes(Revenue, ProductRelated_Duration, fill=Revenue)) + geom_boxplot()
chart4 <- ggplot(mydata, aes(Revenue, BounceRates, fill=Revenue)) + geom_boxplot()
chart5 <- ggplot(mydata, aes(Revenue, ExitRates, fill=Revenue)) + geom_boxplot()
chart6 <- ggplot(mydata, aes(Revenue, PageValues, fill=Revenue)) + geom_boxplot()
chart7 <- ggplot(mydata, aes(Revenue, ProductRelated, fill=Revenue)) + geom_boxplot()

plot_grid(chart1, chart2, chart3, chart4, chart5, chart6, chart7, nrow=4)
```

![](EDA_files/figure-gfm/Target%20vs%20Other%20Variables-1.png)<!-- -->

``` r
chart_a <- ggplot(mydata, aes(SpecialDay, fill=Revenue)) + geom_bar(stat = "count", position = "dodge")
chart_b <- ggplot(mydata, aes(Month, fill=Revenue)) + geom_bar(stat = "count", position = "dodge")
chart_c <- ggplot(mydata, aes(OperatingSystems, fill=Revenue)) + geom_bar(stat = "count", position = "dodge")
chart_d <- ggplot(mydata, aes(Browser, fill=Revenue)) + geom_bar(stat = "count", position = "dodge")
chart_e <- ggplot(mydata, aes(Region, fill=Revenue)) + geom_bar(stat = "count", position = "dodge")
chart_f <- ggplot(mydata, aes(TrafficType, fill=Revenue)) + geom_bar(stat = "count", position = "dodge")
chart_g <- ggplot(mydata, aes(VisitorType, fill=Revenue)) + geom_bar(stat = "count", position = "dodge")
chart_h <- ggplot(mydata, aes(Weekend, fill=Revenue)) + geom_bar(stat = "count", position = "dodge")

options(repr.plot.width = 20, repr.plot.height = 8)
plot_grid(chart_a, chart_b, chart_c, chart_d, chart_e, chart_f, chart_g, chart_h, nrow=4)
```

![](EDA_files/figure-gfm/Target%20vs%20Other%20Variables-2.png)<!-- -->
