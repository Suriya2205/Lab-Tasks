tsk = str(input("Enter Task (Ex: [Task 1]): "))

# Task 1
if tsk == "Task 1":
    for i in range(1, 100+1):
        print(i)


# Task 2
if tsk == "Task 2":
    start = int(input("Enter Start: "))
    end = int(input("Enter End: "))
    for i in range(start, end+1):
        if i%3 == 0:
            continue
        else:
            print(i)


# Task 3
if tsk == "Task 3":
    start = int(input("Enter Start: "))
    end = int(input("Enter End: "))
    for i in range(start, end+1):
        if i%9 == 0:
            break
        else:
            print(i)


# Task 4
if tsk == "Task 4":
    num = int(input("Enter Number: "))
    running = True
    while running:
        if num > 1:
            print(num)
        elif num == 1:
            running = False
    num-=1


# Task 5
if tsk == "Task 5":
    num = int(input("Enter Number: "))
    running = True
    while running:
        if num > 1:
            print(num)
        elif num == 1:
            pass
    num-=1


# Task 6
if tsk == "Task 6":
    num = int(input("Enter Number: "))
    running = True
    while running:
        if num > 1:
            print(num)
        elif num < 1:
            break
    num-=1


# Task 7
if tsk == "Task 7":
    word = "PYTHON"
    for char in word:
        if char == "H":
            continue
        else:
            print(char)


# Task 8
if tsk == "Task 8":
    num = 20
    running = True
    while running:
        if num > 0:
            if num == 17:
                continue
            elif num == 13:
                running = False
        else:
            running = False
    num-=1


