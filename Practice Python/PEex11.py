# Check Primality functions: Ask the user for a number and determine if it is a prime number
def get_number():
    number = int(input("Give a number: "))
    if number > 1:
        # Check for any factors
        for i in range(2, number):
            if number % i == 0:
                print("Number is not a prime number.")
                break
        else:
            print("Number is a prime number.")
    else:
        print("Number is not a prime number.")


# Alternative solution: Using flags
number = int(input("Enter number: "))
flag = False
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            flag = True
            break

# Check if flag is True
if flag:
    print("Number is not a prime number.")
else:
    print("Number is a prime number.")