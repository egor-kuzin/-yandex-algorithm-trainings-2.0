folders_num = input()
files_num = list(map(int, input().split()))

ans = sum(files_num) - max(files_num)

print(ans)