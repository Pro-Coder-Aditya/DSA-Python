# First in Frist Out(FIFO)

queue = []

while True:
    print('''
1 Push Elements
2 Pop First Elements
3 Front Element
4 Last Element
5 Display Queue
6 Exit
''')
    choice = int(input("Enter the operation: "))
    
   
    if choice == 1:
        n = input("Enter the value: ")
        queue.append(n)
        print(queue)
    elif choice == 2:
        if len(queue) == 0:
            print("Empty Queue")
        else:
            del queue[0]
            print(queue)
    elif choice == 3:
        if len(queue) == 0:
            print("Empty Queue")
        else:
            print("First Queue Element: ", queue[0])
    elif choice == 4:
        if len(queue) == 0:
            print("Empty Queue")
        else:
            print("Last Queue Element: ", queue[-1])
    elif choice == 5:
        print("Display Queue: ", queue)
    elif choice == 6:
        break
    else:
        print("Invalid Operation")    