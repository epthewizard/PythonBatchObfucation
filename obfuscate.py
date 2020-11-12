import os
from random import choice
import string
import random

goal = "start C:/WINDOWS/System32/calc.exe"

random_strings = []
list_of_characters = string.ascii_lowercase
final_command = []

# Create a list of random strings. Length ranges from 5-10
def create_random_strings(min_length=5, max_length=10):
    while True:
        length = random.randrange(min_length, max_length)
        word = ''
        for _ in range(length):
            this_choice = random.choice(list_of_characters)
            word += this_choice
        if word not in random_strings:
            random_strings.append(word)
            print(word)
        else:
            break
    print(random_strings)

def pick_definitions(choices):
    # There is definitely a better way to do this but I was lazy
    with open('payload.bat', 'a') as file:
        start = random.choice(choices)
        second = random.choice(choices)
        third = random.choice(choices)
        file.write(f"set {start}=set\n")
        file.write(f"%{start}% {second}= \n")
        file.write(f"%{start}%%{second}%{third}==\n")
    # Set random variables equal to each letter in goal
        for x in goal:
            remove = random.choice(choices)
            file.write(f"%{start}%%{second}%{remove}%{third}%{x}\n")
            final_command.append(f"%{remove}%")
            choices.remove(remove)
    return ''.join(final_command)

create_random_strings()
final_command = pick_definitions(random_strings)

with open('payload.bat', 'a') as payload:
    payload.write(final_command)