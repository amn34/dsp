Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
Type "copyright", "credits" or "license" for more information.

IPython 4.1.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: 
In [2]: 
In [3]: 
In [4]: 
In [5]: for row in data: print row
['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points']
['Arsenal', '38', '26', '9', '3', '79', '36', '87']
['Liverpool', '38', '24', '8', '6', '67', '30', '80']
['Manchester United', '38', '24', '5', '9', '87', '45', '77']
['Newcastle', '38', '21', '8', '9', '74', '52', '71']
['Leeds', '38', '18', '12', '8', '53', '37', '66']
['Chelsea', '38', '17', '13', '8', '66', '38', '64']
['West_Ham', '38', '15', '8', '15', '48', '57', '53']
['Aston_Villa', '38', '12', '14', '12', '46', '47', '50']
['Tottenham', '38', '14', '8', '16', '49', '53', '50']
['Blackburn', '38', '12', '10', '16', '55', '51', '46']
['Southampton', '38', '12', '9', '17', '46', '54', '45']
['Middlesbrough', '38', '12', '9', '17', '35', '47', '45']
['Fulham', '38', '10', '14', '14', '36', '44', '44']
['Charlton', '38', '10', '14', '14', '38', '49', '44']
['Everton', '38', '11', '10', '17', '45', '57', '43']
['Bolton', '38', '9', '13', '16', '44', '62', '40']
['Sunderland', '38', '10', '10', '18', '29', '51', '40']
['Ipswich', '38', '9', '9', '20', '41', '64', '36']
['Derby', '38', '8', '6', '24', '33', '63', '30']
['Leicester', '38', '5', '13', '20', '30', '64', '28']

In [6]: 
In [7]: 
In [8]: 
In [9]: goalsdata
Out[9]: 
[['Team',
  'Games',
  'Wins',
  'Losses',
  'Draws',
  'Goals',
  'Goals Allowed',
  'Points'],
 ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
 ['Liverpool', '38', '24', '8', '6', '67', '30', '80'],
 ['Manchester United', '38', '24', '5', '9', '87', '45', '77'],
 ['Newcastle', '38', '21', '8', '9', '74', '52', '71'],
 ['Leeds', '38', '18', '12', '8', '53', '37', '66'],
 ['Chelsea', '38', '17', '13', '8', '66', '38', '64'],
 ['West_Ham', '38', '15', '8', '15', '48', '57', '53'],
 ['Aston_Villa', '38', '12', '14', '12', '46', '47', '50'],
 ['Tottenham', '38', '14', '8', '16', '49', '53', '50'],
 ['Blackburn', '38', '12', '10', '16', '55', '51', '46'],
 ['Southampton', '38', '12', '9', '17', '46', '54', '45'],
 ['Middlesbrough', '38', '12', '9', '17', '35', '47', '45'],
 ['Fulham', '38', '10', '14', '14', '36', '44', '44'],
 ['Charlton', '38', '10', '14', '14', '38', '49', '44'],
 ['Everton', '38', '11', '10', '17', '45', '57', '43'],
 ['Bolton', '38', '9', '13', '16', '44', '62', '40'],
 ['Sunderland', '38', '10', '10', '18', '29', '51', '40'],
 ['Ipswich', '38', '9', '9', '20', '41', '64', '36'],
 ['Derby', '38', '8', '6', '24', '33', '63', '30'],
 ['Leicester', '38', '5', '13', '20', '30', '64', '28']]

In [10]: ---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-a402bf706bdb> in <module>()
----> 1 __pyfile = open('''/tmp/py27844kYb''');exec(compile(__pyfile.read(), '''/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py''', 'exec'));__pyfile.close()

/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py in <module>()
      7 # The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.
      8 
----> 9 
     10 import csv
     11 

TypeError: unsupported operand type(s) for -: 'list' and 'list'

In [11]: ---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-40f61502b353> in <module>()
----> 1 __pyfile = open('''/tmp/py27844L3t''');exec(compile(__pyfile.read(), '''/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py''', 'exec'));__pyfile.close()

/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py in <module>()
      7 # The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.
      8 
----> 9 
     10 import csv
     11 

TypeError: append() takes exactly one argument (3 given)

