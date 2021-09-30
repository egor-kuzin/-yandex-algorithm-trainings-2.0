num = int(input())
pupils_coordinates = list(map(int, input().split()))

if num % 2 != 0:
    medium = int(num // 2)
else:
    medium = int(num / 2)

print(pupils_coordinates[medium])
