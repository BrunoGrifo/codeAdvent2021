import copy

check_track = []
reset = []
matrix = []

def toString(m):
    for x in m:
        print(x)
    print("\n")
    print("\n")

def load():
    global check_track, reset, matrix
    with open("../file.txt", 'r') as file:
        invalid_score = 0
        for line in file:
            matrix.append([int(x) for x in line.strip()])
            check_track.append([False for x in line.strip()])
            reset.append([False for x in line.strip()])




def explode(i,j):
    if i<0 or j<0 or i>=len(matrix[0]) or j>=len(matrix[0]):
        return 0
    if check_track[i][j] == True:
        return 0
    if matrix[i][j] == 9:
        matrix[i][j] = 0
        check_track[i][j] = True
        return 1 + explode(i-1,j) + explode(i,j-1) + explode(i-1,j-1) + explode(i+1,j) + explode(i,j+1) + explode(i+1,j+1) + explode(i-1,j+1) + explode(i+1,j-1)
    else:
        matrix[i][j] += 1
        return 0


def engine():
    final = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 9:
                if check_track[i][j] == False:
                    matrix[i][j] += 1
            else:
                final += explode(i,j)
    return final

def flash():
    for line in matrix:
        if not all(x==0 for x in line):
            return False
    return True

def main():
    global check_track, reset, matrix
    load()
    toString(matrix)
    result = 0
    for i in range(500):
        
        result += engine()
        if flash():
            print(i+1)
            return 0
        #toString(check_track)
        #toString(matrix)
        check_track = copy.deepcopy(reset)
    print(result)
        
if __name__ == "__main__":
    main() 