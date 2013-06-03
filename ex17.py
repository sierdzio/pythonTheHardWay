from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print "Copying from %s to %s" % (fromFile, toFile)

inFile = open(fromFile)
inData = inFile.read()

print "The input file is %d bytes long" % len(inData)
print "Does the output file exist? %r" % exists(toFile)
print "Ready, hit RETURN to continue, Ctrl-C to abort."
raw_input()

outFile = open(toFile, 'w')
outFile.write(inData)

print "Done."

inFile.close()
outFile.close()
