# Reverse word order: Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. 

sentence = input("Enter a sentence to reverse words: \n")
sentence= sentence.split()
reverse = sentence[::-1]
result = ' '.join(reverse)
print(result)

# Which can be condensed into result = ' '.join(setntence.split()[::-1])