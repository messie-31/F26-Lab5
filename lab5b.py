#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-21
# Purpose: Write data to a file.
# Usage: ./lab5b.py

# TO DO 1: Paste the code provided in readme.md file.
# TO DO 2: Run the script.
# TO DO 3: Run the 'ls' command.
# TO DO 4: Print the contents of fruits.txt in a loop.
f = open("fruits.txt", "w")
f.write("1. Apples are crunchy.\n2. Oranges are sweet, sour and juicy.\n3. Strawberries are sweet.\n4. Which fruit do you like?\n")
f.close()
print("file fruits.txt has been created")
print("Reading the file fruits.txt ...")
f_read = open("fruits.txt", "r")
line = f_read.readline()
while line!="":
    print(line, end="")
    line = f_read.readline()
f_read.close()