In [12]: ---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-b6f6c0129e89> in <module>()
----> 1 __pyfile = open('''/tmp/py278440sq''');exec(compile(__pyfile.read(), '''/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py''', 'exec'));__pyfile.close()

/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py in <module>()
      8 
      9 
---> 10 import csv
     11 
     12   def read_data(data):

TypeError: unsupported operand type(s) for -: 'str' and 'str'

In [13]: ---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-13-981941c3df29> in <module>()
----> 1 __pyfile = open('''/tmp/py27844afS''');exec(compile(__pyfile.read(), '''/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py''', 'exec'));__pyfile.close()

/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py in <module>()
      8 
      9 
---> 10 import csv
     11 
     12   def read_data(data):

ValueError: invalid literal for int() with base 10: 'Goals'

In [14]: print goalsdata
[['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'], ['Arsenal', '38', '26', '9', '3', '79', '36', '87'], ['Liverpool', '38', '24', '8', '6', '67', '30', '80'], ['Manchester United', '38', '24', '5', '9', '87', '45', '77'], ['Newcastle', '38', '21', '8', '9', '74', '52', '71'], ['Leeds', '38', '18', '12', '8', '53', '37', '66'], ['Chelsea', '38', '17', '13', '8', '66', '38', '64'], ['West_Ham', '38', '15', '8', '15', '48', '57', '53'], ['Aston_Villa', '38', '12', '14', '12', '46', '47', '50'], ['Tottenham', '38', '14', '8', '16', '49', '53', '50'], ['Blackburn', '38', '12', '10', '16', '55', '51', '46'], ['Southampton', '38', '12', '9', '17', '46', '54', '45'], ['Middlesbrough', '38', '12', '9', '17', '35', '47', '45'], ['Fulham', '38', '10', '14', '14', '36', '44', '44'], ['Charlton', '38', '10', '14', '14', '38', '49', '44'], ['Everton', '38', '11', '10', '17', '45', '57', '43'], ['Bolton', '38', '9', '13', '16', '44', '62', '40'], ['Sunderland', '38', '10', '10', '18', '29', '51', '40'], ['Ipswich', '38', '9', '9', '20', '41', '64', '36'], ['Derby', '38', '8', '6', '24', '33', '63', '30'], ['Leicester', '38', '5', '13', '20', '30', '64', '28']]

In [15]: 
In [16]: goals
Out[16]: <csv.DictReader instance at 0x7f61300395a8>

