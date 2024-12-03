#!/usr/bin/env python3

import argparse


def puzzle1(list1, list2):
    list1.sort()
    list2.sort()
    total = 0
    for x, y in zip(list1, list2):
        distance = abs(x - y)
        total += distance
    return total

def puzzle2(list1, list2):
    similarity_total = 0

    for x in list1:
        l2_count = list2.count(x)
        similarity = x * l2_count
        similarity_total += similarity
    return similarity_total

def input_processor(filename):
    with open(filename, "r") as f:
        list1 = []
        list2 = []
        for line in f:
            line = line.strip()
            if line:
                nums = line.split("   ")
                list1.append(int(nums[0]))
                list2.append(int(nums[1]))
        return (list1, list2)

def main():
    parser = argparse.ArgumentParser(description="Description of your script.")
    # Add arguments here if needed
    # parser.add_argument('-f', '--file', help='File to process', required=True)
    args = parser.parse_args()
    lists = input_processor("puzzle_input1")
    #list1 = [3, 4, 2, 1, 3, 3]
    #list2 = [4, 3, 5, 3, 9, 3]
    list1 = lists[0]
    list2 = lists[1]
    #total = puzzle1(list1, list2)
    #print(total)

    similarity = puzzle2(list1, list2)
    print(similarity)

if __name__ == "__main__":
    main()

