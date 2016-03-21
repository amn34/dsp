[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

    rand = [random.random() for i in range(1000)]
    pmf = thinkstats2.Pmf(rand)
    thinkplot.Pmf(pmf)
    thinkplot.Show()

![randompmf](http://github.com/amn34/dsp/blob/master/img/randompmf.png

    cdf = thinkstats2.Cdf(rand)
    thinkplot.Cdf(cdf)

![randomcdf](http://github.com/amn34/dsp/blob/master/img/randomcdf.png


The PMF and CDF show that the distribution of this set of numbers created with random.random() is uniform. Each number between 0 and 1 has the same 0.01 chance of being selected, as shown by the PMF, and the straight-line CDF shows that percentiles line up with the percent of data that falls below them (e.g. 50% of the data falls below the 50th percentile).
