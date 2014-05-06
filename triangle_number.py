import math

factors = 1
current_row = 1
previous_sum = 0

while factors < 500:
	row_sum = 0
	factors = 0

	row_sum = previous_sum + current_row

	sqrt_row = int(math.sqrt(row_sum))
	for x in range(1,sqrt_row):
		if row_sum % x == 0:
			factors += 2

	if sqrt_row ** 2 == row_sum:
		factors -= 1

	current_row+=1
	previous_sum = row_sum

print row_sum