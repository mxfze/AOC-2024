from itertools import product
part_one_sum  = 0
part_two_sum = 0

def check1(numbers, operators):
    starting_part_one = numbers[0] #gets the first index
    for v, x in enumerate(operators):
        if x == "+":
            starting_part_one += numbers[v+1]
        elif x == "*":
            starting_part_one *= numbers[v+1]
    return starting_part_one

def check2(numbers, operators):
    starting_part_two = numbers[0] #gets the first index
    for v, x in enumerate(operators):
        if x == "+":
            starting_part_two += numbers[v+1]
        elif x == "*":
            starting_part_two *= numbers[v+1]
        elif x == "|":
            starting_part_two = int(str(starting_part_two) + str(numbers[v+1]))
    
    return starting_part_two

with open("input.txt", "r") as file:
    for i in file:
        total, values = i.split(":")
        total = int(total)
        values = list(map(int, values.split()))
        a = len(values) -1 #amount of spaces that an operator can be placed in
        for i in product("+*", repeat=a): #all possibilites
            if check1(values, i) == total:
                part_one_sum += total
                break  
        for j in product("+*|", repeat=a): #Part 2
            if check2(values, j) == total:
                part_two_sum += total
                break
                
print(f"Part 1: {part_one_sum}")
print(f"Part 2: {part_two_sum}")