In [17]: for row in goals: print row
{'Draws': '3', 'Wins': '26', 'Losses': '9', 'Goals Allowed': '36', 'Points': '87', 'Games': '38', 'Goals': '79', 'Team': 'Arsenal'}
{'Draws': '6', 'Wins': '24', 'Losses': '8', 'Goals Allowed': '30', 'Points': '80', 'Games': '38', 'Goals': '67', 'Team': 'Liverpool'}
{'Draws': '9', 'Wins': '24', 'Losses': '5', 'Goals Allowed': '45', 'Points': '77', 'Games': '38', 'Goals': '87', 'Team': 'Manchester United'}
{'Draws': '9', 'Wins': '21', 'Losses': '8', 'Goals Allowed': '52', 'Points': '71', 'Games': '38', 'Goals': '74', 'Team': 'Newcastle'}
{'Draws': '8', 'Wins': '18', 'Losses': '12', 'Goals Allowed': '37', 'Points': '66', 'Games': '38', 'Goals': '53', 'Team': 'Leeds'}
{'Draws': '8', 'Wins': '17', 'Losses': '13', 'Goals Allowed': '38', 'Points': '64', 'Games': '38', 'Goals': '66', 'Team': 'Chelsea'}
{'Draws': '15', 'Wins': '15', 'Losses': '8', 'Goals Allowed': '57', 'Points': '53', 'Games': '38', 'Goals': '48', 'Team': 'West_Ham'}
{'Draws': '12', 'Wins': '12', 'Losses': '14', 'Goals Allowed': '47', 'Points': '50', 'Games': '38', 'Goals': '46', 'Team': 'Aston_Villa'}
{'Draws': '16', 'Wins': '14', 'Losses': '8', 'Goals Allowed': '53', 'Points': '50', 'Games': '38', 'Goals': '49', 'Team': 'Tottenham'}
{'Draws': '16', 'Wins': '12', 'Losses': '10', 'Goals Allowed': '51', 'Points': '46', 'Games': '38', 'Goals': '55', 'Team': 'Blackburn'}
{'Draws': '17', 'Wins': '12', 'Losses': '9', 'Goals Allowed': '54', 'Points': '45', 'Games': '38', 'Goals': '46', 'Team': 'Southampton'}
{'Draws': '17', 'Wins': '12', 'Losses': '9', 'Goals Allowed': '47', 'Points': '45', 'Games': '38', 'Goals': '35', 'Team': 'Middlesbrough'}
{'Draws': '14', 'Wins': '10', 'Losses': '14', 'Goals Allowed': '44', 'Points': '44', 'Games': '38', 'Goals': '36', 'Team': 'Fulham'}
{'Draws': '14', 'Wins': '10', 'Losses': '14', 'Goals Allowed': '49', 'Points': '44', 'Games': '38', 'Goals': '38', 'Team': 'Charlton'}
{'Draws': '17', 'Wins': '11', 'Losses': '10', 'Goals Allowed': '57', 'Points': '43', 'Games': '38', 'Goals': '45', 'Team': 'Everton'}
{'Draws': '16', 'Wins': '9', 'Losses': '13', 'Goals Allowed': '62', 'Points': '40', 'Games': '38', 'Goals': '44', 'Team': 'Bolton'}
{'Draws': '18', 'Wins': '10', 'Losses': '10', 'Goals Allowed': '51', 'Points': '40', 'Games': '38', 'Goals': '29', 'Team': 'Sunderland'}
{'Draws': '20', 'Wins': '9', 'Losses': '9', 'Goals Allowed': '64', 'Points': '36', 'Games': '38', 'Goals': '41', 'Team': 'Ipswich'}
{'Draws': '24', 'Wins': '8', 'Losses': '6', 'Goals Allowed': '63', 'Points': '30', 'Games': '38', 'Goals': '33', 'Team': 'Derby'}
{'Draws': '20', 'Wins': '5', 'Losses': '13', 'Goals Allowed': '64', 'Points': '28', 'Games': '38', 'Goals': '30', 'Team': 'Leicester'}

In [18]: for row in goals: print row[5]

In [19]: for row in goals: print row['Goals Allowed']

In [20]: for row in goals: print row

In [21]: ('Arsenal', '36')
('Liverpool', '30')
('Manchester United', '45')
('Newcastle', '52')
('Leeds', '37')
('Chelsea', '38')
('West_Ham', '57')
('Aston_Villa', '47')
('Tottenham', '53')
('Blackburn', '51')
('Southampton', '54')
('Middlesbrough', '47')
('Fulham', '44')
('Charlton', '49')
('Everton', '57')
('Bolton', '62')
('Sunderland', '51')
('Ipswich', '64')
('Derby', '63')
('Leicester', '64')

In [22]: type(row['Goals Allowed'])
Out[22]: str

In [23]: 36
30
45
52
37
38
57
47
53
51
54
47
44
49
57
62
51
64
63
64

In [24]:   File "/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py", line 7
    # The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.
                                                                 ^
SyntaxError: invalid syntax


In [25]: 43
37
42
22
16
28
9
1
4
4
8
12
8
11
12
18
22
23
30
34

In [26]: 43
37
42
22
16
28
9
1
4
4
8
12
8
11
12
18
22
23
30
34

In [27]: Aston_Villa 1

In [28]: Team Aston_Villa had the smallest difference with 34 goals against them.

In [29]: Team Aston_Villa had the smallest difference with 34 more goals  them.

In [30]: print diff
34

In [31]: Team Aston_Villa had the smallest difference with 1 more goals  them.

In [32]:   File "/home/amn34/ds/metis/prework/dsp/python/q8_parsing.py", line 13
    # COMPLETE THIS FUNCTION
        ^
IndentationError: unexpected indent


In [33]: 
In [34]: Team Aston_Villa had the smallest difference with 1 more goals against them.

In [35]: Team Aston_Villa had the smallest difference in goals with 1 more against them.

In [36]: 
