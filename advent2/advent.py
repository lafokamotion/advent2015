#!/usr/bin/python3

def calc_dimensions(line):
    len,wid,hei = line.split('x')
    l = int(len)
    w = int(wid)
    h = int(hei)
    smallest = min(l*w,w*h,h*l)
    return 2*l*w + 2*w*h + 2*h*l + smallest

def calc_ribbon_dim(line):
    len,wid,hei = line.split('x')
    l = int(len)
    w = int(wid)
    h = int(hei)
    bow = l*w*h
    largest = max(l,w,h)
    return (2*l+2*w+2*h) - 2*largest + bow

def read_file(name):
    file = open(name)
    total_sq_ft = 0
    total_ribbon_sq_ft = 0
    for line in file.readlines():
        sq_ft = calc_dimensions(line)
        total_sq_ft+=sq_ft
        sq_ft = calc_ribbon_dim(line)
        total_ribbon_sq_ft+=sq_ft
    return [total_sq_ft, total_ribbon_sq_ft]

output = read_file("input.txt")
print("Total Square Feet of wrapping paper needed: ", output[0])
print("Total Square Feet of ribbon needed: ", output[1])
