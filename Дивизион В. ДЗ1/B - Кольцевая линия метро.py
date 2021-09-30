n, i, j = map(int, input().split())

if i < j:
    l1 = abs(j - i - 1)
    l2 = abs(i + n - j - 1)
else:
    l1 = abs(i - j - 1)
    l2 = abs(j + n - i - 1)

if l1 < l2:
    print(l1)
else:
    print(l2)
