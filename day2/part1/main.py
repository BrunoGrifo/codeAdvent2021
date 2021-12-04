coor = {"up":0, "down":0, "forward":0}
with open("../file.txt", 'r') as file:
    for line in file:
        par = line.split(" ")
        coor[par[0]] += int(par[1])
print(coor)
print(coor["forward"]*(coor["down"] - coor["up"]))