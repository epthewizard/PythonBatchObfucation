from random import choice
import string
import os
import subprocess
import time
import random
import sys

# Change this to whatever program you want to startup
goal = "start C:/WINDOWS/System32/calc.exe"

random_strings = []
list_of_characters = string.ascii_lowercase
final_command = []

def banner():
    print('''\033[91m
     ▄▄▄▄    ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██                                                   
▓█████▄ ▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒                                                  
▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░                                                  
▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██                                                   
░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓                                                  
░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒                                                  
▒░▒   ░   ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░                                                  
 ░    ░   ░   ▒    ░      ░         ░  ░░ ░                                                  
 ░            ░  ░        ░ ░       ░  ░  ░                                                  
      ░                   ░                                                                  
 ▒█████   ▄▄▄▄     █████▒█    ██   ██████  ▄████▄   ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █ 
▒██▒  ██▒▓█████▄ ▓██   ▒ ██  ▓██▒▒██    ▒ ▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒██░  ██▒▒██▒ ▄██▒████ ░▓██  ▒██░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██   ██░▒██░█▀  ░▓█▒  ░▓▓█  ░██░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
░ ████▓▒░░▓█  ▀█▓░▒█░   ▒▒█████▓ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
░ ▒░▒░▒░ ░▒▓███▀▒ ▒ ░   ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
  ░ ▒ ▒░ ▒░▒   ░  ░     ░░▒░ ░ ░ ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░ ░ ░ ▒   ░    ░  ░ ░    ░░░ ░ ░ ░  ░  ░  ░          ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
    ░ ░   ░                ░           ░  ░ ░            ░  ░         ░      ░ ░           ░ 
               ░                          ░                                                  
               ''')


    print('+[+[+[+ Generating ASCIi characters and preparing to obfuscate characters +]+]+]')
    time.sleep(3)
    
# Create a list of random strings. Length ranges from 5-10
def create_random_strings(min_length=5, max_length=10):
    while True:
        word = ''
        for _ in range(random.randrange(min_length, max_length)):
            this_choice = random.choice(list_of_characters)
            word += this_choice
        if word not in random_strings:
            random_strings.append(word)
            print(word)
        else:
            break

def pick_definitions(choices):
    # There is definitely a better way to do this but I was lazy
    # decision = str(input('Do you want to save the payload(1) or delete it(2)? $-> '))
    # while decision != '1' and decision != "2": 
        # decision = str(input('Do you want to save the payload (1) or delete it(2)? Please enter 1 to save or 2 to delete it $-> '))

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

if __name__ == '__main__':
    banner()
    create_random_strings()
    final_command = pick_definitions(random_strings)

    # if decision == '1':
        # word = str(input('What would you like to name the payload? Please do not enter any extensions, just the name $-> '))

    # Write the final command to the end of the file
    with open(f'payload.bat', 'a') as payload:
        payload.write(final_command)
    
    try:
        # if decision == 1:
            # subprocess.run('echo off && payload.bat', shell=True)
            # print('\033[92m[+[+[+ Successfully injected payload +]+]+]')
            # sys.exit()
        subprocess.run('echo off && payload.bat & notepad.exe payload.bat', shell=True)
        print('\n\033[92m[+[+[+ Successfully injected payload +]+]+]')
        sys.exit()

    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)