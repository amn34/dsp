[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

    #using already saved live, first, others dataframes
    
    firstsample = thinkstats2.SampleRows(first, 100, replace = False)  otherssample = thinkstats2.SampleRows(other, 100, replace = False)
    #preg length
    data = firstsample.prglngth.values, otherssample.prglngth.values
    test = hypothesis.DiffMeansPermute(data)
    p = test.PValue(iters=1000)

    #chi-squared

    test = hypothesis.CorrelationPermute(data)
    p = test.PValue(iters=1000)

    #birth weight
    data = firstsample.totalwgt_lb.values, otherssample.totalwgt_lb.values
    test = hypothesis.DiffMeansPermute(data)
    p = test.PValue(iters=1000)

    #weight v age
    livesample = thinkstats2.SampleRows(live, 100, replace = False)
    data = livesample.total_wgtlb.values, livesample.agepreg.values
    test = hypothesis.CorrelationPermute(data)
    p = test.PValue(iters=1000)

|preg length | chi-squared | birth weight | weight v age 
---|---*|---*|---*|---*
n = 100 |0.58|0.15|0.0|0.0
n = 1000 |0.60|0.14|0.0|0.0
n = 10000 |0.60|0.14|0.0|0.0

Theoretically, p-values should fall as n increases, all else equal. Hypothesis tests become more sensitive with larger sample sizes; you should be more likely to correctly reject a false null hypothesis. Unfortunately my replication of the tests on various sample sizes yielded stable p-values. In cases where large p-values remained large, perhaps the tests are low-powered because the effect size is quite small. p = 0.0 persists from n = 100 to n = 10000, as expected.

#Just wanted to say that I found this chapter really weird. There's no discussion of CLT and good sampling practice, so instead it talks about "reshuffling" data to simulate it (in the birth weights example). Then the dice rolling example has n = 60. I don't really understand why there's no discussion of creating a normal distribution through random sampling...
