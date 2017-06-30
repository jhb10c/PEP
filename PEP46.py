'''Solution for Problem 46 on Project Euler. The outline of the proof is thus:
    1. Find the odd composite numbers.
    2. Check if the odd composite number can be written as the sum of a prime
       and two times a square.
    3. Return First Composite number that does not have this Property

'''

import math

'''Checks If a number is Prime'''
def isPrime(var):
    if var == 1:
        return False
    count=2
    while count<=math.sqrt(var):
        if var%count==False:
            #print(var/count)
            return False
        count=count+1
    return True

'''Generator for Prime Numbers'''
def Prime_gen():
    count =2
    while True:
        if isPrime(count)==True:
            yield count
        count+=1
'''Generator for Composite Odd Numbers.'''
def gen_odd():
    i = 1 
    while True:
        if isPrime(i)==False:
            yield i
        i+=2
        
'''Checks if a odd composite number has listed property'''
def is_sum_pats(composite):
    for i in Prime_gen():
        if i > composite:
            break
        if composite-i > 0:
            #print(composite-i,'=',composite,'-',i)
            if (composite-i)%2==0:
                okay =int((composite-i)/2)
                #print('divide by 2',okay)
                if math.sqrt(okay).is_integer()==True:
                    #print(math.sqrt(okay))
                    return True
    return False

'''Disproves Goldbach's other conjecture!'''
def Golds_o_conjecture():
    for i in gen_odd():
        if i ==1 :
            continue
        if is_sum_pats(i)==False:
            print(i)
            return i
        
Golds_o_conjecture()
        

            
                
                
        

        