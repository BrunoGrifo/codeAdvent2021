import numpy as np

def load():
    template = {}
    with open("../file.txt", 'r') as file:
        for line in file:
            pair = line.strip().split(" -> ")
            template[pair[0]] = pair[1]
    return template

def dicCount(total):
    occurrences = {}
    for x in total:
        if x in occurrences:
            occurrences[x] += 1
        if x not in occurrences:
            occurrences[x] = 1
    key_max = max(occurrences.values())
    key_min = min(occurrences.values())
    return key_max, key_min

def runSequence(template):
    initial = ['B','N','S','O','S','B','B','K','P','C','S','C','P','K','P','O','P','N','N','K']
    for i in range(6):
        print(f"day {i}")
        new = []
        for x in range(0, len(initial)-1):
            new.append(initial[x])
            new.append(template[f"{initial[x]}{initial[x+1]}"])
        new.append(initial[x+1])
        initial = new
    return new

def main():
    template = load()
    total = runSequence(template)
    print(len(total))
    max_v, min_v = dicCount(total)
    print(max_v - min_v)        
if __name__ == "__main__":
    main() 