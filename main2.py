#a password generator app
import random
def password_generator(length):
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password=""
    for i in range(length):
        password+=random.choice(characters)
    return password
length=int(input("Enter the length of the password you want to generate:"))
print("Your generated password is: "+password_generator(length))