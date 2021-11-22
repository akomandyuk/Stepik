from typing import List

a = [int(i) for i in input().split()]

new_list: List[int] = []
n = 0

a.sort()
# print(a)


if len(a) == 1:
    print('')

else:
    for i in a:
        if n == (len(a) - 1):
            pass
        elif n == (len(a) - 2):
            if i == a[n + 1]:
                new_list.append(i)
        elif i == a[n + 1] and a[n + 1] != a[n + 2]:
            new_list.append(i)
        n += 1
    print(*new_list)
