# Part 2 for Day 6 is coming soon.
map = []
crashed = False
current_level = 0
positions = []

with open("input.txt", "r") as file:
    for i in file:
        map.append(i.rstrip("\n"))

for y_value, level in enumerate(map):
    if "^" in level:
        direction = "up"
        x =  level.index("^")
        y = y_value
        pos = (x, y)
        positions.append(pos)

def move(direction):
    global x, y, pos, crashed, map, current_level 
    if direction == "up":
        while crashed == False and direction == "up":
            y-=1
            pos = (x, y)                
            if pos not in positions:
                positions.append(pos)
            if map[y-1][x] == "#":
                direction = "right"
                move("right")

                crashed = True

    if direction == "right":
            while crashed == False and direction == "right":
                x +=1
                pos = (x, y)
                if pos not in positions:
                    positions.append(pos)
                if map[y][x+1] == "#":
                        direction = "down"
                        move("down")
                        crashed = True


    if direction == "down":
            while crashed == False and direction == "down":
                y+=1
                pos = (x, y)
                if pos not in positions:
                    positions.append(pos)
                if map[y+1][x] == "#":
                            direction = "left"
                            move("left")
                            crashed = True
                    


    if direction == "left":
            while crashed == False and direction == "left":                
                if x > 0:
                    x -=1
                else:
                    print(f"Part 1: {len(positions)}")
                    break
                
                pos = (x, y)
                
                if pos not in positions:
                    positions.append(pos)
                try:
                    if map[y][x-1] == "#":
                        direction = "up"
                        move("up")
                        crashed = True

                except IndexError:
                     print(len(positions))
                     break


move("up")
