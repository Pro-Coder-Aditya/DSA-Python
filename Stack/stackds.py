# Last in First Out(LIFO)

stack = []

while True:
    print('''
1 Push Elements
2 Pop Elements
3 Peek Element
4 Display Stack
5 Exit
''')
    choice = int(input("Enter the operation: "))
    
   
    if choice == 1:
        n = input("Enter the value: ")
        stack.append(n)
        print(stack)
    elif choice == 2:
        if len(stack) == 0:
            print("Empty Stack")
        else:
            p = stack.pop()
            print(p)
            print(stack)
    elif choice == 3:
        if len(stack) == 0:
            print("Empty Stack")
        else:
            print("Last Stack value: ", stack[-1])
    elif choice == 4:
        print("Display Stack: ", stack)
    elif choice == 5:
        break
    else:
        print("Invalid Operation")    