total_letters = 0

for i in range(1,1001):
	str_rep = str(i)
	if "1" in str_rep:
		total_letters += 3
	elif "2" in str_rep:
		total_letters += 3
	elif "3" in str_rep:
		total_letters += 5
	elif "4" in str_rep:
		total_letters += 4
	elif "5" in str_rep:
		total_letters += 4
	elif "6" in str_rep:
		total_letters += 3
	elif "7" in str_rep:
		total_letters += 5
	elif "8" in str_rep:
		total_letters += 5
	elif "9" in str_rep:
		total_letters += 4

	if len(str_rep) >= 3:
		total_letters += 10
print total_letters