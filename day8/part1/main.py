import numpy as np
import statistics

def match(x, y):
    if sorted(x) == sorted(y):
        return True
    else:
        return False

def parcial(str1, str2):
    return all([i in str2 for i in str1])

def fillMapping(mapping, sequence):
    newSequence = []
    for digit in sequence:
        if len(digit) == 2:
            mapping[1] = digit
        elif len(digit) == 3:
            mapping[7] = digit
        elif len(digit) == 4:
            mapping[4] = digit
        elif len(digit) == 7:
            mapping[8] = digit
        else:
            newSequence.append(digit)
    for digit in newSequence:
        if len(digit) == 6:
            if parcial(mapping[4], digit):
                mapping[9] = digit
            elif parcial(mapping[1], digit) and not parcial(mapping[4], digit):
                mapping[0] = digit
            else:
                mapping[6] = digit
    for digit in newSequence:
        if len(digit) == 5:
            if parcial(mapping[1], digit) and parcial(mapping[7], digit):
                mapping[3] = digit
            elif parcial(digit, mapping[6]):
                mapping[5] = digit
            else:
                mapping[2] = digit

    return newSequence
        

def decode(sequence):
    print("New line...")
    mapping = {}
    sequence = fillMapping(mapping, sequence)
    return mapping

def decodedValue(sequence, mapping):
    number = ""
    for digit in sequence:
        if len(digit) == 2:
            number += "1"
        elif len(digit) == 3:
            number += "7"
        elif len(digit) == 4:
            number += "4"
        elif len(digit) == 7:
            number += "8"
        else:
            if len(digit) == 5:
                if match(digit, mapping[3]):
                    number += "3"
                elif match(digit, mapping[5]):
                    number += "5"
                else:
                    number += "2"
            if len(digit) == 6:
                if match(digit, mapping[9]):
                    number += "9"
                elif match(digit, mapping[6]):
                    number += "6"
                else:
                    number += "0"

    return int(number)


def load():
    with open("../file.txt", 'r') as file:
        total = 0
        mapping = {}
        with open("../file.txt", 'r') as file:
            for line in file:
                sequence = line.strip().split(" | ")
                print(sequence)
                part1 = sequence[0].split(" ")
                part2 = sequence[1].split(" ")

                mapping = decode(part1)
                total += decodedValue(part2, mapping)

        return total
def main():
    final = load()
    print(final)
        
if __name__ == "__main__":
    main()
    