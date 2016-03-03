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
In [5]: remove_adjacent([])
Out[5]: []

In [6]: remove_adjacent([1,2,2,3])
[1]

In [7]: 
In [8]: remove_adjacent([1,2,2,3])
[1, 3]

In [9]: 
In [10]: remove_adjacent([1,2,2,3])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-10-b679b2f2c978> in <module>()
----> 1 remove_adjacent([1,2,2,3])

/home/amn34/ds/metis/prework/dsp/python/q7_lists.py in remove_adjacent(nums)
     19     for word in words:
     20         if len(word) >= 2 and word[0] == word[-1]:
---> 21             counter += 1
     22     print counter
     23 

AttributeError: 'list' object has no attribute 'appe'

In [11]: 
In [12]: remove_adjacent([3,2,3,3,3])
[3, 2, 3]

In [13]:   File "/home/amn34/ds/metis/prework/dsp/python/q7_lists.py", line 18
    counter = 0
               
^
SyntaxError: invalid syntax


In [14]: linear_merge(['aa','xx','zz'],['bb','cc'])
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-14-68aa0b23a48d> in <module>()
----> 1 linear_merge(['aa','xx','zz'],['bb','cc'])

NameError: name 'linear_merge' is not defined

In [15]:   File "/home/amn34/ds/metis/prework/dsp/python/q7_lists.py", line 25
    def front_x(words):
                       
^
SyntaxError: invalid syntax


In [16]: 
In [17]: list1=['aa','xx','zz']

In [18]: list2=['bb','cc']

In [19]: linear_merge(list1,list2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-19-6b5b83ffc23f> in <module>()
----> 1 linear_merge(list1,list2)

/home/amn34/ds/metis/prework/dsp/python/q7_lists.py in linear_merge(list1, list2)
     18     counter = 0
     19     for word in words:
---> 20         if len(word) >= 2 and word[0] == word[-1]:
     21             counter += 1
     22     print counter

TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'

In [20]: 
In [21]: linear_merge(['aa','aa'],['aa','bb','bb'])
['aa', 'aa', 'aa', 'bb', 'bb']

In [22]: 
