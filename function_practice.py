# a function is started with def 
def say_hello():
	print "Hello"

say_hello()

def say_hello_with_name(name);
	print "Hello, %s" % name 

say_hello_with_name("Jamie")
say_hello_with_name("Jamie")
say_hello_with_name("Jamie")
say_hello_with_name("Jamie")

students =["Jamie","saif", "Zach","Casey"]
for i in range(0,len(students)):


def say_hello_safe(name, in_class="Yes"):
	print "%s, %s is in the class" % (in_class, name) 

say_hello_safe("Jong")

#functions always return a value
# return value is a functions chance to send one and only one thing back 
# to whoever called it

def return_user_name(name):
	normalized_name =name.upper()
	return normalized_name

print return_user_name("Chris")
print return_user_name("Im a wild guy")

