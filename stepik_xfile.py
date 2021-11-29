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




print(a)