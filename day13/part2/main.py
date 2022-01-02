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

def fold_h(paper, at):
    for j, line in enumerate(paper[at+1:]):
        for i, value in enumerate(line):
            if value == 1:
                mirror = j+1
                paper[at-mirror][i] = value
    return paper


def main():
    coor, max_x, max_y = load()
    paper = np.zeros((max_y, max_x))
    for point in coor:
        paper[point[1]][point[0]]=1

    paper = fold_v(paper, 655)
    paper = fold_h(paper, 447)
    paper = fold_v(paper, 327)
    paper = fold_h(paper, 223)
    paper = fold_v(paper, 163)
    paper = fold_h(paper, 111)
    paper = fold_v(paper, 81)
    paper = fold_h(paper, 55)
    paper = fold_v(paper, 40)
    paper = fold_h(paper, 27)
    paper = fold_h(paper, 13)
    paper = fold_h(paper, 6)

    for x in paper[:6]:
        for i in x[:40]:
            if i==1:
                print('#', end =" ")
            else:
                print('.', end =" ")
            
        print('')


        
if __name__ == "__main__":
    main() 