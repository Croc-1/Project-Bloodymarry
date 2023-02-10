#imprting the convert module.
import convert as c


print("\t\tNUMBER SYSTEM CONVERTOR")

#asking for inputs.
try:
    number=input("Please write a number ----->")
except:
    number=eval(input("An error has occurd....\nPlease check if you missed to put(\" \")....")) ###+++++


base = int(input("Your entered data is in (write number only): \n1)Decimal\n2)Binary\n3)Octal\n4)Hexadecimal\n--->"))
bases = [1, 2, 3, 4]
while base not in bases:
    base = int(input("Please write a valid base...."))

print('\n'+'='*35)


# For decimal's conversion....
if base == 1:

    # ensuring that the input is decimal.
    org_list=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    output=[]
    while True:
        w_num = list(str(number))   ###+++++
        for i in w_num:
            flag=i in org_list
            output.append(flag)
        if False in output:
            print("Seems the number tht you entered is not Decimal or try removing(\" \")...")
            number=input("Please write a Decimal number...\n--->")
            output=[]
            w_num=number
        else:
            number=int(number)
            break

    # output
    print("BINARY \t\t===>",c.bin10(number))
    print("OCTAL \t\t===>",c.oct10(number))
    print("HEXADECIMAL\t===>",c.hex10(number))
        

'''For binary's conversion....'''
if base == 2:
    
    # ensuring that the number is binary.
    while True:
        bin_nums={'0', '1'};bin_num1={'1',};bin_num0={'0',}
        dgts=set(str(number))
        if dgts==bin_nums or dgts==bin_num1 or dgts==bin_num0:
            number=int(number)
            break
        else :
            print("Seems the number tht you entered is not binary or try removing(\" \")...")
            number=input("--->")
            
    # output
    print("DECIMAL\t\t===>",c.dec2(number))
    print("OCTAL\t\t===>",c.oct2(number))
    print("HEXADECIMAL\t===>",c.hex2(number))


'''For octal's conversion...'''
if base == 3:

    #ensuring that the input is octal.
    org_list=['0', '1', '2', '3', '4', '5', '6', '7']
    output=[]
    while True:
        w_num=list(str(number))
        for i in w_num:
            flag=i in org_list
            output.append(flag)
        if False in output:
            print("Seems the number tht you entered is not octal or try removing(\" \")...")
            number=input("--->")
            output=[]
            w_num=number
        else:
            number=int(number)
            break

    #output
    print("DECIMAL\t\t===>",c.dec8(number))
    print("BINARY\t\t===>",c.bin8(number))
    print("HEXADECIMAL\t===>",c.hex8(number))


'''For hexadecimal's conversion'''
if base == 4:

    #ensuring that the number is hexadecimal.
    number=number.upper()
    mlist=list(number)
    org_list=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    output=[]
    while True:
        w_num=list(str(number))
        for i in w_num:
            flag=i in org_list
            output.append(flag)
        if False in output:
            print("Seems the number tht you entered is not hexadecimal or try removing(\" \")...")
            number=input("--->")
            output=[]
            w_num=number
        else:
            break

    #output
    print("DECIMAL\t\t===>",c.dec16(number))
    print("BINARY\t\t===>",c.bin16(number))
    print("OCTAL\t\t===>",c.oct16(number))
