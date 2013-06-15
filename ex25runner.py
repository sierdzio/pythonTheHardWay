#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ex25
sentence = "All good things come to those who wait."
words = ex25.breakWords(sentence)
print words
sortedWords = ex25.sortWords(words)
print sortedWords

ex25.printFirstWord(words)
ex25.printLastWord(words)
print words

ex25.printFirstWord(sortedWords)
ex25.printLastWord(sortedWords)
print sortedWords

sortedWords = ex25.sortSentence(sentence)
print sortedWords

ex25.printFirstAndLast(sentence)
ex25.printFirstAndLastSorted(sentence)
