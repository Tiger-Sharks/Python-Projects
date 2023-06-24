# -*- coding: utf-8 -*-
"""
@author: Tiger Sharks
"""

import string
import random

length = int(input("Enter Password Length:  "))

print("Choose Character Set for Password:")
print("1. Digits")
print("2. Lowercase Characters")
print("3. Uppercase Characters")
print("4. Special Characters")
print("5. Include Spaces")
print("6. Proceed")

charList = ""

while (True):
    choice = int(input("Enter your choice:  "))
    if (choice == 1):
        charList += string.digits
    elif (choice == 2):
        charList += string.ascii_lowercase
    elif (choice == 3):
        charList += string.ascii_uppercase
    elif (choice == 4):
        charList += string.punctuation
    elif (choice == 5):
        charList += string.whitespace
    elif (choice == 6):
        break
    else:
        print("Invalid Option Selected!")

password = []

for x in range(length):
    randomChar = random.choice(charList)
    password.append(randomChar)

print("The Generated Password is: \n" + "".join(password))