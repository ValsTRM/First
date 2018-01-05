my_name = 'Valaya Choudhary'
my_age = 10  # not a lie for 1/1/2018
my_height = 58 # inches (for now at 1/1/2018)
my_weight = 83 # pounds as of 1/1/2018
my_eyes = 'Dark Brown'
my_teeth = 'White'
my_hair = 'Dark Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are ussually %s." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( 
	my_age, my_height, my_weight, my_age + my_height + my_weight)
	# If I add 10, 58, and 83 I get 151.