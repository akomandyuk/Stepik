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


if strings == 1 and columns == 1:
    a[0][0] = a[0][0] * 4
    new_nested_list.append(a[0][0])

print(*new_nested_list)
print(a)