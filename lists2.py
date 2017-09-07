someString = ("someStriNg").upper()

print("someStriNg").upper()

print(someString).capitalize()

# python reversing can only be done to lists
print(someString)[::-1]


#Leetspeak
str 
print str 

#Long-long Vowels
newWord = ""
word = "good"
vowels = ["a", "e", "i", "o", "u"]

#i = 0
#while i < len(word):
# i += 1 
for i in range(0,len(word) - 1):
	if (word[i] == word[i+1]):
		for j in vowels:
			if word[i] == j:
				newWord += word[i] * 3 
	else:
		newWord += word[i]	
newWord += word[-1]				
print newWord
