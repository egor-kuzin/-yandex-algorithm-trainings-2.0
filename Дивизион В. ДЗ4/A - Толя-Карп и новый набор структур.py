with open('input.txt', 'r') as fin:
    num = int(fin.readline().strip())
    ans_dict = {} # {_: 0 for _ in range(num)}
    for _ in fin:
        a, d = map(int, _.split())
        if ans_dict.get(a):
            ans_dict[a] += d
        else:
            ans_dict[a] = d

for _ in sorted(ans_dict.items()):
    print(*_)