with open('input.txt', 'r') as fin:
    fin.readline()
    seq = list(map(int, fin.readline().split()))
    orders_num = int(fin.readline().strip())
    orders = []
    for line in range(orders_num):
        l, r = map(int, fin.readline().split())
        orders.append([l, r])

seq.sort()

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


ans = []

for order in orders:
    ans.append(rbs(order[1], seq) - lbs(order[0], seq))

print(*ans)