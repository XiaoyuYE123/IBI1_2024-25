# What does this piece of code do?
# Answer: simulates a random number which falls in the range 1-6 matching process and counts the number of iterations until two randomly drawn numbers match

# Import libraries
# This program rolls two random dice (numbers from 1 to 6)
# until both dice show the same number (a double).
# It then prints how many attempts it took
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress>=0:
	# randint(1, 6) returns a random integer between 1 and 6 (inclusive), simulating a dice roll
	progress+=1
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n:
		print(progress)
		break

