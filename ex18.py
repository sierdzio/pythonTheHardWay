#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This one is like your scripts with argv
def printTwo(*args):
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def printTwoAgain(arg1, arg2):
    print "arg1: %s, arg2: %s" % (arg1, arg2)

# Tum dum dum
def printOne(arg1):
    print "arg1: %s" % arg1

# No args
def printOne():
    print "I got nothin'."

printTwo("Tom", "Bob")
printTwoAgain("Tommy", "Bobby")
printOne("One")
printNone()
