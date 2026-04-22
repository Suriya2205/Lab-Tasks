tsk = str(input("Enter Task (Ex: Task 1): "))

# Task 1
if tsk == "Task 1":
    lst = [x for x in range(1,11)]
    print(f"The List is: {lst}")
    ask = str(input("Enter Method: "))
    if ask == "append":
        itn = int(input("Enter Number to append: "))
        lst.append(itn)
        print(f"Now the list is: {lst}")
    elif ask == "insert":
        ind = int(input("Enter the Index to insert: "))
        num = int(input("Enter Number to insert: "))
        lst.insert(ind, num)
        print(f"Now the list is: {lst}")
    elif ask == "remove":
        ele = int(input("Enter Number to remove: "))
        if ele in lst:
            lst.remove(ele)
            print(f"Now the list is: {lst}")
        else:
            print("The given element is not present in the list")  
    elif ask == "pop":
        a = lst.pop()
        print(f"The popped element is: {a}")
        print(f"Now the list is: {lst}")
    elif ask == "extend":
        lst2 = []
        itn = int(input("Enter No of elements for list2: "))
        for i in range(itn):
            a = int(input(f"Enter {i=1}th element: "))
        lst.extend(lst2)
        print(f"Now the list is: {lst}")
    else:
        print("Invalid Operation")


# Task 2
if tsk == "Task 2":
    lst = [1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6]
    num = int(input("Enter Number to count the repitation: "))
    a = lst.count(num)
    print(a)


# Task 3
if tsk == "Task 3":
    lst = [1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6]
    print(f"The List is: {lst}")
    num = int(input("Enter the number to find index: "))
    a = lst.index(num)
    print(a)


# Task 4
if tsk == "Task 4":
    lst = [x for x in range(1, 27)]
    print("Reversed List")
    print(lst.reverse())


# Task 5
if tsk == "Task 5":
    lst = [1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6]
    w = str(input("Do you ASC/DESC: "))
    if w == "ASC":
        print("Ascending Sorted list: ")
        print(lst.sort(reverse = False))
    elif w == "DESC":
        print("Desending Sorted List: ")
        print(lst.sort(reverse = True))


# Task 6
if tsk == "Task 6":
    lst = [1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6]
    list.clear()
    print(f"List Cleared: {lst}")


# Task 7
if tsk == "Task 7":
    lst = [1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6]
    lst2 = lst.copy()
    print(f"copied list: {lst2}")


# Task 8
if tsk == "Task 8":
    tup = [x for x in range(7)]
    w = str(input("Enter Operation: "))
    if w == "len":
        a = len(tup)
        print(a)
    elif w == "max":
        a = max(tup)
        print(a)
    elif w == "min":
        a = min(tup)
        print(a)


# Task 9
if tsk == "Task 9":
    tup = (1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6)
    print(tup)
    num = int(input("Enter the Number to count: "))
    a = tup.count(num)
    print(a)


# Task 10
if tsk == "Task 10":
    tup = (1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6)
    num = int(input("Enter the Number to find its index: "))
    a = tup.index(num)
    print(a)


# Task 11
if tsk == "Task 11":
    tup = (1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6)
    lst = list(tup)
    ent = int(input("Enter How many elements you wanna add: "))
    for i in range(ent):
        ele = int(input(f"Enter {i+1}th Number: "))
        lst.append(ele)
    tup = tuple(lst)
    print(f"The Tuple is: {tup}")


# Task 12
if tsk == "Task 12":
    tup1 = (1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6)
    tup2 = (12,5,1,2,3,51,5,2,2,1,2,2,,1,79,6)
    print(f"Concatenated Tuple is {tup1+tup2}")


# Task 13
if tsk == "Task 13":
    tup = (x for x in range(1,10))
    print(tup[2:5+1])


# Task 14
if tsk == "Task 14":
    tup = (1,2,5,5,41,2,1,12,3,5,8,1,2,5,1,12,2,6)
    ele = int(input("Enter Element: "))
    if ele in tup:
        print("Element Exists")
    else:
        print("Element Doesn't Exists")

