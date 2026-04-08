tdk = input("Enter Task No. [Ex: Task 1]: ")
# Task 1
if tdk == "Task 1":   
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

# Task 2
if tdk == "Task 2": 
    shape = str(input("Enter the Shape: "))
    if shape == "rectangle":
        length = int(input("Enter lenght: "))
        breadth = int(input("Enter Breadth: "))
        print("Area:", length*breadth)
        print("Perimeter:",2*(length + breadth))
        
    elif shape == "square":
        side = int(input("Enter Side: "))
        print("Area:", side**2)
        print("Perimeter:", 4 * side)

    elif shape == "circle":
        radius = int(input("Enter Radius: "))
        print("Area:", 3.14 * (radius**2))
        print("Perimeter:", 2 * 3.14 * radius)

    else:
        print("Invalid Shape")


# Task 3
if tdk == "Task 3": 
    fir = int(input("Enter First Number: "))
    sec = int(input("Enter Second Number: "))
    thi = int(input("Enter Third Number: "))
    tot = fir+sec+thi
    print("The Average of Three Numbers is:",tot/3)


# Task 4
if tdk == "Task 4": 
    num = int(input("Enter A Number: "))
    com = int(input("Enter A Number to be Compared: "))
    if num == com:
        print("The two numbers are equal")
    elif num > com:
        print("The number is greater than the given number")
    elif num < com:
        print("The number is smaller than the given number")


# Task 5
if tdk == "Task 5": 
    numb = int(input("Enter The Number: "))
    sqrt_num = numb ** 0.5
    print("The Square Root of the Given Number is",sqrt_num)


# Task 6
if tdk == "Task 6": 
    amount = int(input("Enter Principal Amount: "))
    roi = int(input("Enter Rate of Interest: "))
    time = int(input("Enter Time in Years: "))
    ask = str(input("Enter the Kind of Interest"))
    if ask == "simple interest":
        numer = amount * roi * time
        denom = 100
        result = numer / denom
        print("The Simple Interest is:",result)
    elif ask == "compound interest":
        result = ( amount*((1 + (roi/100))**time) - amount )
        print("The Compound Interest is:",result)
    else:
        print("Invalid Operation!!")


# Task 7
if tdk == "Task 7": 
    x = 10
    y = int(input("Enter the Number for operation: "))
    opr = str(input("Enter the Operation: "))
    if opr == "+":
        x+=y
        print(x)
    elif opr == "-":
        x-=y
        print(x)
    elif opr == "*":
        x*=y
        print(x)
    elif opr == "/":
        x/=y
        print(x)
    elif opr == "%":
        x%=y
        print(x)
    elif opr == "**":
        x**=y
        print(x)
    else:
        print("Invalid Operation")


# Task 8
if tdk == "Task 8": 
    a =5
    b=3
    a=a+b
    b=a-b
    a=a-b
    print(a,b)


# Task 9
if tdk == "Task 9": 
    numb = int(input("Enter The Number: "))
    result = (numb ** (1/3))
    print(result)


# Task 10
if tdk == "Task 10": 
    numb = 8523
    l2d = numb % 100
    print(l2d)


# Task 11
if tdk == "Task 11": 
    numb = 8523
    rl2d = numb // 100
    print(rl2d)


else:
    print("Invalid Task No. !!")
    print("Type Like if your task No. 2")
    print("Task 2")
