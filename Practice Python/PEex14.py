# List remove duplicates: Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

list1 = [2, 2, 8, 9, 10, 10, 11]

# Method 1: Using loops and constructing the list
def remove_dupe(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(remove_dupe(list1))

# Method 2: Using sets
def remove_dupe_sets(list):
    list_set = set(list)
    return list_set
print(remove_dupe_sets(list1))