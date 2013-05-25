myName = 'Tom Siekierda'
myAge = 25
myHeight = 177.5 # centimeters
myWeight = 71.5 # kilograms
myEyes = 'Blue'
myTeeth = 'Yellow'
myHair = 'Brown'

print "Let's talk about %s." % myName
print "He's %s cm tall." % myHeight
print "He's %r kg heavy." % myWeight
print "He's got %s eyes and %s hair." % (myEyes, myHair)
print "His teeth are usually %s depending on the tea." % myTeeth

# tricky alert!
print "If I add %d, %d, and %d I get %d." % (myAge, myHeight, myWeight, myAge + myHeight + myWeight)
