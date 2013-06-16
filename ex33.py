#!/usr/bin/env python
# -*- coding: utf-8 -*-

i = 0
numbers = []

while i < 6:
    print "In the beginning, i was: %d" % i
    numbers.append(i)
    i += 2
    print "Numbers now:", numbers
    print "And lo! i has become %d by the time it got to the bottom of the loop." % i

print "The numbers:"

for num in numbers:
    print num
