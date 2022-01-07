# List ends: Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list. 

a = [5, 10, 15, 20, 25]

def list_ends(list):
    x = [a[0], a[-1]]
    return x

print(list_ends(a))