with open('input.txt', 'r') as fin:
    sequence = list(fin.readline().strip())
del fin


for _, symbol in enumerate(sequence):
    if symbol == '(':
        sequence[_] = 1
    elif symbol == ')':
        sequence[_] = -1
del symbol

trg = None
prefixsums = [0] * (len(sequence)+1)
for _ in range(len(sequence)+1):
    if _ == 0:
        prefixsums[0] = 0
    else:
        prefixsums[_] = sequence[_-1] + prefixsums[_-1]
        if prefixsums[_] < 0:
            trg = False
        elif prefixsums[_] > 0:
            trg = True

print('YES') if trg and prefixsums[-1] == 0 else print('NO')
