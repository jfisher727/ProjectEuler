import math

total = 2

for i in range(3,2000000):
	sqrt_i = int(math.ceil(math.sqrt(i)))
	is_prime = True
	for x in range (2, sqrt_i):
		if i % x == 0:
			is_prime = False
	if is_prime:
		print i
		total += i
print total