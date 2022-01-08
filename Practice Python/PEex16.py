# Password Generator: Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

import random

password_bank = ['pancake', 'cream', 'only', 'summer', 'celebrity', 'heaven', 'love', 'eight']
strong_pass_bank = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
pass_strength = input("How strong do you want the password to be? (weak / moderate / strong) \n>>> ")
if pass_strength == 'weak': 
    password = random.sample(password_bank, 1)
elif pass_strength == 'moderate':
    password = random.sample(password_bank, 3)
elif pass_strength == 'strong':
    password = random.sample(strong_pass_bank, 10)
password = ''.join(password)
print(password)