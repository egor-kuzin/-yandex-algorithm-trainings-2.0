====== Проходит только на PyPy ==========

s = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.pop(0)
b.pop(0)
c.pop(0)

a = [[ai, index] for index, ai in enumerate(a)]
b = [[bi, index] for index, bi in enumerate(b)]


def find_three_sum(list1, list2, orig_list_c):
    c_set = set(orig_list_c)
    ans = []
    ans_finded = False

    for ai in range(0, len(list1)):
        if ans_finded:
            break
        else:
            a0 = list1[ai][0]
            if a0 < s:

                for bi in range(0, len(list2)):
                    ab = list1[ai][0] + list2[bi][0]
                    x = s - ab
                    if x in c_set:
                        y = orig_list_c.index(x)
                        ans.append([list1[ai][1], list2[bi][1], y])
                        ans_finded = True
                        break

    return ans

    
ans = find_three_sum(a, b, c)

print(*ans[0]) if ans else print(-1)
