# Calculate the area of rectangle
def area_of_rectangle(length, width):
    return length * width



# Calculate the area of trangle

def area_of_triangle(base, height):
    return 0.5 * base * height



# Clculate perimeter of rectangle 

def perimeter_of_rectangle(length, width):
    return 2 * (length + width)


# Use a list comprehension to create a list of even numbers from 1 to 20.

even_numbers = [x for x in range(1, 20) if x % 2==0]
print("Even numbers: ", even_numbers)


# Write a lambda function to check if a number is divisible by 3 and use it with filter() on a list of numbers.
numbers = [1,3,5,6,9,8,10]
divisible_by_3 = list(filter(lambda x: x % 3 ==0 , numbers))
print(divisible_by_3)


# Create a decorator that prints "Starting..." before a function runs and "Done!" after it finishes.
def my_decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Done!")
    return wrapper

@my_decorator
def say_hello():
    print('Hello!')
say_hello()        



# Write a simple context manager that prints "Opening connection" on entry and "Closing connection" on exit.

class MyConnection:
    def __enter__(self):
        print('Opening connection')
        return self
    

    def __exit__(self, exc_track, exc_value, traceback):
        print("Closing connection")

with MyConnection():
    print("Doing something")   


# Roll a six sided die
import random
def roll_die():
    return random.randint(1, 6)
print("You rolled:", roll_die())   




# Shuffle a list of 5 names
import random
names = ["Lena", " Sina", "Louna", "Houda", "Mila"]
random.shuffle(names)
print("Shuffled names:", names)



# Generate a password with at least one uppercase letter

import random
import string

def generate_password(length = 8):
    if length < 1:
        return ""
    password = []
    password.append(random.choice(string.ascii_uppercase))
    all_chars = string.ascii_letters+string.digits
    password += random.choices(all_chars, k =length - 1)
    random.shuffle(password)
    return"".join(password)
print("Generate password: ", generate_password(10))


# Words of the day 

import random
words =[ "Sunshine", "River", "Ocean", "Beach"]
word_of_the_day = random.choice(words)
print("word of the day: ", word_of_the_day)