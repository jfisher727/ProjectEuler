
total = 2

first = 1
second = 2
result = first + second

while result < 4000000:
	first = second
	second = result
	result = first + second
	if result % 2 == 0:
		total += result

print total