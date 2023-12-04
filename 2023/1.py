#!/usr/bin/env python
import re
import sys

def main():
    digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    print(sum([int(''.join([n[0], n[-1]])) for n in [''.join([digits[w] if w in digits else w  for w in [m.group(1) for m in re.finditer(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', l.strip())]]) for l in sys.stdin]]))

if '__main__' == __name__:
    main()
