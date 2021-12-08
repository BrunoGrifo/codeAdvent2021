def load():
    with open("../file.txt", 'r') as file:
        return sorted(list(map(int,next(file).strip().split(","))))

def getPopulation(sequence):
    newbies = []
    for i in range(256):
        print(f"Dia {i}")
        pop = 0
        n_del = 0
        for fish in sequence:
            if fish > 0:
                break
            pop += 1
            newbies.append(9)
        
        if pop > 0:
            sequence = sequence[pop:]

        
        for num in newbies:
            if num == 6:
                n_del +=1
        
        newbies = newbies[n_del:]

        if n_del >0:
            sequence.extend([6]*n_del)
                
        sequence = [num - 1 for num in sequence]
        newbies = [num - 1 for num in newbies]
        #add
        if pop > 0:
            sequence.extend([6]*pop)
        
    print(len(sequence) + len(newbies))

    

def main():
    sequence = load()
    getPopulation(sequence)
        
if __name__ == "__main__":
    main()
    