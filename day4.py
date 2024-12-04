#This code is quite unoptimised but works with my input since I have taken into account he number of lines and length of each line. Not sure if it will work with others though.

count = 0
part2 = 0

places = []
with open("input.txt", "r") as file:
    for i in file:
        places.append(i)


for v, i in enumerate(places):
    for index, location in enumerate(i):
        if i[index:index+4] == "XMAS":
            count +=1
        if i[index:index+4] == "SAMX":
            count +=1
        if v < 138 and location == "X" and places[v+1][index] == "M" and places[v+2][index] == "A" and places[v+3][index] == "S": #Vertical
            count +=1
        if v < 137 and location == "S" and places[v+1][index] == "A" and places[v+2][index] == "M" and places[v+3][index] == "X": #Vertical
            count +=1
        if v < 137 and location == "X" and places[v+1][index+1] == "M" and places[v+2][index+2] == "A" and places[v+3][index+3] == "S": #XMAS Diagonal Right
            count +=1
        if v < 137 and location == "X" and places[v+1][index-1] == "M" and places[v+2][index-2] == "A" and places[v+3][index-3] == "S": #XMAS Diagonal Left
            count +=1
        if v < 137 and location == "S" and places[v+1][index-1] == "A" and places[v+2][index-2] == "M" and places[v+3][index-3] == "X": #SAMX Diagonal Right
            count +=1
        if v < 137 and location == "S" and places[v+1][index+1] == "A" and places[v+2][index+2] == "M" and places[v+3][index+3] == "X": #SAMX Diagonal Right
            count +=1


for v, i in enumerate(places):
    for index, location in enumerate(i):
        if index < 138 and v < 138 and i[index] == "M" and i[index+2] == "S":
            if places[v+1][index+1] == "A":
                if places[v+2][index] == "M" and places[v+2][index+2] == "S":
                    part2 +=1

        if index < 138 and v < 138 and i[index] == "S" and i[index+2] == "S":
            if places[v+1][index+1] == "A":
                if places[v+2][index] == "M" and places[v+2][index+2] == "M":
                    part2 +=1
        
        if index < 138 and v < 138 and i[index] == "S" and i[index+2] == "M":
            if places[v+1][index+1] == "A":
                if places[v+2][index] == "S" and places[v+2][index+2] == "M":
                    part2 +=1

        if index < 138 and v < 138 and i[index] == "M" and i[index+2] == "M":
            if places[v+1][index+1] == "A":
                if places[v+2][index] == "S" and places[v+2][index+2] == "S":
                    part2 +=1

        
                
        

print(f"Part 1 {count}")
print(f"Part 2 {part2}")

