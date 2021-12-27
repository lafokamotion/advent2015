#!/usr/bin/python3

class Coordination:
    def __init__(self):
        self.start = [0,0]

def read_file(name):
    file = open(name)
    return file.readline()

def make_moves(instructions):
    santa = Coordination()
    mappings = {
        '<': [0,-1],
        '>': [0,1],
        '^': [1,0],
        'v': [-1,0],
    }
    houses = {}

    for char in instructions:
        movement = mappings[char]
        santa.start[0]+=movement[0]
        santa.start[1]+=movement[1]
        # comma separate coordinates!
        key = str(santa.start[0]) + "," + str(santa.start[1])
        houses[key] = 1
    house_visits = len(set(houses)) + 1 # for the first house
    return house_visits

def make_dual_moves(instructions):
    santa = Coordination()
    robo = Coordination()
    mappings = {
        '<': [0,-1],
        '>': [0,1],
        '^': [1,0],
        'v': [-1,0],
    }
    houses = {}
    # reverse the instructions for pop usage
    instr_arr = list(instructions)
    instr_arr.reverse()
    while len(instr_arr) > 0:
        move = instr_arr.pop()
        movement = mappings[move]
        santa.start[0]+=movement[0]
        santa.start[1]+=movement[1]
        # comma separate coordinates!
        key = str(santa.start[0]) + "," + str(santa.start[1])
        houses[key] = 1
        if len(instr_arr) > 0:
            move = instr_arr.pop()
            movement = mappings[move]
            robo.start[0]+=movement[0]
            robo.start[1]+=movement[1]
            # comma separate coordinates!
            key = str(robo.start[0]) + "," + str(robo.start[1])
            houses[key] = 1
    house_visits = len(set(houses)) + 1 # for the first house
    return house_visits

instructions = read_file("input.txt")
visits = make_moves(instructions)
print("Houses visited at least once: ", visits)

dual_visits = make_dual_moves(instructions)
print("Houses visited at least once by both Santas: ", dual_visits)