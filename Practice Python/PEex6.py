# String Lists: Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = input("Enter a string: ")
word = [i.lower for i in word if i is i.isupper]
reverse_word = word[::-1]
if word == reverse_word:
    print("Given string is a palindrome.")
else:
    print("Given string is not a palindrome.")