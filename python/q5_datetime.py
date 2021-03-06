# Hint:  use Google to find python function

from datetime import datetime

# a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
date_format = '%m-%d-%Y'

diff = (datetime.strptime(date_stop, date_format) -
        datetime.strptime(date_start, date_format))
print diff

# b)
date_start = '12312013'
date_stop = '05282015'
date_format = '%m%d%Y'

diff = (datetime.strptime(date_stop, date_format) -
        datetime.strptime(date_start, date_format))
print diff

# c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
date_format = '%d-%b-%Y'

diff = (datetime.strptime(date_stop, date_format) -
        datetime.strptime(date_start, date_format))
print diff
