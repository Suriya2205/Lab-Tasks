tsk = input("Enter Task {Task 1}: ")


# Task 1
if tsk == "Task 1":
    lst = []
    for i in range(3):
        a = int(input(f"Enter {i+1}st Number: "))
        lst.append(a)
    res = lambda x: max(x)
    print(f"Maximum: {res(lst)}")


# Task 2
if tsk == "Task 2":
    num = int(input("Enter Number: "))
    lst = list(num)
    res = filter(lambda a: a%2 == 0, lst)
    if res == True:
        print("Even")
    else:
        print("Odd")


# Task 3
if tsk == "Task 3":
    num = int(input("Enter Number: "))
    lst = list(num)
    res = filter(lambda a: a%5, lst)
    if res == True:
        print("Divisible By 5")
    else:
        print("Not Divisible By 5")
