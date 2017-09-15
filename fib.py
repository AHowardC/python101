fib = [1,2]
sum = 2 
for i in range(2,400000):
	x = fib[i -1] + fib[i - 2]
	fib.insert(i,x)
	if (x > 4000000):
		break
	if (x % 2 == 0):
		sum += x
print sum 



sumNum = 0
a,b = 0,1
while b < 4000000:
	a,b = b,a+b
	if(b % 2 == 0):
		sumNum += b
print sumNum

#the Prim challenge
knownPrime = [2,3]
def is_prime(n):
	totalPrimes = len(knownPrime)
	for i in range(0,totalPrimes):
		if(n % knownPrime[i] == 0):
			return False
		else:
			continue
	knownPrime.append(n)
	return True 
print is_prime(24)







