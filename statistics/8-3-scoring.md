[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

    def goals(lam):

        t = 0
        count = 0

        while True:
            t += np.random.exponential(1.0/lam)
            if t > 1:
                return count
            else: count += 1

        return count

    def game_sim(lam):

        rates = []
    
        for i in range(1000):
            rates.append(goals(lam))

        cdf = thinkstats2.Cdf(rates)

        print RMSE(rates, lam)
        print MeanError(rates, lam)

        thinkplot.Cdf(cdf)
        thinkplot.Show(xlabel = 'estimated lam', ylabel = 'CDF')  

| lam = 2 | lam = 5 | lam = 10
---|---*|---*|---*
std err | 1.40 | 2.24 | 3.13
mean err | 0.04 | 0.11 | 0.05
CI | (0, 4) | (2, 8) | (6, 14)

![lamcdf](/images/lamcdf.png)

Sampling error increases for increasing values of lam. Intuitively this makes sense, as the greater the space for goal-scoring, the more variability there will be. However, given a small and consistent mean error, this estimator seems unbiased.

