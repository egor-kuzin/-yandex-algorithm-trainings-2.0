with open('input.txt', 'r') as fin:
    fin.readline()
    seq = list(map(int, fin.readline().split()))
    fin.readline()
    orders = list(map(int, fin.readline().split()))


def lbs(x, sequence):
    l = 0
    r = len(sequence)
    while l < r:
        m = (l + r) // 2
        if seq[m] < x:
            l = m + 1
        else:
            r = m
    return l


def rbs(x, sequence):
    l = 0
    r = len(sequence)
    while l < r:
        m = (l + r) // 2
        if seq[m] > x:
            r = m
        else:
            l = m + 1
    return l


seq_set = set(seq)
ans = []

for order in orders:
    if order in seq_set:
        ans.append([lbs(order, seq) + 1, rbs(order, seq)])
    else:
        ans.append([0, 0])

for _ in ans:
    print(*_)
