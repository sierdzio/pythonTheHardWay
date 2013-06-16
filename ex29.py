#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, people, cats, dogs = argv

#people = 20
#cats = 30
#dogs = 15

people = int(people)
cats = int(cats)
dogs = int(dogs)

if people < cats:
    print "Too many cats!"

if people > cats:
    print "Not too many cats."

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is try."

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People equal to dogs."
