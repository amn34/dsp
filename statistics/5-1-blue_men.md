[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

    heights = scipy.stats.norm(loc = 178, scale = 7.7)

Blue Men must be between 177.8 cm and 185.4 cm in height.

    heights.cdf(185.4) - heights.cdf(177.8)

    >> 0.342

34% of US males fall within the Blue Man casting height guidelines.
