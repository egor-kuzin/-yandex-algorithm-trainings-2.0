import sys
sys.setrecursionlimit(2501)

def find_hight(tree, pr, h):
    ancesor = None
    if pr[0] in tree:
        pr_upper = tree[pr[0]]
        h += 1
        return find_hight(tree, pr_upper, h)
    else:
        if h == 1:
            ancesor = pr[0]
        return h, ancesor


def find_parent(tree, p1, p2):
    pr_upper = tree[p2][0]
    if pr_upper == p1:
        return 1
    elif pr_upper == 0:
        return -1
    else:
        return find_parent(tree, p1, pr_upper)


family_tree = dict()
ans = []

with open("input.txt", "r") as fin:
    n = int(fin.readline().strip())
    for line in range(n - 1):
        child, parent = map(str, fin.readline().split())
        family_tree[child] = [parent]

    for child, parent in family_tree.items():
        h, pr = find_hight(family_tree, parent, 1)
        family_tree[child].extend([h])
        if pr is not None:
            ancesor = pr
    family_tree[ancesor] = [0, 0]

    for line in fin:
        person1, person2 = line.split()
        h1 = family_tree[person1][1]
        h2 = family_tree[person2][1]
        if h1 < h2:
            request = find_parent(family_tree, person1, person2)
            if request == 1:
                ans.append(1)
            elif request == -1:
                ans.append(0)
        elif h1 > h2:
            request = find_parent(family_tree, person2, person1)
            if request == 1:
                ans.append(2)
            elif request == -1:
                ans.append(0)
        else:
            ans.append(0)


print(*ans)