'''

 1: прибытие груза
 -1: окончание обработки

'''


with open('input.txt', 'r') as fin:
    n = int(fin.readline().strip())
    events = [] * 2 * n

    for line in fin:
        time_arrival, test_length = map(int, line.split())
        events.append([time_arrival, 1])
        events.append([time_arrival + test_length, -1])

events.sort()

max_divices = 0
cargo = 0

for time, code in events:
    if code == -1:
        cargo -= 1
    if code == 1:
        cargo += 1
    max_divices = max(max_divices, cargo)

print(max_divices)
