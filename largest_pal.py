largest_pal = 0
factor1 = 0
factor2 = 0

def checkPalindrome (str_rep):
	stack = []
	queue = []
	for i in range(len(str_rep)):
		stack.append(str_rep[i])
		queue.append(str_rep[i])

	for i in range(len(stack)):
		if stack.pop() == queue.pop(0):
			continue
		else:
			return 0
	return 1


for x in range(100,1000):
	for y in range (100, 1000):
		product = x * y
		str_rep = str(product)
		if checkPalindrome(str_rep):
			factor1 = x
			factor2 = y
			if product > largest_pal:
				largest_pal = product

print largest_pal