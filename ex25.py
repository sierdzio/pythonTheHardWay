#!/usr/bin/env python
# -*- coding: utf-8 -*-

def breakWords(stuff):
    """This function will break up words for us."""
    return stuff.split(' ')

def sortWords(words):
    """Sorts the words."""
    return sorted(words)

def printFirstWord(words):
    """Prints the first word after popping it off."""
    print words.pop(0)

def printLastWord(words):
    """Prints the lat word after popping it off."""
    print words.pop(-1)

def sortSentence(sentence):
    """Takes in a full sentence and returns sorted words."""
    return sortWords(breakWords(sentence))

def printFirstAndLast(sentence):
    """Prints first and last words of the sentence."""
    words = breakWords(sentence)
    printFirstWord(words)
    printLastWord(words)

def printFirstAndLastSorted(sentence):
    """Sorts the words and then prints the first and last one."""
    words = sortSentence(sentence)
    printFirstWord(words)
    printLastWord(words)
