import itertools 
import math

def permutation_list(card):
    perms = []
    for i in range(0,card+1):
        perms.append(i)
    permslist=list(itertools.permutations(perms))
    return permslist

def isPrime(var):
    count=2
    while count<=math.sqrt(var):
        if var%count==False:
            #print(var/count)
            return False
        count=count+1
    return True

def Prime_gen():
    count =2
    while True:
        if isPrime(count)==True:
            yield count
        count+=1


def Sub_string_divisibility(tple):
    count  =0 
    PrimeG= Prime_gen()
    while count < 7:
        st=(tple[count+1]*100)+(tple[count+2]*10)+tple[count+3]
        pime=next(PrimeG)
        if st%pime !=0:
            return False
        count+=1
    return True
        

def main():       
    hold=permutation_list(9)
    list_to_sum =[]
    for i in hold:
        if Sub_string_divisibility(i)==True:
            lol =''
            for j in i:
                lol+=str(j)
            list_to_sum.append(int(lol))
    print(list_to_sum)
    print(sum(list_to_sum))
    print('hello branchnjnkjnkj')

main()

