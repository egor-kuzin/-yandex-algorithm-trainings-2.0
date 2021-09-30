with open('input.txt', 'r') as fin:
    ans_dict = {}
    for _ in fin:
        w = _.split()
        for __ in w:
            if ans_dict.get(__):
                ans_dict[__] += 1
            else:
                ans_dict[__] = 1
    del w
    del _
    del __
fin.close()
del fin

x = [(int, str)] * len(ans_dict)
for index, word in enumerate(ans_dict):
    if index < len(ans_dict):
        x[index] = (ans_dict[word], word)
del ans_dict
del index
del word

z = sorted(x, key=lambda k: (-k[0], k[1]))
del x

for _ in z:
    print(_[1])
