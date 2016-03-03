#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

goals = csv.DictReader(open("football.csv"))

mindiff = None
team = None

for row in goals:

    diff = abs(int(row['Goals']) - int(row['Goals Allowed']))
    if mindiff == None or mindiff > diff:
        mindiff = diff
        team = row['Team']

    if int(row['Goals']) > int(row['Goals Allowed']):
        score = 'for'
    else: score = 'against'

print team, "had the smallest difference in goals with", mindiff, "more goal(s)", score, "them."
