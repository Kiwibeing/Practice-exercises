# Exercise 1: Calculate the multiplication and sum of two numbers
number1 = input("Number 1: ")
number2 = input("Number 2: ")
x = int(number1) * int(number2)
sum = int(number1) + int(number2)
if x > 1000:
    print(f'The result is {x}.')

else:
    print(f'The result is {sum}')

# Exercise 2: Print the sum of the current number and the previous number
number_range = input("Range of numbers: ")
number_range = int(number_range)
assert number_range > 0
print(f"Printing current and previous number sum in a range({number_range})")
prev_num = 0
i = 0
while i < number_range:
    x_sum = prev_num + i
    print("Current Number", i, "Previous Number", prev_num - 1, "Sum:", x_sum)
    i += 1
    prev_num = i

# Exercise 3: Print characters from a string that are present at an even index number
get_string = input("String: ")
print(f"Original string is {get_string}")
print("Printing only even index chars")
string_length = len(get_string)
for i in range(0, string_length, 2):
    print(f"{get_string[i]}")


# Exercise 4: Remove first n characters from a string
def remove_chars(string, chars):
    return string[chars: ]

print(remove_chars("Kevin", 1))


# Exercise 5: Check if the first and last number of a list is the same
def first_last_num(given_list):
    print("Given list:", given_list)

    first_num = given_list[0]
    last_num = given_list[-1]

    if first_num == last_num:
        return True
    else:
        return False

# Exercise 6: Display numbers divisible by 5 from a list
list_input = [10, 20, 33, 46, 55]
print(f"Given list is {list_input}")
print("Divisible by 5")
for number in list_input:
    if number % 5 == 0:
        print(number)
    

# Exercise 7: Return the count of a given substring from a string
str_x = "Emma is good developer. Emma is a writer"
for word in str_x:
    output = 0
    if word == 'Emma':
        output += 1

print(f"Emma appeared {output} times.")


    






