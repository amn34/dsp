[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

    from numpy import mean

    estimates = []

    for i in range(1000):
        sample = np.random.exponential(1.0/2, 100)
        L = 1/mean(sample)
        estimates.append(L)

    cdf = thinkstats2.Cdf(estimates)
    stde = RMSE(estimates, 2)
    conf = cdf.Percentile(10), cdf.Percentile(90)

For m = 10, the standard error is 0.90 and the CI is (1.30, 3.88)

    thinkplot.Cdf(cdf)
    thinkplot.Show(xlabel = 'L', ylabel = 'CDF')

![samplingdist](/img/samplingdist.png)

parameter |n = 100 | n = 1000 | n = 10000
---|---:|---:|---:
std err | 0.84 | 0.07 | 0.02
CI | (1.44, 3.09) | (1.92, 2.10) | (1.97, 2.02)

    estimates = []
    stde = []
    for n in range(100, 10000, 500):
        for i in range(1000):
            sample  = np.random.exponential(1.0/2, n)
            L  = 1/mean(sample)
            estimates.append(L)
        se = RMSE(estimates, 2)
        stde.append(se)
    
    thinkplot.Bar(range(100,10000,500), stde, width = 100)
    thinkplot.Show(xlabel = 'n', ylabel = 'standard error')

![stderrn](/img/stderrn.png)
