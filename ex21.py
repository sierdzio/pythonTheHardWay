#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with those functions!"

age = add(20, 5)
height = subtract(180, 3)
weight = multiply(7, 10)
iq = divide(200, 2)

print "Age: %d, height: %d, weight: %d, IQ: %d" % (age, height, weight, iq)

# EC
print "Here is a puzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"
