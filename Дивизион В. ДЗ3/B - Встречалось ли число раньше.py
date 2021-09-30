nums = list(map(int, input().split()))

def yes_no(list):
    nums_set = set()
    previous_lenth = 0
    ans = []
    for i in nums:
        previous_lenth = len(nums_set)
        nums_set.add(i)
        if len(nums_set) == previous_lenth:
            ans.append('YES')
        else:
            ans.append('NO')
    return ans

print('\n'.join(yes_no(nums)))
