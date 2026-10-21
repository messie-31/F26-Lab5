#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-21
# Purpose: Handle FileNotFoundError
# Usage: ./lab4e.py

# TO DO 1: Create text file numbers.txt as directed in readme.md file.
# TO DO 2: Complete the add() functions.
def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except Exception as e:
        return str(e)
    
# TO DO 3: Complete the read_file() functions.
def read_file(filename):
    numbers_list = []
    f=None
    try:
        f=open(filename, "r")
        for line in f:
            numbers_list.append(int(line.strip()))
        return numbers_list
    except FileNotFoundError:
        return "Exception: could not open the file"
    except ValueError:
        return "Exception: error reading the data"
    finally:
        if f is not None:
            f.close()

def main():
    print(add(10,5))
    print(add("10",5))
    print(add("abc",5))
    print(read_file("file10000.txt"))
    print(read_file("numbers.txt"))

if __name__ == "__main__":
    main()