#!/usr/bin/python3

def read_file(name):
    file = open(name)
    line = file.readline()
    return line

output = read_file("input.txt")
floor_count = 0
index = 0
for char in output:
    index+=1
    if char == '(':
        floor_count+=1
    elif char == ')':
        floor_count-=1
    if floor_count == -1:
        print(index)
print(floor_count)