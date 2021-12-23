import copy

def load():
    tree = {}
    with open("../file.txt", 'r') as file:
        for line in file:
            words = line.strip().split("-")
            if words[0] in tree:
                tree[words[0]].append(words[1])
            else:
                tree[words[0]] = [0,words[1]]
            if words[1] in tree:
                tree[words[1]].append(words[0])
            else:
                tree[words[1]] = [0,words[0]]
    return tree

def getPaths(twice, tree, key, path):
    if key == 'end':
        return 1
    if key.islower() and tree[key][0]>1:
        return 0
    if key.islower() and tree[key][0]==1:
        if key == 'start':
            return 0
        elif not twice:
            twice = True
        else:
            return 0
    paths = 0
    tree[key][0] += 1
    for node in tree[key][1:]:
        paths += getPaths(twice, copy.deepcopy(tree), node, f"{path} -> {node}")
    return paths



def main():
    tree = load()
    count = getPaths(False, tree, 'start', "start")

    print(count)
        
if __name__ == "__main__":
    main() 