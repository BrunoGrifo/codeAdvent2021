def load():
    with open("../file.txt", 'r') as file:
        smoke = []
        for line in file:
            line = [int(char) for char in line.strip()]
            smoke.append(line)
        return smoke

def lowerPoints(smoke):
    total = 0
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
            
            print(f"Adding: {number} on line {i}, column {j}")
            total += number+1
    return total

def main():
    smoke = load()
    print(lowerPoints(smoke))
        
if __name__ == "__main__":
    main() 