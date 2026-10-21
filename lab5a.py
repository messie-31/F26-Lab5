#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-21
# Purpose: Read a text file.
# Usage: ./lab5a.py

# TO DO 1: Create data2.txt.
# TO DO 2: Complete the functions below.
def read_file_lineByLine(file_name):
    with open(file_name, "r") as f:
        for line in f:
            print(line.strip())
def read_file_list(file_name):
    lines_list= []
    with open(file_name, "r") as f:
        for line in f:
            lines_list.append(line.strip())
    return lines_list
def main():
    file_name = 'data2.txt'
    read_file_lineByLine(file_name)
    print(read_file_list(file_name))

if __name__ == "__main__":
    main()
