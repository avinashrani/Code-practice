from sys import argv

script, user_name = argv

prompt = '>'

print "Hi %s, I'm the %s script" %(user_name, script)
print "I'd like to ask you a few questions"
print "Do you like me %s ?" %user_name
likes = raw_input(prompt)

print "where do you live %s" %user_name
live = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Allright, So you said %r about liking me,
You live in %s, not sure where that is,
You have a %s. Nice
""" %(likes, live, computer)

