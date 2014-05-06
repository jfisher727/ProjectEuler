i = 1
counter = 0

while True:
	for x in range(1,21):
		if i % x != 0:
			counter = 0
			break
		else:
			counter += 1
	if counter == 20:
		break
	else:
		i+= 1

print i