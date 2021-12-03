n, m = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]


# Save the number of strings
# We'll need them when we'll set the sums to the new list
strings = len(a)
# Save the number of columns
columns = len(a[0])
new_nested_list = []
counter = 1


for i in range(1):
    new_nested_list = []
    for j in range(columns):
        a[i][j] = counter
        counter += 1
    print(*a[0], end='\n')



