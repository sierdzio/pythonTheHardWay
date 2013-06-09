#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, inputFile = argv

def printAll(file):
    print file.read()

def rewind(file):
    file.seek(0)

def printLine(lineCount, file):
    print lineCount, file.readline()

currentFile = open(inputFile)

print "First let's print the whole file:\n"
printAll(currentFile)

print "Now let's rewind, kind of like a tape."
rewind(currentFile)

print "Let's print three lines:"
line = 1
printLine(line, currentFile)

line = line + 1
printLine(line, currentFile)

line += 1
printLine(line, currentFile)
