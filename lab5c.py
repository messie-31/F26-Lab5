#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-21
# Purpose: Process File data.
# Usage: ./lab5c.py

# TO DO 1: Run the code provided in readme.md file.
# TO DO 2: Open rhyme.txt file.
# TO DO 3: Print the output as directed in readme.md file.
with open("rhyme.txt", "w") as dataFile:
    dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")

f_read = open("rhyme.txt", "r")

line = f_read.readline()

while line != '':
    clean_line = line.strip().strip('.')
    words = clean_line.split()
    word_count = len(words)
    print(f"{clean_line} --- {word_count} words")
    line = f_read.readline()

f_read.close()