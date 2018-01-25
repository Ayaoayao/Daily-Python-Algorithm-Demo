def aplusb(a, b):
    # write your code here, try to do it without arithmetic operators.
        
    if(b == 0):
        
        return a
    else:
        
        c=a^b
        
        d=(a&b)<<1
        
        return aplusb(c,d)
                

if __name__ == '__main__':
    x=aplusb(2,3)
    print(x)