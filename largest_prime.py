import math

largest_factor = 1

starting_number = 600851475143

while starting_number % 2 == 0:
	starting_number = starting_number / 2
	largest_factor = 2


square_root = math.floor(math.sqrt(starting_number))
square_root = int(square_root)
for i in range (3, square_root+1):
	while starting_number % i == 0:
		starting_number = starting_number / i
		largest_factor = i

print largest_factor