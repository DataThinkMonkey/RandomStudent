import random

list = input("Enter file name of list in current directory: ")

# Read student list files as list, split by line.
with open(list, 'r') as f:
    studentlist = f.read().splitlines()

# Randomly choose from list
print(random.choice(studentlist))

# Ask for another random name
repeat = int(input("\n1. List another random name.\n2. Quit.\nSelection: "))

while repeat==1:
    print(random.choice(studentlist))
    repeat = int(input("\n1. List another random name.\n2. Quit.\nSelection:  "))
