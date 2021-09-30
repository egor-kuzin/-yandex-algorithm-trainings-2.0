with open('input.txt', 'r') as fin:
    witnesses = int(fin.readline().strip())
    testimony = []
    for _, __ in enumerate(fin):
        if _ < witnesses:
            testimony.append(__.strip())
        else:
            plates = int(__)
            break
    plate = {_: [0, 0] for _ in range(plates)}
    for _, __ in enumerate(fin):
        plate[_][0] = __.strip()

for _ in testimony:
    for index, value in enumerate(plate.values()):
        if index < plates:
            q = set(_)
            w = set(value[0])
            e = set(value[0]).isdisjoint(set(_))
            r = set(value[0]).intersection(set(_))
            if len(set(value[0]).intersection(set(_))) == len(set(_)):
                plate[index][1] += 1

a = max([plate[_][1] for _ in plate])

for _ in plate:
    if plate[_][1] == a:
        print(plate[_][0])
