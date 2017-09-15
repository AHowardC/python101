#is prime 
def is_prime(num):
    if num < 2:
        return False;
    else:
        for i in range(2, int(num**0.5 )+ 1):
            if (num % i == 0):
                return False;
        return True;


#nthPrime number
def nthPrime(n):
    numberofPrimes = 0; #this keeps track of the postion
    prime =1; #this keeps track of the postion’s number
    while(numberofPrimes < n):
        prime+=1;
        if(is_prime(prime)):
            numberofPrimes +=1;
    return prime
print nthPrime(6);
