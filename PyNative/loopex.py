# Qn 1: Print first 10 natural numbers using while loop
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

# Qn 2: Print the pyramid pattern
row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end= ' ')
    print("")

# Qn 3: Calculate the sum of all numbers from 1 to a given number
number = int(input("Enter number: "))
sum = 0
number_count = 1
while number_count <= number:
    sum += number_count
    number_count += 1
print("Sum is: ", sum)

s = 0
n = int(input("Enter number: "))
for i in range(1, n + 1, 1):
    s += i
print("Sum is: ", sum)

# Qn 4: Write a program to print the multiplication table of a number
num = 2
for i in range(1, 11, 1):
    product = num * i
    print(product)

# Qn 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i % 5 == 0:
        print(i)
    elif i > 150:
        continue
    elif i > 500:
        break

# Qn 6: Count the total number of digits in a number
number = int(input("Enter number: "))
counter = 0
while number != 0:
    number = number // 10
    counter += 1
print(counter)

# Qn 7: Print the following pattern
row = 5
for r in range(5, 0, -1):
    for c in range(r, 0, -1):
        print(c, end= ' ')
    print('')

# Qn 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
size = len(list1)
for i in range(size, -1, -1):
    print(list1[i])

# Qn 9: Display numbers from -10 to -1 using a loop
start = -10
while start < 0:
    print(start)
    start += 1

for num in range(-10, 0 , 1):
    print(num)

# Qn 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")

# Qn 10: Write a program to display all prime numbers within a range
start = 25
end = 50
for i in range(start, end + 1, 1):
    if i > 1:
        if i % 2 != 0:
            print(i)
        else:
            break
    else:
        continue
    




    
