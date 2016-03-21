[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

    first = live[live.birthord==1]
    others = live[live.birthord!=1]

    firstmean = first.totalwgt_lb.mean()
    othermean = others.totalwgt_lb.mean()

The mean weight of a first baby is 7.20 lbs, while the mean weight of a non-first baby is 7.33 lbs.

    thinkstats2.CohenEffectSize(others.totalwgt_lb,     
    first.totalwgt_lib)

Cohen's d for this comparison is 0.089, indicating a very small increase in baby weight for babies born after the first one. Over 96% of the distributions of the baby weights for first-born and non- overlap.

This difference is slightly larger than the difference in pregnancy length, had a Cohen's d value of 0.029, but both fall quite short of representing even a small effect size (generally set at d = 0.20).
