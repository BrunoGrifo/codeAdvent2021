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
        final_string = 0
        for line in file:
            print(line.strip())
            track = {')': [0,[]], '}': [0,[]], ']': [0,[]], '>': [0,[]]}
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
                        print("found")
                        final_string += 3
                        break
                    track[')'][0] -= 1
                    track[char][1].pop()
                elif char == '}':
                    if not checkClosing(line, track, char):
                        final_string += 1197
                        print("found")
                        break
                    track['}'][0] -= 1
                    track[char][1].pop()
                elif char == ']':
                    if not checkClosing(line, track, char):
                        final_string += 57
                        print("found")
                        break
                    track[']'][0] -= 1
                    track[char][1].pop()
                else:
                    if not checkClosing(line, track, char):
                        final_string += 25137
                        print("found")
                        break
                    track['>'][0] -= 1
                    track[char][1].pop()

        return final_string


def main():
    result = load()
    print(result)
        
if __name__ == "__main__":
    main() 