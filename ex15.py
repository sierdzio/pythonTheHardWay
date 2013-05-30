from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %s:" % filename
print txt.read()

print "Type the filename again:"
fileAgain = raw_input('> ')

if filename == fileAgain:
  txtAgain = open(fileAgain)
  print txtAgain.read()
else:
  print "Filenames don't match: %s, %s." % (filename, fileAgain)
