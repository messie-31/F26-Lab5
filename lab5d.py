#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-21
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.
# TO DO 2: Follow the instructions from the readme.me file to create the exact output.
with open("pythonStatements.txt", "r") as py_file, open("machineCode.txt", "r") as mc_file, open("output.txt", "w") as out_file:
    py_lines = py_file.readlines()
    mc_lines = mc_file.readlines()
    for i in range(len(py_lines)):
        py_line = py_lines[i].strip()
        if "#" in py_line:
            py_line = py_line.split("#")[0].strip()
        mc_line = mc_lines[i].strip()
        out_line = f"{py_line}\t{mc_line}\n"
        out_file.write(out_line)
        print(f"{py_line}\t{mc_line}")