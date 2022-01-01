import numpy as np
import copy

def load():
    template = {}
    with open("../file.txt", 'r') as file:
        for line in file:
            pair = line.strip().split(" -> ")
            template[pair[0]] = pair[1]
    return template

def dicCount(occurrences, total):
    for x in total:
        if x in occurrences:
            occurrences[x] += 1
        if x not in occurrences:
            occurrences[x] = 1

def getCount(total):
    occurrences = {}
    for x in total:
        if x in occurrences:
            occurrences[x] += 1
        if x not in occurrences:
            occurrences[x] = 1
    return occurrences

def runSequence(template):
    initial = ['B','N','S','O','S','B','B','K','P','C','S','C','P','K','P','O','P','N','N','K']
    for i in range(5):
        print(f"day {i}")
        new = []
        for x in range(0, len(initial)-1):
            new.append(initial[x])
            new.append(template[f"{initial[x]}{initial[x+1]}"])
        new.append(initial[x+1])
        initial = copy.copy(new)

    print("Counting....")
    occurrences = {}
    dicCount(occurrences, initial)
    
    storage = {}

    #final = []

    for j in range(len(initial)-1):
        print(f"{j} - {len(initial)}")

        pivot = [initial[j], initial[j+1]]

        if f"{initial[j]}{initial[j+1]}" in storage:
            #final.extend(storage[f"{initial[j]}{initial[j+1]}"])
            for key, value in storage[f"{initial[j]}{initial[j+1]}"]:
                occurrences[key]+=value

        else:
            for i in range(5,10):
                temp_new = []
                for x in range(0, len(pivot)-1):
                    temp_new.append(pivot[x])
                    temp_new.append(template[f"{pivot[x]}{pivot[x+1]}"])
                last = pivot[x+1]
                pivot = copy.copy(temp_new)
                pivot.append(last)

            storage[f"{initial[j]}{initial[j+1]}"] = copy.copy(getCount(temp_new))
            #storage[f"{initial[j]}{initial[j+1]}"] = temp_new

            dicCount(occurrences, temp_new)
            #final.extend(temp_new)
    
    final.append(initial[-1])

    
    key_max = max(occurrences.values())
    key_min = min(occurrences.values())
    return max_v, min_v 

def main():
    template = load()
    max_v, min_v = runSequence(template)
    #max_v, min_v = dicCount(total)
    print(max_v - min_v)        
if __name__ == "__main__":
    main() 