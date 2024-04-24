# Importing modules

import math
print("1. Math Module:")
print("Square root of 16:", math.sqrt(16))
print("Cosine of 45 degrees:", math.cos(math.radians(45)))

import random
print("\n2. Random Module:")
print("Random integer between 1 and 100:", random.randint(1, 100))
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))

import datetime
print("\n3. Datetime Module:")
print("Current date and time:", datetime.datetime.now())
print("Current year:", datetime.datetime.now().year)

import os
print("\n4. OS Module:")
print("Current working directory:", os.getcwd())
print("List of files in the current directory:", os.listdir())

import json
print("\n5. JSON Module:")
data = {'name': 'John', 'age': 30}
json_data = json.dumps(data)
print("JSON data:", json_data)

import hashlib
print("\n6. Hashlib Module:")
hashed_value = hashlib.sha256(b'Hello World').hexdigest()
print("SHA-256 hash of 'Hello World':", hashed_value)

import re
print("\n7. Regular Expression Module:")
pattern = r'\bcat\b'
print(pattern)
text = "I have a cat and a dog."
match = re.search(pattern, text)
if match:
    print("Found:", match.group())
else:
    print("No match found.")

import itertools
print("\n8. Itertools Module:")
perm = itertools.permutations([1, 2, 3])
print("Permutations of [1, 2, 3]:", list(perm))

import collections
print("\n9. Collections Module:")
counter = collections.Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print("Count of each element:", counter)

import sys
print("\n10. Sys Module:")
print("Python version:", sys.version)
print("System platform:", sys.platform)
