tsk = str(input("Enter Task No. [Ex:Task 1]: "))
# Task 1
if tsk == "Task 1":
    num = int(input("Enter The Number: "))
    if num%2 == 0:
        print("The Number is Even")
    else:
        print("The Number is Odd")
        

# Task 2
if tsk == "Task 2":
    age = int(input("Enter Age: "))
    if age >= 18:
        print("You are eligible to Vote")
    else:
        print("You are not eligible to Vote")


# Task 3
if tsk == "Task 3":
    mark = int(input("Enter Your Marks: "))
    if mark >= 40:
        print("You have passed in the Exam")
    else:
        print("You have failed in the Exam")


# Task 4
if tsk == "Task 4":
    num = int(input("Enter Number: "))
    if num >= 0:
        print("The Number is Positive")
    else:
        print("The Number is Negative")


# Task 5
if tsk == "Task 5":
    mark = int(input("Enter Your Marks: "))
    if mark > 90:
        print("Your Grade is Assigned as 'A'")
    elif mark >=75 and mark <= 89:
        print("Your Grade is Assigned as 'B'")
    elif mark >=50 and mark <= 74:
        print("Your Grade is Assigned as 'C'")
    else:
        print("Fail")


# Task 6
if tsk == "Task 6":
    fir = int(input("Enter First Number: "))
    sec = int(input("Enter Second Number: "))
    thr = int(input("Enter Third Number; "))
    lst = [fir, sec, thr]
    print(max(lst))


# Task 7
if tsk == "Task 7":
    num = int(input("Enter Number (1-7): "))
    if num == 1
        print("Monday")
    elif num == 2:
        print("Tuesday")
    elif num == 3:
        print("Wednesday")
    elif num == 4:
        print("Thursday")
    elif num == 5:
        print("Friday")
    elif num == 6:
        print("Saturday")
    elif num == 7:
        print("Sunday")
    else:
        print("Invalid Number")


# Task 8
if tsk == "Task 8":
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    op = str(input("Enter the arithmetic operation: "))

    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)
    elif op == "//":
        print(a//b)
    elif op == "%":
        print(a%b)
    elif op == "**":
        print(a**b)
    else:
        print("Invalid Arithmetic Operation!!")


# Task 9
if tsk == "Task 9":
    username = "Suriya"
    password = "password123"
    usr = str(input("Enter Username: "))
    psd = str(input("Enter Password: "))
    if usr == username:
        if psd == password:
            print("Login Success")
        else:
            print("Wrong Password")
    else:
        print("Invalid Username")


# Task 10
if tsk == "Task 10":
    signal = str(input("Enter Signal Type/Color: "))
    if signal == "red":
        print("Stop")
    elif signal == "yellow":
        print("Get Ready")
    elif sginal == "green":
        print("Go")
    else:
        print("Error: Invalid Signal!!")

else:
    print("Invalid Task No. !!")
    print("Type Like if your task No. 2")
    print("Task 2")

        
