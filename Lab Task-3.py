tsk = str(input("Enter Task No. [Ex: Task 1]: "))

# Task 1
if tsk == "Task 1":
    for i in range(1,11):
        print(i)


# Task 2
elif tsk == "Task 2":
    num = int(input("Enter the Number: "))
    times = int(input("Enter the No. of Times to run: "))
    for i in range(1,times+1):
        print(num, "x", i, "=", num*i)


# Task 3
elif tsk == "Task 3":
    for i in range(1, 51):
        if i%2 == 0:
            print(i)


# Task 4
elif tsk == "Task 4":
    res = 1
    ask = int(input("Enter the No. for factorial: "))
    for i in range(1,ask+1):
        res*=i
    print(res)


# Task 5
elif tsk == "Task 5":
    num = int(input("Enter The Number: "))
    i = 0
    s = num
    while s > 0:
        m = s % 10
        i = (i*10) + m
        s = s // 10
    print(i)
    if i == num:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")


# Task 6
elif tsk == "Task 6":
    ask = int(input("Enter the size of the Triangle: "))
    for i in range(1, ask+1):
        print("*"*i)
    print()


# Task 7
elif tsk == "Task 7":
    for i in range(2, 21):
        if i%2 == 0:
            print(i)


# Task 8
elif tsk == "Task 8":
    i = 1
    while i<=10:
        print(i)
        i+=1


# Task 9
elif tsk == "Task 9":
    i = 0
    running = True
    while running:
        if i == 20:
            running = False
        print(i)
        i+=1


# Task 10
elif tsk == "Task 10":
    i = 10
    running = True
    while running:
        if i == 1:
            running = False
        print(i)
        i-=1
        
