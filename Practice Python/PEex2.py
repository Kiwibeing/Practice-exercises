# Odd or even: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

number = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))
if number % check == 0: 
    print(f"{number} can be evenly divided by {check}")
elif number % 4 == 0:
    print(f"{number} can be evenly divied by 4")
elif number % 2 ==0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")