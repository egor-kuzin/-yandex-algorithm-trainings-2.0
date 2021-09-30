nums = list(map(int, input().split()))

def unicum(list_name):
    my_dict = {}
    for i in list_name:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    ans = list(filter(lambda x: my_dict[x] == 1, my_dict.keys()))
    return ans

print(*unicum(nums))
