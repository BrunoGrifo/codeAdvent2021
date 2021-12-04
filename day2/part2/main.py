coor = {"up":0, "down":0, "forward":0, "depth":0}
with open("../file.txt", 'r') as file:
    for line in file:
        par = line.split(" ")
        if par[0] == "forward":
            coor["depth"] += (coor["down"] - coor["up"]) * int(par[1])
        coor[par[0]] += int(par[1])
        
print(coor)
print(coor["forward"]*coor["depth"])