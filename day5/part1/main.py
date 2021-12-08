def load():
    list_coor = []
    x_max = 0
    y_max = 0
    with open("../file.txt", 'r') as file:
        for line in file:
            coor = line.strip().replace(" -> ", ",").split(",")
            x = sorted([int(coor[0]), int(coor[2])])
            y = sorted([int(coor[1]), int(coor[3])])
            x_max = max(x_max, max(x))
            y_max = max(y_max, max(y))
            if x[0]==x[1] or y[0]==y[1]:
                list_coor.append({
                    "x": x,
                    "y": y,
                    })
    return list_coor, x_max+1, y_max+1


def fill_cloud(list_coor, cloud):
    for coor in list_coor:
        x = coor["x"]
        y = coor["y"]
        for i in range(x[0], x[1]+1):
            for j in range(y[0], y[1]+1):
                cloud[i][j] += 1
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
    