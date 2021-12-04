def getReport(l, flag):
    positions = {}
    for i in range(len(l[0])):
        positions[i] = 0
    for line in l:
        nums = [char for char in line]
        for count, value in enumerate(nums):
            if flag:
                positions[count] += 1 if value == "0" else -1
            else:
                positions[count] += 1 if value == "1" else -1

    return positions

def returnUniqueValue(index, report, values, flag):
    if len(values) == 1:
        return values[0]
    else:
        if not flag:
            check = str(1) if report[index] >= 0 else str(0)
        else:
            check = str(1) if report[index] > 0 else str(0)
        rows = [value for value in values if value[index]==check]
        return returnUniqueValue(index+1, getReport(rows, flag), rows, flag)

def main():
    with open("../file.txt", 'r') as file:
        rows = file.readlines()

    report = getReport(rows, False)
    oxygen = int(returnUniqueValue(0, report, rows, False), 2)
    print(oxygen)
    
    report = getReport(rows, True)
    co2 = int(returnUniqueValue(0, report, rows, True), 2)
    print(co2)

    print(oxygen * co2)

if __name__ == "__main__":
    main()
    