#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-21
# Purpose: Catch ZeroDivisionError
# Usage: ./lab5f.py

# TO DO 1: Complete the given functions.

def safe_divide(a,b):
    try:
        result = a / b
        print(result)
        return result
    except ZeroDivisionError:
        print("Zero Division Error")

def main():
  safe_divide(10,5)  # works
  safe_divide(10,0)  # exception : Zero Division Error

if __name__ == "__main__":
    main()