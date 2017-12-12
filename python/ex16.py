from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you dont want to erase, this CTRL-C"
print "If you do want to erase, hit RETURN"

raw_input("?")

print "opening the file"
target = open(filename,'w')

print "Truncating the file, Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines"

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these to file"

para = line1 + '\n'+ line2 + '\n' + line3


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write(para)

print "And finally, we close it"
target.close()

txt = open(filename)
print txt.read()

