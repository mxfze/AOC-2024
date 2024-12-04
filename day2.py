safe = 0
part2safe = 0
count = 0

def is_safe(thingy):
    global count
    count = 0
    ascending = sorted(thingy)
    descending = sorted(thingy, reverse=True)
    if thingy == ascending or thingy == descending:
            thingy.sort(reverse=True)
            for j in range((len(thingy)-1)):
                if abs(thingy[j] - thingy[j+1]) == 1 or abs(thingy[j] - thingy[j+1]) == 2 or abs(thingy[j] - thingy[j+1]) == 3:
                    count+=1
                
                if count == (len(thingy)-1):
                    return True
    
                
                    
def part_two():
    pass
with open("input.txt", "r") as file:
    for i in file:
        report = list(map(int, i.split()))

        #Part 1
        if is_safe(report):
            safe+=1
            part2safe +=1
        else:
            #Part 2
            for x in range(len(report)):
                modified_list = report[:x] + report[x + 1:]
                if is_safe(modified_list):
                    part2safe +=1
                    break


                    


print(f"Part 1: {safe}")
print(f"Part 2: {part2safe}")

