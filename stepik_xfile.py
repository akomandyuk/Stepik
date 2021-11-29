a = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()

# Save the number of strings
strings = len(a)
# Save the number of columns
columns = len(a[0])
print(strings)
print(columns)
new_nested_list = []
c = a.copy()


''' Snippets
topi = a[j - 1][k]
bottomi = a[j + 1][k]
rightj = a[j][k - 1]
leftj = a[j][k + 1]
'''

if strings == 1 and columns == 1:
    a[0][0] = a[0][0] * 4
    new_nested_list.append(a[0][0])

else:
    # We take the 1 string
    for j in range(strings):
        # And check every element of the 1 string
        for k in range(columns):
            a[j][k] = a[j - 1][k] + a[(j + 1) % strings][k] + a[j][k - 1] + a[j][(k + 1) % columns]
            new_nested_list.append(a[j][k])



print(*new_nested_list)
print(a)