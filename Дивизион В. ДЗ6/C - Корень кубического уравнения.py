import sys

# with open('input.txt', 'r') as fin:
fin = sys.stdin
a, b, c, d = map(int, fin.readline().split())


def lbs(l, r, eps, a, b, c, d, check):
    while l + eps < r:
        m = (l + r) / 2
        # print('l, r', l, r)
        if check(m, a, b, c, d):
            r = m
        else:
            l = m
    return l


def check_up(x, a, b, c, d):
    ev = a * x**3 + b * x**2 + c * x + d
    return ev > 0


def check_down(x, a, b, c, d):
    ev = a * x**3 + b * x**2 + c * x + d
    return ev < 0

l = -10001
r = 10009
eps = 0.00001

if a > 0:
    print(lbs(l, r, eps, a, b, c, d, check_up))
else:
    print(lbs(l, r, eps, a, b, c, d, check_down))
