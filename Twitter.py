
# Difficulty Level: Beginner
# Exercise: Tweet length calculator

# Part one:
# Create a variable called tweet and put some text in it
#   maybe something like "Hear Me Code class was so much fun today!"

tweet = "Hear Me Code class was so much fun today!"

# Measure the length of that tweet.
print tweet
print len(tweet)
character_limit = 140

# Was that tweet more than 140 characters?
#   If so, tell the user it was too long!
# Was that tweet 140 or fewer characters?
#   If so, tell the user how witty they are!

if len(tweet) > character_limit:
	print "Your tweet is too long"
else:
	print "You're so witty"

# Part two:
# Adjust the program to say how many characters you have remaining to use, or how many you need to trim by in order to meet the 140 character limit

if len(tweet) > character_limit:
	print "Your tweet is too long by {0} characters. Please shorten it".format(len(tweet)-character_limit)
elif len(tweet) == character_limit:
	print "You've reached the character limit."
else: 
	print "You have {0} characters remaining".format(character_limit-len(tweet))

# Part three:
# Twitter announced they are changing their character limit to 280, but they might change it again.
# Can you make your code flexible enough so that you don't have to replace the character limit in multiple places in your code?
#by replacing the number 140 with a definition of the character limit as 140, so you can change it to whatever
