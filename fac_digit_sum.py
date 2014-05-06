factorial = 1
for i in range(1,101):
	factorial = i * factorial

fac = str(factorial)
total = 0
for x in range(0,len(fac)):
        total += int(fac[x])

print (total)
