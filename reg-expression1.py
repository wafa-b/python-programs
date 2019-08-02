import re

pattern = "^[a-zA-Z]*$"

name = input("Please enter your name: ")

if re.match(pattern,name):
    print('text matched')
else:
    print('text not matched')
