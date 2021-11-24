a = input('')

count = 1
i = 0
j = i + 1

for k in a:
    if j < len(a):
        if a[i] == a[j]:
            count += 1
            i += 1
            j += 1
        else:
            print(a[i] + str(count), end = '')
            count = 1
            i += 1
            j += 1
a = a[i] + str(count)
print(a)
