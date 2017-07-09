'''
Solution for Project Euler problem 50. 

Problem Statement: Which prime "P" can be written as the sum of the 
most consecutive primes, where "P" is less then 1000000.

Solution:There are two steps, the first one is to find the consective sums
of prime numbers less then one million that start at 2 and the second step is 
to check if the difference of the consective sums of prime numbers is itself
prime. This is done in the functions lstofsums() and filtersum()  
        
Things to work on: My variables names are terrible. Need to really work on
that.
'''
import time

def timing_function(function):
    '''
    Outputs the time a function takes to run.
    Only works for functions without arguments.
    Must also Print the decorated function
    '''
    def wrapper_timer():
        t1 = time.time()
        function()
        t2 = time.time()
        return "Time: " + str((t2-t1)) + "\n"
    return wrapper_timer

def prime_seive(number):
    ''' 
    This is the Sieve of Eratosthenes. The parameter 'number' is the upper
    bound for the seive. Returns list of primes.
    '''
    seive=[True]*number
    seive[0]=seive[1]=False

    for (i,is_prime) in enumerate(seive):
        if is_prime == True:
            for n in range(i*i,number,i):
                seive[n]=False
    Primes = [i for i,is_prime in enumerate(seive) if is_prime == True]
    return Primes

constant = 1000000  
seive = prime_seive(constant)


def is_prime(check):
    '''
    Checks if the input is a prime.  
    '''
    for i in seive:
        if check == i:
            return True
        if i>check:
            return False
    return False
    


def lstofsums():
    '''
    Creates a list of sums of consective primes. For example, n-th position
    of the list is the sum of the first n-1 primes. The n+1-th is sum of 
    the first n-1 primes plus the n-th prime. 
    '''
    sumofprimes=[0]
    for i in seive:
        sumofprimes.append(i+sumofprimes[-1])
        if sumofprimes[-1]>=constant:
            break
    #print(sumofprimes)
    return sumofprimes
    


def filtersum(sumof):
    '''
    There are two loops: The outer loop starts at the end of list created by
    lstofsums(), we will call these elements LastS and the inner loop that 
    starts at the beginning of list created by lstofsums(), we will call these 
    elements FirstS. It then checks if NewConsecutive=(LastS-FirstS) is prime 
    and if length is greater then current greatest length. If true then this 
    is current sum of most consective primes that is prime.
    '''
    count = len(sumof)-1
    greatestlength=0
    hold = ()
    for prime in reversed(sumof):
        for j,prime2 in enumerate(sumof):
            if count-j > greatestlength and is_prime(prime-prime2)==True:
                    greatestlength = count - j
                    hold = (prime-prime2,count-j)
                    break
        count-=1
    print(hold)        
                
@timing_function
def main():
    ok=lstofsums()
    filtersum(ok)


    
if __name__ == "__main__":
    print(main())

    
                    
