#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, people, cars, buses = argv

people = int(people)
cars = int(cars)
buses = int(buses)

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide"

if buses > cars:
    print "That's too many buses"
elif buses < cars:
    print "Maybe we could take the buses"
else:
    print "We still can't decide"

if people > buses:
    print "Alright, let's just take the buses"
else:
    print "Fine, let's stay home then"
