#!/usr/bin/env python3

# Originally copied from deepseek, based off of a bash script made using deepseek
# this script is just ran manually to grab op codes and output as csv

import os
import re

DIR = '.'

# Simple version that closely matches the original bash script
def simple_search():
  func_pattern = re.compile(r'func .*\(')
  search_pattern = re.compile(r'[.]put_op\(\d*\)')
  #func_grabber = re.compile(r'func ([a-zA-Z_]*)\(')
  number_grabber = re.compile(r'[.]put_op\((\d*)\)')
  for root, dirs, files in os.walk(DIR):
    for file in files:
      if file.endswith('.gd'):
        #print(file)
        filepath = os.path.join(root, file)
        #print(f"Processing {filepath}...")
        current_func = "Global Scope"
        with open(filepath, 'r', encoding='utf-8') as f:
          for line in f:
            line = line.strip()
            # Check for function definition
            if func_pattern.search(line):
              current_func = line
              # Check for search pattern
            if search_pattern.search(line):
              #print(f"Function: {current_func}")
              #print(f"Line: {line}")
              #print()
              #print(current_func)
              #current_func = func_grabber.match(current_func).group(1)
              # brute force it
              parentheses_index = current_func.index("(")
              current_func_name = current_func[5:parentheses_index]
              opcode = number_grabber.search(line).group(1)
              print(f"{opcode},{file},{current_func_name}")
simple_search()