positions = {}
first = ""
second = ""
with open("../file.txt", 'r') as file:
    save = [char for char in next(file).strip()]
    for i in range(len(save)):
        positions[i] = 0
    print(positions)

    for line in file:
        nums = [char for char in line.strip()]
        for count, value in enumerate(nums):
            positions[count] += 1 if value == "1" else -1
    
    for count, value in enumerate(save):
            positions[count] += 1 if value == "1" else -1

for i in range(len(save)):
    if positions[i] > 0:
        first += "1"
        second += "0"
    else:
        first += "0"
        second += "1"

print(int(first,2) * int(second,2))


    