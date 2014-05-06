sum_of_squares = 0

for i in range(1,101):
	sum_of_squares += i**2

square_of_sums = 0
for i in range(1,101):
	square_of_sums += i

result_squared = square_of_sums ** 2

print result_squared - sum_of_squares