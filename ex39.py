#!/usr/bin/env python
# -*- coding: utf-8 -*-

def printLine(message = None):
    msg = '-' * 10
    if message:
        msg += " " + message
    print msg

# creating mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
printLine("Cities:")
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
printLine("States:")
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using state then cities dict
printLine("State then cities")
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
printLine()
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state:
printLine()
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
printLine("Every city and state:")
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

printLine()
# safely get the value
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city
