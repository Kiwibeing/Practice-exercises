# Qn 1: Create a function in Python
def name_age(name, age):
    return print(name, age)

# Qn 2: Create a function with variable length of arguments
def func1(*numbers):
    print("Printing values")
    for i in numbers:
        print(i)
    return 1

# Qn 3: Return multiple values from a function
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

# Qn 4: Create a function with default argument
def show_employee(name, salary = 9000):
    print('Name:', name, 'salary:', salary)
    return 1

# Qn 5: Create an inner function to calculate the addition in a following way
def outer_func(a, b):
    def addition(a, b):
        sum = a + b
        return sum
    return sum + 5

# Qn 6: Create a recursive function
def recursive(num):
    if num == 0:
        return 0
    else:
        return num + recursive(num - 1)

# Qn 7: Generate a Python list of all the even numbers between 4 to 30
def even_num():
    list = [i for i in range(4, 30, 2)]
    return list

# Qn 8: Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
print(max(x))
