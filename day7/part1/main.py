import numpy as np
import statistics

def load():
    with open("../file.txt", 'r') as file:
        f_list = list(map(int,next(file).strip().split(",")))
        return f_list

def getMedian(sequence):
    return statistics.median(sequence)

def getFuel(number, sequence):
    fuel = 0
    for x in sequence:
        fuel += abs(x-number)
    return fuel


def main():
    sequence = load()
    median = getMedian(sequence)
    target = getFuel(int(median), sequence)
    l_target = getFuel(int(median)-1, sequence)
    h_target = getFuel(int(median)+1, sequence)
    
    if l_target < target:
        save = l_target
        lower = l_target
        t_median = (int(median)-1)
        while(lower < l_target):
            lower = getFuel(t_median-1, sequence)
            if lower < save:
                save = lower
        print(save)

    elif h_target < target:
        lower = h_target
        save = h_target
        t_median = (int(median)+1)
        while(lower < l_target):
            lower = getFuel(t_median+1, sequence)
            if lower < save:
                save = lower
        print(save)
    else:
        print(target)

        
if __name__ == "__main__":
    main()
    