from sys import argv

script, filename = argv

print "We're going to erase %s." % filename
print "If you don't want that, hit Ctrl-C.\nIf you are ok with that, press Enter."
raw_input('?')

print "Openinng the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm goint to write these to the file."
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.close()

print "This is your file:\n%s" % open(filename, 'r').read()

print "And finally, we close it."
#target.close()

