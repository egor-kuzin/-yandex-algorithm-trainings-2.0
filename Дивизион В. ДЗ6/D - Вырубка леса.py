with open('input.txt', 'r') as fin:
    a, k, b, m, x = map(int, fin.readline().split())


def check(day):
    return a * (day - day // k) + b * (day - day // m) >= x


def lbs(check):
    l = 0
    r = x
    while l < r:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m + 1
    return l


print(lbs(check))
