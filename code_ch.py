fullName = "Akil"
age = 33

myArray = []
myArray.append(fullName)
myArray.append(age)
print myArray

def say_hello():
	print "Hello!"
say_hello()

#4
splitName = fullName.split()
print splitName

#5
def sayName():
	print "Hello, %s" % splitName[0]
splitName()



#6
import datetime
now = datetime.datetime.now()
currentYear = now.yearBorn

def myAge(yearBorn):
	print (currentYear - yearBorn)
myAge()

#7
def sum_odd_numbers():
	init a var "sum" at 0 so we can increment it 
	sum = 0 
	for i in range(1,5001):
		#check to see if it is odd
		if (i % 2 == 1):
			odd number!
			sum += i 
	print sum
sum_odd_numbers()



def sum_odd_numbers2():
	sum = 0
	#range has a 3rd arg. step is the 3rd so you can run the loop by 2s instead of 1s
	for i in range(1,5001,2):
		sum += i 
	print sum

sum_odd_numbers2()

def sum_odd_numbers3()
	i = 0
	while 1:
		sum += i
		i += i 
		if (i == 5000):
			break




















