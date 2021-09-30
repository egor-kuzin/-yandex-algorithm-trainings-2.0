INP = -1
OUT = 1
ZERO = 0


with open('input.txt', 'r') as fin:
    m = int(fin.readline().strip())
    segments = []

    li, ri = map(int, fin.readline().split())

    while li != 0 or ri != 0:
        segments.append((li, INP, (li, ri)))
        segments.append((ri, OUT, (li, ri)))
        li, ri = map(int, fin.readline().split())

segments.append((0, ZERO, (0, 0)))
segments.append((m, ZERO, (0, m)))
segments.sort()

ans = set()
concurrent_events = set()
control_point = 0
is_no_solution = False

for point, code, segment in segments:

    if code == INP:
        concurrent_events.add(segment)

    if code == OUT:
        if segment in concurrent_events:
            concurrent_events.remove(segment)
        if point == control_point:
            if concurrent_events:
                max_segment = max(concurrent_events, key=lambda x: x[1])
                control_point = max_segment[1]
                if not max_segment in ans:
                    ans.add(max_segment)

    if code == ZERO and point == 0:
        if concurrent_events:
            max_segment = max(concurrent_events, key=lambda x: x[1])
            control_point = max_segment[1]
            if not max_segment in ans:
                ans.add(max_segment)

    if control_point >= m:
        is_no_solution = True
        break

if not concurrent_events:
    print('No solution')
else:
    print(len(ans))
    [print(*_) for _ in sorted(ans)]
