[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

    pmf = thinkstats2.Pmf(resp.NUMKDHH)

    >> 0: 0.46617820227659301 
    >> 1: 0.21405207379301322 
    >> 2: 0.19625801386889966 
    >> 3: 0.087138558157791451 
    >> 4: 0.025644380478869556 
    >> 5: 0.010728771424833181
    
    pmf.Mean()

    >> 1.024

Biased PMF:

    >> 0 = 0.466 * 0
    >> 1 = 0.214 * 1 = 0.214 / 1.02 = 0.210
    >> 2 = 0.195 * 2 = 0.390 / 1.02 = 0.382
    >> 3 = 0.087 * 3 = 0.261 / 1.02 = 0.256
    >> 4 = 0.025 * 4 = 0.100 / 1.02 = 0.098
    >> 5 = 0.011 * 5 = 0.055 / 1.02 = 0.054

    >> mean = 2.39

    bias = BiasPmf(pmf)
    bias.Mean()

    thinkplot.Pmfs([pmf, bias])
    thinkplot.Show()

![pmfs](http://github.com/amn34/images/biaspmf.png)

Self-reported observed family sizes will be biased toward a larger family mean because more family members in larger families in the sample observe larger family sizes. For each five-membered family, five respondents will observe five-membered families, while for each two-membered family, only two respondents will report a two-membered family.
