i, j, year = map(int, input().split())

if i <= 12 and j <= 12 and i != j:
    print(0)
elif i <= 12 and j <= 12 and i == j:
    print(1)
elif i > 12 or j > 12:
    print(1)
else:
    print(0)
