[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)


    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome==1]
    live = live.dropna(subset = ['agepreg', 'totalwgt_lb'])
    sample = thinkstats2.SampleRows(live, 5000)
    age, weight = sample.agepreg, sample.totalwgt_lb

    thinkplot.Scatter(age, weight)
    thinkplot.Show(xlabel = 'mother age in years', ylabel = 'birth weight in lbs')

![ageweightscatter](/img/ageweightscatter.png)


    bins = np.arange(15, 50, 3)
    indices = np.digitize(sample.agepreg, bins)
    groups = sample.groupby(indices)

    ages = [group.age.mean() for i, group in groups]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        thinkplot.Plot(ages, weights)

![ageweightpercentiles](/img/ageweightpercentile.png)

    thinkstats2.Corr(age, weight)
    thinkstats2.SpearmanCorr(age, weight)

The Pearson correlation coefficient is 0.061, while the Spearman correlation is 0.089. Both of these suggest that the overall relationship between mother's age at pregnance and birthweight is very weak, though positive, assuming a linear model is correct. Since Spearman is larger than Pearson, it could be that the relationship is nonlinear or that there are low-end outliers affecting the Pearson correlation.

From the percentile birth weight/age plot, it does in fact seem that the relationship is nonlinear, given the sharp drop-off in birthweights for mothers over the age of 40.
