value = 2 ** 1000

str_value = str(value)
total = 0
for i in range(len(str_value)):
	total += int(str_value[i])

print total