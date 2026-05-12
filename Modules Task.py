import math
import time
import datetime
import random
import pywhatkit
import calendar

tsk = input("Enter Module Task: ")


# Math Module
if tsk == "Math"
print("Square root of 16:", math.sqrt(16))
print("Power (3^4):", math.pow(3, 4))
print("Pi value:", math.pi)
print("Ceiling of 5.3:", math.ceil(5.3))
print("Floor of 5.3:", math.floor(5.3))
print("Factorial of 5:", math.factorial(5))

# Unit Conversion (Hours / Grams)
hours = 2
minutes = 120
grams = 5000
kilograms = 5

print("Hours to minutes:", hours * 60)
print("Minutes to seconds:", minutes * 60)
print("Grams to kilograms:", grams / 1000)
print("Kilograms to grams:", kilograms * 1000)
print("Hours to seconds:", hours * 3600)


# Time Module
if tsk == "Time"
    print("Current time (epoch):", time.time())
    print("Pausing for 3 seconds...")
    time.sleep(3)
    print("Readable current time:", time.ctime())
    current_time = time.localtime()
    print("Hours:Minutes:Seconds =",
          current_time.tm_hour, ":", current_time.tm_min, ":", current_time.tm_sec)


# DateTime Module
if tsk == "Datetime"
    today = datetime.date.today()
    now = datetime.datetime.now()
    print("Today's date:", today)
    print("Current date and time:", now)
    print("Current year:", now.year)
    print("Current month:", now.month)
    print("Current day:", now.day)


# Calendar Module
if tsk == "Calender":
    year = 2026
    month = 5
    print("Calendar of current month:\n", calendar.month(year, month))
    print("Calendar of year 2026:\n", calendar.calendar(year))
    print("Is 2024 leap year?:", calendar.isleap(2024))
    print("Number of days in May 2026:", calendar.monthrange(year, month)[1])
    print("Weekday of 12 May 2026:", calendar.weekday(2026, 5, 12)) 


# Random Module
if tsk == "Random":
    print("Random number (1–10):", random.randint(1, 10))
    print("Random number (1–100):", random.randint(1, 100))
    sample_list = ["apple", "banana", "cherry", "date"]
    print("Random element from list:", random.choice(sample_list))
    print("Random float number:", random.random())
    random.shuffle(sample_list)
    print("Shuffled list:", sample_list)



# PyWhatKit Module
if tsk == "Pywhatkit":
    kit.search("Python programming")
    kit.playonyt("Python tutorial")
    kit.sendwhatmsg("+911234567890", "Hello from Python!", 15, 30)  # HH:MM format
    kit.info("Artificial Intelligence", lines=3)
