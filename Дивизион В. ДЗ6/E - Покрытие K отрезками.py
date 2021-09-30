'''
Составляем список длин для полученных точек.
Бинпоиском берем длину и проверяем можно ли разбить набор точек на заданное количество отрезков.
'''


with open('input.txt', 'r') as fin:
    k = list(map(int, fin.readline().split()))[1]
    seq = list(map(int, fin.readline().split()))


def check_for_segments(sequence, m):
    count = 1
    current_distance = sequence[0]
    for distance in sequence:
        current_segment = distance - current_distance
        if current_segment > m:
            current_distance = distance
            count += 1
            if count > k:
                return False
    return count <= k


def lbs(sequence, check):
    l = 0
    r = sequence[-1]
    while l < r:
        m = (l + r) // 2
        if check(sequence, m):
            r = m
        else:
            l = m + 1
    return l


seq.sort()

all_distances_list = [value - seq[0] for value in seq]

print(lbs(all_distances_list, check_for_segments))
