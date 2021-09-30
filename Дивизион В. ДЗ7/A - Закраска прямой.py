'''

-1: начало отрезка
 1: конец отрезка

'''


with open('input.txt', 'r') as fin:
    n = int(fin.readline().strip())
    events = [] * 2 * n

    for segment in fin:
        li, ri = map(int, segment.split())
        events.append([li, -1])
        events.append([ri, 1])

events.sort()

prefsum = 0
sums = 0

starts_count = 0
start = 0
ends_count = 0
end = 0

for point, code in events:
    prefsum += code
    if code == -1:
        starts_count += 1
        if starts_count == 1:
            start = point
    if code == 1:
        ends_count += 1
        end = point
    if prefsum == 0:
        sums += end - start
        starts_count = 0

print(sums)
