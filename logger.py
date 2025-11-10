from config import LOGLEVEL, DEBUG, INFO, WARNING, ERROR, FATAL, PRINT_CSV
from sys import stderr
import os

# theres definitely a good library for this but im lazy

def print_to_stderr(message):
  print(message, file=stderr)

def debug(message):
  if (LOGLEVEL <= DEBUG):
    print(message)

def info(message):
  if (LOGLEVEL <= INFO):
    print(message)

def warning(message):
  if (LOGLEVEL <= WARNING):
    print_to_stderr(message)

def error(message):
  if (LOGLEVEL <= ERROR):
    print_to_stderr(message)

def fatal(message):
  if (LOGLEVEL <= FATAL):
    print_to_stderr(message)

def print_csv(message,end="\n"):
  if (not PRINT_CSV in [None, False]):
    with open(PRINT_CSV, 'a') as file_handle:
      file_handle.write(message + end)

def clear_csv():
  if (not PRINT_CSV in [None, False]):
    if (isinstance(PRINT_CSV, str)):
      with open(PRINT_CSV, 'w') as file_handle:
        file_handle.write("")

# aliases
d = debug; i = info; w = warning; e = error; f = fatal;
warn = warning