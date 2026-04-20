tsk = str(input("Enter Task (Ex: [Task 1]): "))

# Task 1
if tsk == "Task 1":
    name = str(input("Enter Name: "))
    print(name.upper())


# Task 2
if tsk == "Task 2":
    sent = str(input("Enter Sentence: "))
    print(sent.lower())


# Task 3
if tsk == "Task 3":
    sent = str(input("Enter Sentence: "))
    print(sent.capitalize())


# Task 4
if tsk == "Task 4":
    name = str(input("Enter Name: "))
    age = int(input("Enter Age: "))
    print(f"I am {name} and I am {age} years old")


# Task 5
if tsk == "Task 5":
    word = "PYTHONEERS"
    print(word)
    ent = str(input("Enter The Letter in the word to find its index; "))
    print(word.index(f"{ent}"))


# Task 6
if tsk == "Task 5":
    word = "Python Programming"
    print(word)
    ent = str(input("Enter The Letter in the word to find its index; "))
    print(word.find(f"{ent}"))

# Task 7
if tsk == "Task 7":
    word = "Drawing"
    print(word.endswith("ing"))


# Task 8
if tsk == "Task 8":
    word = "s/tu/tr/ti/ty/ta"
    print(word)
    print(word.expandtabs(4))


# Task 9
if tsk == "Task 9":
    string = "Encode String"
    print(string.encode("UTF-8"))


# Task 10
if tsk == "Task 10":
    string = "123"
    print(string.isdigit())


# Task 11
if tsk == "Task 11":
    string = "456"
    print(string.isnumeric())


# Task 12
if tsk == "Task 12":
    string = "Hello123"
    print(string.isalnum())


# Task 13
if tsk == "Task 13":
    string = "ASCII"
    print(string.isascii())


# Task 14
if tsk == "Task 14":
    string = "Hello"
    print(string.isalpha())
