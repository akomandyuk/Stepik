def modify_list(lst):
    n = len(lst) - 1
    m = 0
    for i in range(n, -1, -1):
        if lst[n] % 2 == 1:
            del lst[n]
        n -= 1

    for j in lst:
        if lst[m] % 2 == 0:
            lst[m] = lst[m] // 2
        m += 1
    return lst


lst = [6, 6, 6, 6]
modify_list(lst)
print(lst)
modify_list(lst)
print(lst)
