#!/usr/bin/env python
# -*- coding: utf-8 -*-

def checkExpression(condition, expectedResult, index):
    expectedText = ""
    if (expectedResult == condition):
        expectedText = "expected"
    else:
        expectedText = "unexpected - wrong answer!"
    print index, "Result:", condition, expectedText #"expected:", expectedResult
    return (index + 1)

index = 1

index = checkExpression((True and True), 1, index)
index = checkExpression((False and True), 0, index)
index = checkExpression((1 == 1 and 2 == 1), 0, index)
index = checkExpression(("test" == "test"), 1, index)
index = checkExpression((1 == 1 or 2 != 1), 1, index)
index = checkExpression((True and 1 == 1), 1, index)
index = checkExpression((False and 0 != 0), 0, index)
index = checkExpression((True and 1 == 1), 1, index)
index = checkExpression(("test" == "testing"), 0, index)
index = checkExpression((1 != 0 and 2 == 1), 0, index)
index = checkExpression("test" != "testing", 1, index)
index = checkExpression("test" == 1, 0, index)
index = checkExpression(not (True and False), 1, index)
index = checkExpression(not (1 == 1 and 0 != 1), 0, index)
index = checkExpression(not (10 == 1 or 1000 == 1000), 0, index)
index = checkExpression(not (1 != 10 or 3 == 4), 0, index)
index = checkExpression(not ("testing" == "testing" and "Zed" == "Cool Guy"), 1, index)
index = checkExpression(1 == 1 and not ("testing" == 1 or 1 == 0), 1, index)
index = checkExpression("chunky" == "bacon" and not (3 == 4 or 3 == 3), 0, index)
index = checkExpression(3 == 3 and not ("testing" == "testing" or "Python" == "Fun"), 0, index)
