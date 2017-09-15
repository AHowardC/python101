#2nd algorithm
#9009 is a two digit palidrom 
# a three digit 91019

#last 2 nums of []
# two lists of nums > 100 < 1000 range(100,1000)
# two biggest multiples to reach a 3 digit palindrom (products) 
# # largest 3 digit num 999
#algorithm 2 ^notes 
# n = 0  
# for a in range(999, 100, -1):  
#    for b in range(a, 100, -1):  
#        x = a * b  
#        if x > n:  
#            s = str(a * b)  
#            if s == s[::-1]:  
#                n = a * b  
# print(n)



#3rd algorithm 1
x = None
n = 0

while not x:
   n += 2520
   for d in xrange(11,20):
       if n % d:
           break
   else:
       x = n

print n



#3rd algorithm 2
# check_list = [11, 13, 14, 16, 17, 18, 19, 20]
# check_list = [11, 13, 14, 16, 17, 18, 19, 20]

# def find_solution(step):
#    for num in xrange(step, 999999999, step):
#        if all(num % n == 0 for n in check_list):
#            return num
#    return None

# if __name__ == '__main__':
#    solution = find_solution(2520)
#    if solution is None:
#        print "No answer found"
#    else:
#        print "found an answer:", solution