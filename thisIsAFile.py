#in the open method parameters you put the name of the file and comma and then what you want it to do 
#either read "r" or write "w" or both.
file1 = open("thisIsAFile.py", "r")
file1.tell()
file1.seek(0,0)

#in the read parameters you put the number of charaters you wanna read. 
file1.read()
#in the write parameters you put what you want to write in the file.
file1.write()
