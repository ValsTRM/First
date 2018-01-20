#change something here
#It tells you to get the argv from the system library
from sys import argv
#It is unpacking what the argv is.
script, filename = argv
# It is defining the txt variable by opening the file
txt = open(filename)
#It is giving the file name
print "Here's your file %r:" % filename
# It is reading the file
print txt.read()
#it is asking you to type the file again, so it can read it to you again.
print "Type the filename again:"
file_again = raw_input("> ")
#It is opening the file that you gave as an input
txt_again = open(file_again)

print txt_again.read()