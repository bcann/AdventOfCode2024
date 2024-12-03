#!/usr/bin/env python3

import argparse

def puzzle1(inputs):
    safe_count = 0
    for report in inputs:
        if safe(report):
            safe_count += 1
    return safe_count

def puzzle2(inputs):
    safe_count = 0
    for report in inputs:
        if safe2(report):
            safe_count += 1
    return safe_count

def safe(report: list[int]) -> bool:
    current = report[0]
    descending = False
    if current > report[1]:
        descending = True
    for x in report[1:]:
        difference = abs(current - x)
        if  difference <= 3 and difference >= 1:
            if descending:
                if current > x:
                    current = x
                    continue
            else: 
                if current < x:
                    current = x
                    continue
        return False
    return True

def safe2(report: list[int]) -> bool:
    current = report[0]
    descending = False
    if current > report[1]:
        descending = True
    for i, x in enumerate(report[1:]):
        difference = abs(current - x)
        if  difference <= 3 and difference >= 1:
            if descending:
                if current > x:
                    current = x
                    continue
            else: 
                if current < x:
                    current = x
                    continue
        # Oh this brute force is disgusting.
        for j, _ in enumerate(report):
            report_copy = report.copy()
            del report_copy[j]
            if safe(report_copy):
                return True
        return False
    return True

def input_processor(filename):
    inputs = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                nums = line.split(" ")
                conv_nums = []
                for x in nums:
                    conv_nums.append(int(x))
                inputs.append(conv_nums)
        return inputs

def main():
    parser = argparse.ArgumentParser(description="Description of your script.")
    # Add arguments here if needed
    # parser.add_argument('-f', '--file', help='File to process', required=True)
    args = parser.parse_args()
    inputs = input_processor("puzzle_input")
    num_safe = puzzle2(inputs)
    print(num_safe)

if __name__ == "__main__":
    main()

