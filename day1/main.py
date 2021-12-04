count = -1
pivot = 0
with open("file.txt", 'r') as file:
    first = int(next(file))
    second = int(next(file))
    for line in file:
        if first + second + int(line) > pivot: count+=1
        pivot = first + second + int(line)
        first = second
        second = int(line)
print(count)