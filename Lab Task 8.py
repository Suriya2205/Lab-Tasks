tsk = input("Enter Task {Task 1}: ")

# Task 1
if tsk == "Task 1":
    def fun():
        print("Hello")
    fun()


# Task 2
if tsk == "Task 2":
    def add(num1,num2):
        print(num1+num2)
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    add(a,b)


# Task 3
if tsk == "Task 3":
    a = lambda a: a**2
    print(a(4))


# Task 4
if tsk == "Task 4":
    a = [x for x in range(1, 25)]
    fil = lst(filter(lambda x: x%2 == 0,a))
    for i in fil:
        print(i, end = " ")


# Task 5
if tsk == "Task 5":
    a = [x for x in range(1, 10)]
    mapp = list(map(lambda x: x*2, a))
    for i in mapp:
        print(i, end = " ")


# Task 6
if tsk == "Task 6":
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    # Example usage
    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))
        

# Task 7
if tsk == "Task 7":
    def print_numbers(n):
        if n == 0:
            return
        print_numbers(n - 1)   
        print(n)

    # Example
    print_numbers(5)


# Task 8
if tsk == "Task 8":
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    res = lambda A,B: A+B
    print(res(a,b))


# Task 9
if tsk == "Task 9":
    lst = [x for x in range(1,10)]
    fil = list(filter(lambda b: b >5, lst))
    for i in fil:
        print(i, end = " ")


# Task 10
if tsk == "Task 10":
    lst = [x for x in range(1,11)]
    res = list(map(lambda x: x**2, lst))
    for i in res:
        print(i, end = " ")
