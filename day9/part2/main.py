def load():
    with open("../file.txt", 'r') as file:
        smoke = []
        for line in file:
            line = [int(char) for char in line.strip()]
            smoke.append(line)
        return smoke

def getSize(number, i, j, smoke):
    #temp = smoke[i][j]
    smoke[i][j] = 0
    b=0
    t=0
    l=0
    r=0


    if i != 0:
        if smoke[i-1][j] != 0 and smoke[i-1][j] != 9:
            print(f"b: {smoke[i-1][j]} on {i-1},{j}")
            b = 1 + getSize(number, i-1, j, smoke)
    
    
    if i != len(smoke)-1:
        if smoke[i+1][j] != 0 and smoke[i+1][j] != 9:
            print(f"t: {smoke[i+1][j]} on {i+1},{j}")
            t = 1 + getSize(number, i+1, j, smoke)
    
    if j != 0:
        if smoke[i][j-1] != 0 and smoke[i][j-1] != 9:
            print(f"l: {smoke[i][j-1]} on {i},{j-1}")
            l = 1 + getSize(number, i, j-1, smoke)
    
    if j != len(smoke[0])-1:
        if smoke[i][j+1] != 0 and smoke[i][j+1] != 9:
            print(f"r: {smoke[i][j+1]} on {i},{j+1}")
            r = 1 + getSize(number, i, j+1, smoke)

    
    return b+t+l+r

    


def lowerPoints(smoke):
    total = [0,0,0]
    for i in range(len(smoke)):
        for j in range(len(smoke[0])):
            number = smoke[i][j]
            if i != 0 and i != len(smoke)-1:
                if number >= smoke[i-1][j] or number >= smoke[i+1][j]:
                    continue
            if i==0:
                if number >= smoke[i+1][j]:
                    continue
            if i == len(smoke)-1:
                if number >= smoke[i-1][j]:
                    continue

            if j != 0 and j != len(smoke[0])-1:
                if number >= smoke[i][j-1] or number >= smoke[i][j+1]:
                    continue
            if j==0:
                if number >= smoke[i][j+1]:
                    continue
            if j == len(smoke[0])-1:
                if number >= smoke[i][j-1]:
                    continue
            
            print(f"Calculating size for: {number} on line {i}, column {j}")
            size = getSize(number, i, j, smoke)
            total.append(size+1)
            total = sorted(total)[1:]

    print(total)
    return total[0] * total[1] * total[2] 

def main():
    smoke = load()
    print(lowerPoints(smoke))
        
if __name__ == "__main__":
    main() 