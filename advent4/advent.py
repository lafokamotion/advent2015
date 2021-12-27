#!/usr/bin/python3

import hashlib

input = "ckczppom"

i = 1

while True:
    test_str = input + str(i)
    result = hashlib.md5(test_str.encode())
    # part one with 5 zeroes
    # part two with 6 zeroes
    if result.hexdigest().startswith('000000'):
        print(i)
        print(result.hexdigest())
        break
    else:
        i+=1
