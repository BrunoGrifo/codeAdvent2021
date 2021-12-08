def load():
    list_coor = []
    x_max = 0
    y_max = 0
    with open("../file.txt", 'r') as file:
        for line in file:
            coor = line.strip().replace(" -> ", ",").split(",")
            x = sorted([int(coor[0]), int(coor[2])])
            y = sorted([int(coor[1]), int(coor[3])])
            x_max = max(x_max, x[1])
            y_max = max(y_max, y[1])
            if x[0]==x[1] or y[0]==y[1]:
                list_coor.append({
                    "x": x,
                    "y": y,
                    "special": False
                    })
            else:
                temp = {
                    "x": x,
                    "y": y,
                    "special": True
                    }
                if ( int(coor[0]) < int(coor[2]) and int(coor[1]) > int(coor[3]) ) or ( int(coor[2]) < int(coor[0]) and int(coor[3]) > int(coor[1]) ):
                    temp["inverted"] = True
                else:
                    temp["inverted"] = False
                list_coor.append(temp)

    return list_coor, x_max+1, y_max+1


def fill_cloud(list_coor, cloud):
    for coor in list_coor:
        x = coor["x"]
        y = coor["y"]
        special = coor["special"]
        if not special:
            for i in range(x[0], x[1]+1):
                for j in range(y[0], y[1]+1):
                    cloud[i][j] += 1
        else:
            if coor["inverted"]:
                counter = y[1]
                for i in range(x[0], x[1]+1):
                    cloud[i][counter] += 1
                    counter -= 1
            else:
                counter = y[0]
                for i in range(x[0], x[1]+1):
                    cloud[i][counter] += 1
                    counter += 1
    return cloud

def dangerous_points(cloud):
    count = 0
    for i in cloud:
        for j in i:
            if j>=2:
                count+=1
    return count

def main():
    list_coor, x_max, y_max = load()
    cloud = []
    for i in range(x_max):
        cloud.append([0]*y_max)
    cloud = fill_cloud(list_coor, cloud)
    print(dangerous_points(cloud))
        
if __name__ == "__main__":
    main()
    