dict = {}

for i in range(10000):
    x = int(input())
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1
    if x == 0:
        break
print(dict[max(dict)])
