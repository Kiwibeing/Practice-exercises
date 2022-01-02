# List less than 10: list numbers elements if conditional

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in list:
    if i < 5:
        print(i)

# New list with list comprehension
new_list = [i for i in list if i < 5]
print(new_list)

# Limit number
number = int(input("Enter a limit number: "))
new_list = [i for i in list if i < number]
print(new_list)