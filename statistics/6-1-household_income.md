[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

    RawMoment(log_sample, 1)
    Median(log_sample)
    PearsonMedianSkewness(log_sample)
    Skewness(log_sample)
    thinkstats2.Cdf(log_sample)


|Log upper = 5 | Log upper = 6 | Log upper = 7 
---|---:|---:|---:
mean | 65309.00 | 74278.71 | 122467.40 
median | 51226.45 | 51226.45 | 51226.45 
skew | 1.18 | 4.95 | 11.60
Pearson | 0.81| 0.74 | 0.39
% below mean 0.60 | 0.66 |0.86

Predictably, as the sample incorporates more of the right-hand tail, the mean increases. As we would expect, the percentage of households that fall below the mean income is therefore higher. As the mean rises and moves further to the right of the median, the skew increases. However, Pearson's median statistic actually decreases with an increasing upper bound on the sample, though it remains positive, indicating a rightward skew. As the numerator of the statistic (mean - median) gets larger with a higher upper bound, it must be that the standard deviation increases even more. 
