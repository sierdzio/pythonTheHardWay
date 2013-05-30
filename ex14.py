from sys import argv

script, userName = argv
prompt = "> "

print "Hi %s, I'm the %s script." % (userName, script)
print "I'd like to ask you a few questions.\nDo you like me %s?" % userName
likes = raw_input(prompt)

print "Where do you live, %s?" % userName
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer)
