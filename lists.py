students1 = "Mikayla"
students2 = "jenn"
students3 = "nik"
students4 = "zach"

print students1
print students2
print students3
print students4

A list is made with []. Every element is seperated by a ,
students = [
"mikayla",
"jenn",
"nik",
"zach"
]

print students
print students[0]
print students[3]
print students[-1]

 atlanta_teams = [
 "falcons",
 "braves",
 "hawks",
 "thrashers",
 "atl utd"
 ]

 atlanta_teams.append("atl utd")
 print atlanta_teams
atlanta_teams_length = len(atlanta_teams)
 for i in range(0,atlanta_teams_length):
 		print "bad index"

 		print atlanta_teams


teams_as_a_string = "Falcons, braves, hawks, atl utd" 
teams_as_a_list = teams_as_a_string.split(', ')

atlanta_teams.sort();
print atlanta_teams

sorted will sort the list but not change the list.
it returns the sorted list 

sorted_atlanta_teams = sorted(atlanta_teams)
print atlanta_teams
print sorted_atlanta_teams

# if you want to copy a part of the list you can use [x:y]
# this will make a copy of the array. it will not change the original
# it will start at the Xth element and will stop at the yth

# to delete and index you can use the remove method.
# alternative to pop you provide the element instead of the index






















