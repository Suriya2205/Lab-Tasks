tsk = input("Enter Task {Task 1}: ")

# Task 1
if tsk == "Task 1":
    a = int(input("Enter #1: "))
    b = int(input("Enter #2: "))
    c = int(input("Enter #3: "))
    res = lambda e: max(e)
    print(res([a,b,c]))


# Task 2
if tsk == "Task 2":
    a = int(input("Enter Number to Check: "))
    res = lambda e: e%2 == 0
    if res:
        print("It is Even")
    else:
        print("It is Odd")


# Task 3
if tsk == "Task 3":
    a = int(input("Enter Number to Check: "))
    res = lambda e: e%5 == 0
    if res:
        print("This is Divisible by 5")
    else:
        print("This is Not Divisible by 5")


# Task 4
if tsk == "Task 4":
    a = int(input("Enter Number: "))
    res = lambda e: print(f"''Square: {e**2}\nCube: {e**3}")
    print(res(a))


# Task 5
if tsk == "Task 5":
    a = int(input("Enter Number: "))
    string = str(a)
    res = lambda e: e[-1]
    print(res(string))


# Task 6
if tsk == "Task 6":
    a = int(input("Enter Number: "))
    res = lambda e: e >=0
    if res:
        print("It is a Positive Number")
    else:
        print("It is a Negative Number")


# Task 7
if tsk == "Task 7":
    a = int(input("Enter Mark: "))
    res = lambda e: e>= 40
    if res:
        print("Pass")
    else:
        print("Fail")


# Task 8
if tsk == "Task 8":
    a = int(input("Enter #1: "))
    b = int(input("Enter #2: "))
    c = int(input("Enter #3: "))
    res = lambda d,e,f: d*e*f
    print(res(a,b,c))


# Task 9
if tsk == "Task 9":
    a = int(input("Enter String: "))
    res = lambda e: len(e)
    print(res(a))


# Task 10
if tsk == "Task 10":
    temp = float(input("Enter Temperature in Decimal: "))
    res = lambda e: (e * 1.8) + 32
    print(res(temp))


# Task 11
if tsk == "Task 11":
    lst = [1,2,3]
    res = list(map(lambda e: e**2 , lst))
    print(res)


# Task 12
if tsk == "Task 12":
    lst = [2,4,6]
    res = list(map(lambda e: e*2, lst))
    print(res(lst))


# Task 13
if tsk == "Task 13":
    lst = [5,6,7]
    res = list(map(lambda e: e+1, lst))
    print(res(lst))


# Task 14
if tsk == "Enter 14":
    lst = [1,2,3]
    res = list(map(lambda e: str(e), lst))
    print(res)


# Task 15
if tsk == "Task 16":
    lst = [1,2,3]
    res = list(map(lambda e: e**3, lst))
    print(res)


# Task 16
if tsk == "Task 16":
    lst = ["a", "b", "c"]
    res = list(map(lambda e: e.upper(), lst))
    print(res)


# Task 17
if tsk == "Task 17":
    lst = ["hi", "hello", "bye"]
    res = list(map(lambda e: len(e), lst))
    print(res)


# Task 18
if tsk == "Task 18":
    lst1 = [1,2,3]
    lst2 = [4,5,6]
    res = list(map(lambda e,f: e+f, lst1, lst2))
    print(res)


# Task 19
if tsk == "Task 19":
    lst = [1,2,3]
    res = list(map(lambda e: e*3, lst))
    print(res)


# Task 20
if tsk == "Task 20":
    lst = [5,6,7]
    res = list(map(lambda e: e-2, lst))
    print(res)


# Task 21
if tsk == "Task 21":
    lst = [1,2,3,4,5]
    res = list(filter(lambda e: e%2 == 0, lst))
    print(res)


# Task 22
if tsk == "Task 22":
    lst = [1,2,3,4,5]
    res = list(filter(lambda e: e%2 != 0, lst))
    print(res)


# Task 23
if tsk == "Task 23":
    lst = [2,6,8,1]
    res = list(filter(lambda e: e > 5, lst))
    print(res)


# Task 24
if tsk == "Task 24":
    lst = [5, 12, 7, 20]
    res = list(filter(lambda e: e < 10, lst))
    print(res)


# Task 25
if tsk == "Task 25":
    lst = [1, -2, 3, -4]
    res = list(filter(lambda e: e >= 0, lst))
    print(res)


# Task 26
if tsk == "Task 26":
    lst = [1, -2, 3, -4]
    res = list(filter(lambda e: e < 0, lst))
    print(res)


# Task 27
if tsk == "Task 27":
    lst = [3, 5, 9, 10]
    res = list(filter(lambda e: e%3 == 0, lst))
    print(res)


# Task 28
if tsk == "Task 28":
    lst = [10, 12, 15, 7]
    res = list(filter(lambda e: e%5 == 0, lst))
    print(res)


# Task 29
if tsk == "Task 29":
    lst = [0, 5, 12, 8]
    res = list(filter(lambda e: e<=10 and e>=1, lst))
    print(res)


# Task 30
if tsk == "Task 30":
    lst = [7,2,7,4]
    res = list(filter(lambda e: e == 7, lst))
    print(res)

    
    
