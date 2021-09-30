PI = 3.1415926535
IN = -1
OUT = 1

with open('input.txt', 'r') as fin:
    n = int(fin.readline().strip())
    i = -1
    events = []
    radii_list = []
    for line in fin:
        i += 1
        r1, r2, f1, f2 = map(float, line.split())
        events.append([f1, IN, i])
        events.append([f2, OUT, i])
        radii_list.append([r1, IN])
        radii_list.append([r2, OUT])

events.sort()
radii_list.sort()

intersections = set()
central_angles = []

for angle, code, i in events:
    if code == IN:
        intersections.add(i)
    if code == OUT:
        if i in intersections:
            intersections.remove(i)

ang_1 = 0
ang_2 = 0

for angle, code, i in events:
    if code == IN:
        intersections.add(i)
        if len(intersections) == n:
            ang_1 = angle
    if code == OUT:
        if len(intersections) == n:
            ang_2 = angle
            central_angles.append(ang_2 - ang_1)
        intersections.remove(i)
if len(intersections) == n:
    central_angles.append(2 * PI - ang_1)
del intersections, events

radius_1 = 0
radius_2 = 0
radius_count = 0
for radius, code in radii_list:
    if code == IN:
        radius_count += 1
        if radius_count == n:
            radius_1 = radius

    if code == OUT:
        if radius_count == n:
            radius_2 = radius
        radius_count -= 1
del radii_list

s = 0
for ca in central_angles:
    if ca != None:
        s += ca * (radius_2 ** 2 - radius_1 ** 2) / 2

print(s)
