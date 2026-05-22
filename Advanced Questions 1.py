import random

adv = int(input("Enter Advanced Question No.: "))


if adv == 1:
    print("Enter Mail IDs Like 101 102 102 103")
    ask = input("Enter Mail IDs: ")
    lst = ask.strip().split()
    nodupe = list(set(lst))
    dupe = []
    for i in lst:
        if lst.count(i) > 1:
            if i not in dupe:
                dupe.append(i)
    print("\nThese Mails IDs Have Sent Multiple Mails:", dupe, "\n")
    print("\nThese Are The Mails You Need To Read:", nodupe)


if adv == 2:
    ask = input("Enter The Message Here: ")
    lst = ask.strip().strip(".").split()
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    print("The Message Is:\n")
    for i in res:
        print(i, end = " ")


if adv == 3:
    ask = input("Enter The String: ")
    lst = list(ask)
    lst2 = []
    for i in lst:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz" or i in "1234567890":
            if i not in lst2:
                lst2.append(i)
    res_dict = {}
    for i in lst2:
        if i not in res_dict:
            res_dict[i] = lst.count(i)
    least = 1000000
    res = {}
    for key,value in res_dict.items():
        if value < least:
            least = value
    for key,value in res_dict.items():
        if value == least:
            res[key] = value
    for key,value in res.items():
        print(f"The Character which occurs in least times at the first place:")
        print(f"{key} : {value}")
        break
    print(f"res_dict: {res_dict}")
    print(f"res: {res}")


if adv == 4:
    substr = input("Enter Substring: ")
    count = int(input("Enter How Many IDs You Need: "))
    res = []
    running = True
    while len(res) < count:
            stri = ""
            leng = random.randint(1, 5)
            for i in range(leng):
                char = random.choice(list(substr))
                stri += char
            if str not in res:
                res.append(stri)

    print(f"These Are The IDs Generated: ")
    for i in res:
        print(i)
    print(len(res))