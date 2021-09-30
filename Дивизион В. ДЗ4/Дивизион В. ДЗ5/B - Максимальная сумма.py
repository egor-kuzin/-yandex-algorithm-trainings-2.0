with open('input.txt', 'r') as fin:
    n = int(fin.readline().strip())
    in_list = list(map(int, fin.readline().split()))

ans = 0
current_sum = 0
max_value = in_list[0]
count_minus_values = 0
for value in in_list:
    max_value = max(max_value, value)
    current_sum += value
    ans = max(ans, current_sum)
    if value >= 0:
        ans = max(ans, current_sum, max_value)
    else:
        current_sum = max(current_sum, 0)
        count_minus_values += 1

if count_minus_values == len(in_list):
    ans = max_value

print(ans)
