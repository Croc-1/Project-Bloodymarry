"""
A module to convert numberber system.
"""

def bin10(number):
    #for decimal to binry conversion.
    bnry=""
    while number!=0:
        temp=number%2
        bnry+=str(temp)
        number//=2
    bnry=bnry[::-1]
    return(bnry)

def oct10(number):
    #for decimal to octal conversion.
    octl=""
    while number!=0:
        temp=number%8
        octl+= str(temp)
        number //= 8
    octl=octl[::-1]
    return(octl)

def hex10(number):
    """for decimal to hexadecimal conversion."""
    hexa=""
    alp=["A", "B", "C", "D", "E", "F"]
    while number!=0:
        temp=number%16
        if temp>9:
            rem=(16-temp)*-1
            temp=alp[rem]
        hexa+=str(temp)
        number//=16
    hexa=hexa[::-1]
    return(hexa)

def dec2(number):
    #for binary to decimal conversion.
    total=0
    count=0
    while number!=0:
        temp=number%10
        temp*=2**count
        total+=temp
        number//=10
        count+=1
    return(total)

def oct2(number):
    #for binary to octal conversion.
    octl=""
    while number!=0:
        temp=number%1000
        w_number=dec2(temp)
        octl+=str(w_number)
        number//=1000
    octl=octl[::-1]
    return(octl)

def hex2(number):
    #for binary to hexadecimal conversion.
    temp=dec2(number)
    temp=hex10(temp)
    return(temp)

def dec8(number):
    #for octal to decimal conversion.
    total=0
    count=0
    while number!=0:
        temp=number%10
        temp*=8**count
        total+=temp
        number//=10
        count+=1
    return(total)

def bin8(number):
    #for octal to binary coversion.
    temp=dec8(number)
    temp=bin10(temp)
    return(temp)

def hex8(number):
    #for octal to hexadecimal conversion.
    temp=dec8(number)
    temp=hex10(temp)
    return(temp)

def dec16(number):
    #for hexadecimal to decimal conversion.
    total=0
    count=0
    digits=list(number)
    while digits!=[]:
        temp=digits[-1]
        if temp.isdigit():
            temp=int(temp)
            temp*=16**count
            total+=temp
        else:
            temp=ord(temp)-55
            temp*=16**count
            total+=temp
        digits.pop(-1)
        count+=1
    return(total)

def bin16(number):
    #for hexadecimal to binary conversion.
    temp=dec16(number)
    temp=bin10(temp)
    return(temp)

def oct16(number):
    #for hexadecimal to octal conversion.
    temp=dec16(number)
    temp=oct10(temp)
    return(temp)
