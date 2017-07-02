'''Generates Fractions'''
def fraction_generator():
    count=2
    while True:
        tount=1
        while tount<count:
            yield [tount,count]
            tount+=1
        count+=1
        
'''Checks if a number is a able to be fake canceled'''        
def is_fake_cancel(lst):
    fake=fake_cancel(lst)
    if lst == fake:
        return False
    if lst[1] == 0:
        return False
    if fake[1] == 0:
        return False
    
    if lst[0]/lst[1] == fake[0]/fake[1]:
        o=str(lst[0])
        #print(o[-1],'0')
        if o[-1] != '0':
            print(lst[0],lst[1],fake[0],fake[1])
        return True
    #print('False')
    return False
    
'''This takes a fraction and removes the fake cancel, if it cannot 
it returns the same lst.'''    
def fake_cancel(lst):
    numerator=list(str(lst[0]))
    denominator=list(str(lst[1]))
    #print(numerator,denominator)
    count =0
    while count < len(numerator):
        check =numerator[count]
        if check in denominator:
            numerator.remove(check)
            if numerator == []:
                numerator =['0']
            denominator.remove(check)
        count+=1
        
    
    newnum =''
    for i in numerator:
        newnum+=i
    Newnum = int(newnum)
    
    mewnum =''
    for i in denominator:
        mewnum+=i
    Mewnum = int(mewnum)
    
    lst=[Newnum,Mewnum]
    #print(lst)
    return lst
    
    
def main():
    for i in fraction_generator():
        if is_fake_cancel(i)==True:
            if i ==[49,98]:
                break
            
if __name__ == "__main__":
    main()
            

