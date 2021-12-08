import numpy as np

def load():
    with open("../file.txt", 'r') as file:
        return sorted(list(map(int,next(file).strip().split(","))))

def getChildren(number, days):
    sequence = [number]
    newbies = []
    for i in range(days):
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
    
    return len(sequence) + len(newbies)

def getPopulation(sequence, days):
    memory = {}
    final = 0
    for number in sequence:
        print(number)
        if number in memory:
            final += memory[number]
        else:
            temp = getChildren(number, days)
            final += temp
            memory[number] = temp

    print(final)

def main():
    sequence = load()
    getPopulation(sequence, 256)
        
if __name__ == "__main__":
    main()
    