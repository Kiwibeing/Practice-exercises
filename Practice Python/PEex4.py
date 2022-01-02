# Divisors: Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
list = list()
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if number % i == 0:
        list.append(i)
print(list)