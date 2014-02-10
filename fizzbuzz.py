# Hi there, I'm Alex

# run python fizzbuzz.py [num], and this will print out for 1 to num
# fizz for every number divisible by 3,
# buzz for every number divisible by 5,
# fizzbuzz for divisible by 3 and 5

import sys

num = int(sys.argv[1])

for x in range(1,num+1):
	out = ""
	if(x%3 == 0):
		out += "fizz"
	if(x%5 == 0):
		out += "buzz"
	if(len(out) > 0):
		print "%s: %s" % (x,out)
