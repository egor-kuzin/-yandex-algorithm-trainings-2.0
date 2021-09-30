line_repair = input()

reversed_line_repair = ''.join(reversed(line_repair))


def cost(line):
    letters_table = []
    for _ in range(int(len(line_repair) // 2)):
        if list(line_repair)[_] == list(reversed_line_repair)[_]:
            letters_table.append(True)
        else:
            letters_table.append(False)
    return letters_table.count(False)

print(cost(line_repair))
