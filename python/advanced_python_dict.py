import csv
import pprint
import string

input_file = csv.reader(open('faculty.csv'))
faclist = list(input_file)

faculty_dict = {}
lastnames = []
firstnames = []

# Q6

for i in range(len(faclist)):
    faclist[i][2] = string.replace(faclist[i][2], ' of Biostatistics', '')

for line in faclist[1:]:
    lastnames.append(line[0].split(' ')[-1])
    firstnames.append(line[0].split(' ')[0])

for i in range(len(lastnames)):
    if lastnames[i] in faculty_dict:
        faculty_dict[lastnames[i]].append(faclist[i + 1][1:4])
    else:
        faculty_dict[lastnames[i]] = [faclist[i + 1][1:4]]

# pprint.pprint(faculty_dict)

# Q7

professor_dict = {}
names = zip(firstnames, lastnames)

for i in range(len(names)):
    professor_dict[names[i]] = faclist[i + 1][1:4]

# pprint.pprint(professor_dict)

# Q8

sorted(professor_dict.items, key=lambda x: x[0][1])
