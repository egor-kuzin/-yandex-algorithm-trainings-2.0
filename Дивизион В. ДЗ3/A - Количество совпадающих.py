list_first = list(map(int, input().split()))
list_second = list(map(int, input().split()))

set_1 = set(list_first)
set_2 = set(list_second)

set_comm = set_1.intersection(set_2)

print(len(set_comm))
