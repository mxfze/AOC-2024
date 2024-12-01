left = []
right = []
total = 0
similarity = 0
with open("input.txt", "r") as file:
    for i in file:
        l,r = map(int, i.split())
        left.append(l)
        right.append(r)

#Part 1
left.sort()
right.sort()

for x,v in enumerate(left):
    total += abs(left[x] - right[x])

#Part 2
for j in left:
    times = right.count(j)
    similarity += j * times
    
print(f"Part 1: {total}")
print(f"Part 2: {similarity}")


