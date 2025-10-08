## Password Generator ##

print("PASSWORD GENERATOR")

import random

def generatePassword(length = 16):
    lower =  "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/,._-$£&!<>~@?¬"
    
    all = lower + upper + numbers + symbols
    password = "".join(random.sample(all, length))
    
    return password

number = int(input("Enter the length of your password: "))
print(generatePassword(number))
