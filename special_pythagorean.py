import math

total = 0
a = 1
b = 2
c = 0

for a in range(1,500):
		for b in range(2,500):
			a_squared = a ** 2
			b_squared = b ** 2
			c_squared = a_squared + b_squared
			c = math.sqrt(c_squared)

			total = a + b + c

			if total >= 1001:
				break
			if a < b and b < c:
				if total == 1000:
					print a
					print b
					print c
					print int(a * b * c)