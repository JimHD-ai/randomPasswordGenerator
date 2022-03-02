import string
import random

#Need to create a list of all the letters and characters
character = list(string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()")

#ask the user for the length of the password
def randomPasswordGenerator():
    length = int(input("Enter the length of the password: "))
    #Need to shuffle the characters to an empty list
    random.shuffle(character)
    password = []
    for i in range(length):
        password.append(random.choice(character))
    #shuffle the password in the list
    random.shuffle(password)
    #convert the list to a string
    print(''.join(password))
#print the password
randomPasswordGenerator()