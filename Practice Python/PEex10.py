# List Overlap Comprehensions: Write a program that returns a list that contains only the elements that are common between the lists

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = set(a)
b = set(b)
new_set = a.intersection(b)
print(new_set)

# Better solution
list1 = random.sample(range(1, 30), 12)
list2 = random.sample(range(1, 30), 16)
new_list = [i for i in set(list1) if i in list2]
print(new_list)