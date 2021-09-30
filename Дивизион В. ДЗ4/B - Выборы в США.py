with open('input.txt', 'r') as fin:
    ans_dict = {}
    for _ in fin:
        a, d = _.split()
        d = int(d)
        if ans_dict.get(a):
            ans_dict[a] += d
        else:
            ans_dict[a] = d

for _ in sorted(ans_dict.items()):
    print(*_)
