import re

# Qn 1a: Create a string made of the first, middle and last character
str1 = "James"
length = int(len(str1))
first = str1[0]
last = str1[length - 1]
middle = str1[int((length - 1) / 2)]
first = first + middle + last
print("New string:", first)

# Qn 1b: Create a string made of the middle three characters
def middle_three(word):
    length = len(word)
    mid_pos = int((length - 1) / 2)

    # Use string slicing instead! Basically the same as range function, first argument inclusive last argument exclusive
    # string = word[mid_pos - 1: mid_pos + 2]
    middle = word[mid_pos]
    bef = word[mid_pos - 1]
    aft = word[mid_pos + 1]
    string = bef + middle + aft
    return print("New string:", string)

str1 = "JhonDipPeta"
middle_three(str1)
str2 = "JaSonAy"
middle_three(str2)

# Qn 2: Append new string in the middle of given string
s1 = "Ault"
s2 = "Kelly"
length1 = len(s1)
mid = int(len(s1) / 2)
x = s1[:mid]
x = x + s2
x = x + s1[mid:]
print("New string:", x)

# Qn 3: Create a new string made of the first, middle, and last characters of each input string
s1 = "America"
s2 = "Japan"
s1_length, s2_length = len(s1), len(s2)
s1_first, s2_first = s1[0], s2[0]
s1_mid, s2_mid = s1[int((s1_length - 1) / 2)], s2[int((s2_length - 1) / 2)]
s1_last, s2_last = s1[-1], s2[-1]
string = s1_first + s2_first + s1_mid + s2_mid + s1_last + s2_last
print("New string:", string)

# Qn 4: Rearrange letters such that lower cases come first
str1 = 'PyNaTive'
for i in str1:
    lower, upper = [], []
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
string = ''.join(lower + upper)
print("New string:", string)

# Qn 5: Calculate all letters, digits and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
print("Total count of chars, digits and symbols")
char, digit, sym = 0, 0, 0
for x in str1:
    if x.isalpha():
        char += 1
    elif x.isdigit():
        digit += 1
    else:
        sym += 1
print('Chars =', char, 'Digits =', digit, 'sym =', sym)

# Qn 6: Create a new string using certain rules
s1 = "Abc"
s2 = "Xyz"
s2 = s2[::-1]
result = ''
length = len(s1) if len(s1) > len(s2) else len(s2)
for i in range(length):
    if i < len(s1):
        result = result + s1[i]
    if i < len(s2):
        result = result + s2[i]
print(result)

# Qn 7: String char balance test
def balance(string1, string2):
    flag = True
    for x in string1:
        if x in string2:
            continue
        else:
            flag = False
    return flag

s1 = "Yn"
s2 = "PYnative"
print(balance(s1, s2))

s1 = "Ynf"
s2 = "PYnative"
print(balance(s1, s2))

# Qn 8:  Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
str1 = str1.lower()
print(str1.count('usa'))

# Qn 9: Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
sum = 0
digit_count = 0
for i in str1:
    if i.isdigit():
        sum = sum + int(i)
        digit_count += 1
    else:
        continue
avg = sum / digit_count
print('Sum is:', sum, 'Average is:', avg)

# Qn 10: Write a program to count occurrences of all characters within a string
str1 = "Apple"
char_dict = dict()
for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print(char_dict)

# Qn 11: Reverse a given string (Use negative slicing)
str1 = "PYnative"
str1 = str1[::-1]
print(str1)

# Qn 12: Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."
index = str1.rfind('Emma')
print("Last occurence of substring is at index", index)

# Qn 13: Split a string on hyphens (Split method returns a list)
str1 = 'Emma-is-a-data-scientist'
str1 = str1.split('-')
for m in str1:
    print(m)

# Qn 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
for x in str_list:
    if x == '':
        str_list.remove(x)
print(str_list)

# Qn 15: Remove special symbols/punctuation from a string (REGEX method!!)
str1 = "/*Jon is @developer & musician"
str1 = re.sub(r'[^\w\s]', '', str1)
print(str1)

# Qn 16: Remove all chars from a string except integers
str1 = 'I am 25 years and 10 months old'
string = ''
for x in str1:
    if x.isdigit():
        string = string + x
print(string)

# or use list comprehension:
string = ''.join([x for x in str1 if x.isdigit()])
print(string)

# Qn 17: Find words with both letters and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"
result = []
input = str1.split()
for item in input:
    if any([char.isalpha() for char in item]) and any([char.isdigit() for char in item]):
        result.append(item)
for res in result:
    print(res)

# Qn 18: Replace each special symbol with # in the following string
str1 = '/*Jon is @developer & musician!!'
str1 = re.sub(r'[^\w\s]', '#', str1)
print(str1)



