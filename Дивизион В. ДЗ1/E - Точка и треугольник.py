d = int(input())
a, b = map(int, input().split())

# y = - x + d
# OA = (d, 0)
# OB - (0, d)
# X = (x, y)
# AX = (x - d, y) => sqr( (x-d)**2 + y**2 )
# BX = (x, y - d) => sqr( x**2 + (y-d)**2 )

if 0 <= a <= d and 0 <= b <= -a + d:
    print(0)
else:
    mod = ( a**2 + b**2 )**(0.5)
    ax = ( (a-d)**2 + b**2 )**(0.5)
    bx = ( a**2 + (b-d)**2 )**(0.5)
    if min(mod, ax, bx) == mod:
        print(1)
    elif min(mod, ax, bx) == ax:
        print(2)
    elif min(mod, ax, bx) == bx:
        print(3)

