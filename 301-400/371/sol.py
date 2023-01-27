def getSum(a,b):
    
    # 32 bit mask in hexadecimal
    mask = 0xffffffff
    
    # works both as while loop and single value check 
    while (b & mask) > 0:
        print("b", bin(b))
        print("a", bin(a))
        print("b & mask",bin(b & mask))
        
        carry = ( a & b ) << 1
        print("carry", bin(carry))
        a = (a ^ b) 
        print("a", bin(a))
        b = carry
    
    # handles overflow
    return (a & mask) if b > 0 else a

getSum(1, -1)
getSum(-1,1)
