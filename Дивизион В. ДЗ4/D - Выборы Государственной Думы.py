with open('input.txt', 'r') as fin:
    ans_dict = {}
    for _ in fin:
        splited_line = _.split()
        voices = int(splited_line.pop())
        party = ' '.join(splited_line)
        ans_dict[party] = [voices, 0, 0]
    del splited_line
    del voices
    del party
    del _
fin.close()
del fin

main_div = 0
for _ in ans_dict.values():
    main_div += _[0]
main_div = main_div / 450


x = 0
for _ in ans_dict:
    __ = ans_dict[_][0] / main_div
    ans_dict[_][1] = int(__)
    ans_dict[_][2] = __ - ans_dict[_][1]
    x += ans_dict[_][1]
del _
del __
del main_div

t = []
for _ in ans_dict:
    t.append((_, ans_dict[_][2]))

s = sorted(t, key=lambda k: -k[1])
del t

j = 450 - x
for _, add_pos in enumerate(s):
    if j > 0 and j + x <= 450:
        ans_dict[add_pos[0]][1] += 1
        j -= 1
del j
del _
del add_pos
del s
del x

for _ in ans_dict:
    print(_, ans_dict[_][1])
