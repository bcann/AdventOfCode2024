#!/usr/bin/env python3

import argparse
import re

def puzzle1(inputs):
    total = 0
    for line in inputs:
        matches = re.findall(r"mul\([0-9]*,[0-9]*\)", line)
        for mul_inst in matches:
            mul_total = mult(mul_inst)
            total += mul_total
    return total

def puzzle2(inputs):
    total = 0
    do = True
    for line in inputs:
        matches = re.findall(r"mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)", line)
        for inst in matches:
            if inst[:5] == "don't":
                do = False
            elif inst[:2] == "do":
                do = True
            elif inst[:3] == "mul" and do:
                mul_total = mult(inst)
                total += mul_total
    return total

def mult(mul_inst: str) -> int:
    nums = mul_inst[4:].rstrip(')')
    nums = nums.split(',')
    return int(nums[0]) * int(nums[1])

def input_processor(filename):
    inputs = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            inputs.append(line)
        return inputs

def main():
    parser = argparse.ArgumentParser(description="Description of your script.")
    # Add arguments here if needed
    # parser.add_argument('-f', '--file', help='File to process', required=True)
    args = parser.parse_args()
    inputs = input_processor("Day3/puzzle_input")
    print(puzzle1(inputs))
    print(puzzle2(inputs))

if __name__ == "__main__":
    main()

