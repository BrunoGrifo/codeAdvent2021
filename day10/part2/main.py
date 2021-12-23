def checkClosing(line, track, char):
    if track[char][0] <= 0:
        return False
    for key in track:
        if key != char:
            if len(track[key][1]) == 0:
                continue
            if track[key][1][-1] > track[char][1][-1]:
                return False

    return True

def load():
    with open("../file.txt", 'r') as file:
        invalid_score = 0
        incomplete_score = []
        for line in file:
            print("NEW LINEEEEEE")
            flag = True
            track = {
                ')': [0,[]], 
                '}': [0,[]], 
                ']': [0,[]], 
                '>': [0,[]]}
            scores = {
                '(': 1,
                '[': 2,
                '{': 3,
                '<': 4}
            copy = line.strip()
            to_remove = []
            for i, char in enumerate(line.strip()):
                if char == '(':
                    track[')'][0] += 1
                    track[')'][1].append(i)
                elif char == '{':
                    track['}'][0] += 1
                    track['}'][1].append(i)
                elif char == '[':
                    track[']'][0] += 1
                    track[']'][1].append(i)
                elif char == '<':
                    track['>'][0] += 1
                    track['>'][1].append(i)

                elif char == ')':
                    if not checkClosing(line, track, char):
                        invalid_score += 3
                        flag = False
                        break
                    track[')'][0] -= 1
                    index = track[char][1].pop()
                    to_remove.append(index)
                    to_remove.append(i)
                elif char == '}':
                    if not checkClosing(line, track, char):
                        invalid_score += 1197
                        flag = False
                        break
                    track['}'][0] -= 1
                    index = track[char][1].pop()
                    to_remove.append(index)
                    to_remove.append(i)
                elif char == ']':
                    if not checkClosing(line, track, char):
                        invalid_score += 57
                        flag = False
                        break
                    track[']'][0] -= 1
                    index = track[char][1].pop()
                    to_remove.append(index)
                    to_remove.append(i)
                elif char == '>':
                    if not checkClosing(line, track, char):
                        invalid_score += 25137
                        flag = False
                        break
                    track['>'][0] -= 1
                    index = track[char][1].pop()
                    to_remove.append(index)
                    to_remove.append(i)
            
            if flag:
                for x in sorted(to_remove)[::-1]:
                    copy = copy[:x] + copy[x+1:]
                print(f"Line : {line.strip()}, needs {copy}")
                temp = 0
                print(len(copy))
                print(copy[::-1])
                for letter in copy[::-1]:
                    print(letter)
                    temp = temp * 5 + scores[letter]
                    print(temp)
                incomplete_score.append(temp)


        return invalid_score, incomplete_score


def main():
    invalid_score, incomplete_score = load()
    print(invalid_score)
    print(sorted(incomplete_score)[int(len(incomplete_score)/2)])
        
if __name__ == "__main__":
    main() 