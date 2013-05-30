from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %s:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
fileAgain = raw_input('> ')

if filename == fileAgain:
  txtAgain = open(fileAgain)
  print txtAgain.read()
  txtAgain.close()
else:
  print "Filenames don't match: %s, %s." % (filename, fileAgain)
