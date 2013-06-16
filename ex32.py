#!/usr/bin/env python
# -*- coding: utf-8 -*-

theCount = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# a loop that goes through a list
for number in theCount:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# and now a loop through a mixed list
for i in change:
    print "I got %s" % i

# building lists
elements = range(0, 6) #[]

#for i in range(0, 6):
#    print "Adding %d to the list." % i
#    elements.append(i)

for i in elements:
    print "Element was: %d" % i
