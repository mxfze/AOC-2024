total = 0
total_part_two = 0
parsed = ""
parsed2 = ""
valids = []
valids_part_two = []
enabled = True


with open("input.txt", "r") as file:
    content = file.read().replace("\n", "")
    for i in content:
        parsed += i
        parsed2 +=i

#Part 1
for v,i in enumerate(parsed):
    if parsed[v] == "m" and parsed[v+1] == "u" and parsed[v+2] =="l" and parsed[v+3] == "(":
        if parsed[v+7] == ")" and parsed[v+6].isdigit():
            valids.append(parsed[v+4:v+7])
        if parsed[v+8] == ")" and parsed[v+7].isdigit():
            valids.append(parsed[v+4:v+8])
        if parsed[v+9] == ")" and parsed[v+8].isdigit():
            valids.append(parsed[v+4:v+9])
        if parsed[v+10] == ")" and parsed[v+9].isdigit():
            valids.append(parsed[v+4:v+10])
        if parsed[v+11] == ")" and parsed[v+10].isdigit():
            valids.append(parsed[v+4:v+11])
    
    else:
        continue

#Part 2
for v, i in enumerate(parsed2):
    if parsed[v] == "d" and parsed[v+1] == "o" and parsed[v+2] == "n" and parsed[v+3] == "'" and parsed[v+4] == "t" and parsed[v+5] == "(" and parsed[v+6] == ")":
        enabled = False
    elif parsed[v] == "d" and parsed[v+1] == "o" and parsed[v+2] == "(" and parsed[v+3] == ")":
        enabled = True
    if parsed2[v] == "m" and parsed2[v+1] == "u" and parsed2[v+2] =="l" and parsed2[v+3] == "(":
        if parsed2[v+7] == ")" and parsed2[v+6].isdigit() and enabled == True:
            valids_part_two.append(parsed[v+4:v+7])
        if parsed2[v+8] == ")" and parsed2[v+7].isdigit() and enabled == True:
            valids_part_two.append(parsed[v+4:v+8])
        if parsed2[v+9] == ")" and parsed2[v+8].isdigit() and enabled == True:
            valids_part_two.append(parsed[v+4:v+9])
        if parsed2[v+10] == ")" and parsed2[v+9].isdigit() and enabled == True:
            valids_part_two.append(parsed[v+4:v+10])
        if parsed2[v+11] == ")" and parsed2[v+10].isdigit() and enabled == True:
            valids_part_two.append(parsed2[v+4:v+11])

            
for i in valids:
    a,b = map(int, i.split(","))
    total += a*b

for i in valids_part_two:
    a,b = map(int, i.split(","))
    total_part_two += a*b
print(f"Part 1: {total}")
print(f"Part 2: {total_part_two}")


