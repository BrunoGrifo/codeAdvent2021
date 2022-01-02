import numpy as np

def load():
    coor = []
    max_y = 0
    max_x = 0
    with open("../file.txt", 'r') as file:
        for line in file:
            words = line.strip().split(",")
            if int(words[0]) > max_x:
                max_x = int(words[0])
            if int(words[1]) > max_y:
                max_y = int(words[1])
            coor.append([int(words[0]), int(words[1])])
    return coor, max_x+1, max_y+1

def fold_v(paper, at):
    for j, line in enumerate(paper):
        for i, value in enumerate(line[at+1:]):
            if value == 1:
                mirror = i+1
                paper[j][at-mirror] = value
    return paper


def main():
    coor, max_x, max_y = load()
    paper = np.zeros((max_y, max_x))
    for point in coor:
        paper[point[1]][point[0]]=1

    paper = fold_v(paper, 655)

    total = np.sum(paper[:, :655])
    print(total)

        
if __name__ == "__main__":
    main() 