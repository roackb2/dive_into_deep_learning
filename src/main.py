#!/usr/bin/env python
from playground.playground import run

def main():
  try:
    run()
  except Exception as e:
    print(e)
    exit(1)

if __name__ == '__main__':
  main()
