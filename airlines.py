# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:45:29 2015

@author: Kruthika
"""

# read the whole file at once, return a single string (including newlines)
# 'rU' mode (read universal) converts different line endings into '\n'
f = open('airlines.csv', 'rU')
data = f.read()
f.close()

# read the file into a list (each list element is one row)
with open('airlines.csv', 'rU') as f:
    data = []
    for row in f:
        data.append(row)
        print(data)

# split each string (at the commas) into a list
with open('airlines.csv', 'rU') as f:
    data = [row.split(',') for row in f]
    
# separate the header and data
header = data[0]
data = data[1:]
print(data)

# average number of incidents per year for each airline
average = [round((float(row[2]) + float(row[5])) / 30, 2) for row in data]
print(average)

# airline names without the star
unstarred_airlines = [ row[0][0:-1] if row[0][-1] == '*' else row[0] for row in data  ]

# list containing 1 if there's a star and 0 if not
starred = [ 1  if row[0][-1] == '*' else 0 for row in data ]

# creating a dictionary with key as the airline name (without the star)
#and the value is the average number of incidents
airlines_average_dict = {}
airlines_average = zip(unstarred_airlines, average)
for unstarred_airlines, average in airlines_average:
    airlines_average_dict[unstarred_airlines] = average

# Alternative approach to create dictionary    
airlines_average_dict2 = dict(airlines_average)
    


        



