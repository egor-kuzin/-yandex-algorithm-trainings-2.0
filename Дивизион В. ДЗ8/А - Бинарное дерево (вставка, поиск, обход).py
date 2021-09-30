def find(root, x):
    if not root:
        print("NO")
        return
    key = root[0]
    if key == x:
        print("YES")
        return
    elif x < key:
        left = root[1]
        if not left:
            print("NO")
            return
        else:
            return find(left, x)
    elif x > key:
        right = root[2]
        if not right:
            print("NO")
            return
        else:
            return find(right, x)


def add(root, x):
    if not root:
        root.extend([x, None, None])
        print("DONE")
        return
    key = root[0]
    if key == x:
        print("ALREADY")
    if x < key:
        left = root[1]
        if not left:
            root[1] = [x, None, None]
            print("DONE")
        else:
            add(left, x)
    elif x > key:
        right = root[2]
        if not right:
            root[2] = [x, None, None]
            print("DONE")
        else:
            add(right, x)


def print_tree(root, depth=0):
    if not root:
        return
    if root[1]:
        print_tree(root[1], depth + 1)
    print(f"{''.join('.' * depth)}{root[0]}")
    if root[2]:
        print_tree(root[2], depth + 1)


bin_tree = []

with open("input.txt", "r") as fin:
    n = None
    for line in fin:
        line = line.split()
        if len(line) == 1:
            command = line[0]
            n = None
        elif len(line) == 2:
            command = line[0]
            n = int(line[1])

        if command == 'ADD':
            add(bin_tree, n)

        if command == 'SEARCH':
            find(bin_tree, n)

        if command == 'PRINTTREE':
            print_tree(bin_tree)
