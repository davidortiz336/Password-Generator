# program will generate a strong password for a user
# will ask the user for amount of passwords and length for each password
# will return a password

import random

print('This Is Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

amount = input('Enter the number of passwords you would like to generate: ')
number = int(amount)

length = input('Enter the desired length for your password: ')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

