import csv
import re

csvfile = open('faculty.csv')
reader = csv.reader(csvfile)
next(reader)
faclist = list(reader)

# Q1


def find_degrees(data):

    degrees = []
    degdict = {}

    for row in data:
        degrees.append(row[1])

    deg = (str(degrees)).upper().translate(None, '.')
    parsed = re.findall('[A-Z]+', deg)

    for item in parsed:
        if not item in degdict:
            degdict[item] = 1
        else:
            degdict[item] += 1

    return degdict


# Q2

def find_titles(data):

    titles = []
    titledict = {}

    for row in data:
        titles.append(row[2])

    for item in titles:
        if item not in titledict:
            titledict[item] = 1
        else:
            titledict[item] += 1

    return titledict


# Q3


def find_emails(data):

    emaillist = []

    for row in data:
        if row[3] not in emaillist:
            emaillist.append(row[3])

    return emaillist


# Q4

def find_domains(data):

    email = find_emails(data)

    domainlist = []

    for address in email:
        domain = re.findall('@([^ ]*)', address)
        if domain not in domainlist:
            domainlist.append(domain)

    print "There are", len(domainlist), "different email domains."
    print domainlist
