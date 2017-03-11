#! /usr/bin/python

import re

input = raw_input()
result = re.findall(r"[0-9]",input)
print(result)
