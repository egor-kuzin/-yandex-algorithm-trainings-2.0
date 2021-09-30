plate = list(map(int, input().split()))
blocks = list(map(int, input().split()))

medium = plate[0] / 2

my_dict = {x: (- medium + x + 0.5) for x in blocks}

if plate[0] % 2 != 0 and int(medium - 0.5) in blocks:
    print(int(medium - 0.5))
else:
    left = dict(filter(lambda x: x[1] < 0, my_dict.items()))
    right = dict(filter(lambda x: x[1] > 0, my_dict.items()))
    max_left = max(left, key=lambda k: left[k])
    min_right = min(right, key=lambda k: right[k])
    print(max_left, min_right)
