stack = []
top = 0

ask_size = int(input("Enter the size of the stack "))
print(f"The size of the stack is {ask_size}")

while True:
    
    print("\n1.Push\n2.Pop\n3.Display\n4.Exit")
    # asking the user for options
    ask_menu = input("Enter a options from above --> ").casefold().strip()
    
    if ask_menu in ['1', 'push']:
        if top == ask_size:
            # if the stack is full
            print("\n-- Over Flow --\n")
        else:
            # adding the data to stack
            ask_element = input("Enter data for stack ")
            stack.append(ask_element)
            top += 1
            print(ask_element, ' Added to stack \n')
            
    elif ask_menu in ['2', 'pop']:
        if stack == []:
            print("\n-- Under Flow--\n")
        else:
            removed_element = stack.pop()
            top -= 1
            print(removed_element, ' removed from stack\n')
    elif ask_menu in ['3', 'display', 'show']:
        if stack == []:
            print("The stack is empty")
            # displaying the stack is empty
        else:
            print("STACK".center(20, '-'))
            # printing a center aligned stack 
            for element in stack:
                # iterating over the 
                print(element)
            print("*****".center(20, '-'))
    elif ask_menu in ['exit', '4']:
        # exiting the program using break
        print("Exiting the program")
        break
        
    else:
        # any other option than in menu
        print("Enter a valid option ")
