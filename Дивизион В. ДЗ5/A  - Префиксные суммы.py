orders_list = []

with open('input.txt', 'r', encoding='utf-8') as fin:
    n, q = map(int, fin.readline().split())
    in_list = list(map(int, fin.readline().split()))
    for _ in fin:
        orders_list.append(list(map(int, _.split())))
fin.close()
del fin

prefixsums = [0] * (n+1)

for _ in range(len(in_list)+1):
    if _ == 0:
        prefixsums[0] = 0
    else:
        prefixsums[_] = in_list[_-1] + prefixsums[_-1]


def sum_count(list, l, r):
    return list[r] - list[l-1]

for _ in orders_list:
    print(sum_count(prefixsums, _[0], _[1]))
