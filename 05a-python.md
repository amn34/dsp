# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

**Lists are dynamic/mutable whereas tuples are not. Therefore they do not have append, extend, remove, or pop methods. Tuples can be used as keys in dictionaries where lists cannot (assuming the tuple only has immutable elements, i.e. does not contain a list) because dictionary keys must be immutable. If a list were a key and the list was modified (thus modifying the hash value), this would create a problem in the dictionary look up.**

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

**Unlike lists, sets are unordered, must contain unique values and cannot store unhashable types (lists, sets, dictionaries). Sets support mathematical operations (union, intersection, difference). Both are mutable and support comprehensions.**

    #create list
    items = [1,1,2,3,3,3,4,4,5]
    #creates set from list, i.e. ignores duplicates
    numbers = set(items)

    #creates set that is equal to numbers
    things = {1,1,2,3,3,3,4,4,5}
    
**For testing whether an item is in an object, sets are much faster than lists because each item in a set is placed in membory using its hash. Therefore looking for an item only looks in the hash position to see if it is there. It does not matter how large the set is. Searching in a list means looking at each item, so the longer the list, the longer it will take.**

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

**`lamda` defines an anonymous function in place. This is useful for simple functions that only need to be used once. Its result is the returned value from the (single) expression that it contains.**

    #returns 4
    (lambda x: x**2)(2)
    
    #sorts list by price
    groceries = [('eggs',4),('milk',2.5),('candy',10)] 
    sorted(groceries, key=lambda item: item[1])
    
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

**List comprehension is a way to define and create new lists by applying a function to all elements of an original list.**

     #create list of squares 
     numbers = [1, 4, 8]
     squares = [n**2 for n in numbers]

     def square(n):
         return (n**2)
     numbers = (1, 4, 8)
     squares = map(square, numbers)

     #create list of evens
     numbers = [5, 8, 10, 15]
     evens = [n for n in numbers if n%2 == 0]

     evens = filter(lambda n: n%2 == 0, numbers)

**List comprehension is a complete substitute for `map` and `filter` and there is no real speed difference. Set and dictionary comprehension uses the same syntax.**

     #create set of evens
     numbers = [5, 8, 10, 15]
     {n for n in numbers if n%2 == 0}

     #create dictionary of values, squares
     dict = {n: n**2 for n in numbers}
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





