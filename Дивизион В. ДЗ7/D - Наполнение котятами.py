IN = -1
OUT = 1
CAT = 0
CATS_COUNT = 0

with open('input.txt', 'r') as fin:
    n, m = map(int, fin.readline().split())
    cats = list(map(int, fin.readline().split()))
    events = [] * (2 * m + n)
    segments = [] * m

    i = -1
    for line in fin:
        i += 1
        l, r = map(int, line.split())
        events.append((l, IN, i))
        events.append((r, OUT, i))
        segments.append([l, r, CATS_COUNT])

for cat in cats:
    events.append((cat, CAT, 0))
del cats

events.sort()

for point, code, i in events:
    if code == IN:
        segments[i][2] = CATS_COUNT

    if code == OUT:
        segments[i][2] = CATS_COUNT - segments[i][2]

    if code == CAT:
        CATS_COUNT += 1

del events

print(' '.join([str(_[2]) for _ in segments]))
