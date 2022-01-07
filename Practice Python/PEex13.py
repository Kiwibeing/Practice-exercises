# Fibonacci: Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

length = int(input("How many Fibonacci numbers to generate? >> "))
previous, current = 0, 1
counter = 1
fib_list = [1]
while counter < length:
    current, previous = current + previous, current
    fib_list.append(current)
    counter += 1
print(fib_list)