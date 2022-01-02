# Character input: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter name: ")
age = int(input("Enter age: "))
year = 2022 + (100 - age)
def message():
    return(print(f"{name} will be 100 years old in year {year}."))
message()
repeat = int(input("Enter a number: "))
for i in range(repeat):
    message()