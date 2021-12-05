# n, m = (int(i) for i in input().split())
n = int(input())
a = [[0 for j in range(n)] for i in range(n)]


# Save the number of strings
# We'll need them when we'll set the sums to the new list
strings = len(a)
# Save the number of columns
columns = len(a[0])
new_nested_list = []
counter = 1

x = 0
y = 1

# Case #1: When n == 1
if strings == 1 and columns == 1:
    a[0][0] = 1
    # print(*a[0])

# Case #2: When 'n' is odd
elif (n % 2) == 1:
    for l in range((n-1) // 2):
        # STEP 1
        # We check the first string only
        for i in range(x, y):
            # Check every element in the first string
            for j in range(x, columns-y):
                a[i][j] = counter
                counter += 1

        # STEP 2
        # We check column with index 4 only
        for j in range(columns-y, columns-x):
            # And check every string from 0 to 4 in column 4
            for i in range(x, strings-y):
                a[i][j] = counter
                counter += 1
            # print(*a[0], end='\n')

        # STEP 3
        # We check the last string only
        for i in range(strings-y, strings-x):
            # And go from the last element to the first one
            for j in range(columns-y, x, -1):
                a[i][j] = counter
                counter += 1
            # print(*a, end='\n')

        # STEP 4
        # Check the first column
        for j in range(x, y):
            for i in range(strings-y, x, -1):
                a[i][j] = counter
                counter += 1
            # print(*a[3], end='\n')

        x += 1
        y += 1


    # STEP 9
    # We check the third string only
    for i in range(x, y):
        # Check every element in the third string
        for j in range(x, columns - x):
            a[i][j] = counter
            counter += 1


# Case #3: When 'n' is even
else:
    for l in range(n // 2):
        # STEP 1
        # We check the first string only
        for i in range(x, y):
            # Check every element in the first string
            for j in range(x, columns-y):
                a[i][j] = counter
                counter += 1

        # STEP 2
        # We check column with index 4 only
        for j in range(columns-y, columns-x):
            # And check every string from 0 to 4 in column 4
            for i in range(x, strings-y):
                a[i][j] = counter
                counter += 1
            # print(*a[0], end='\n')

        # STEP 3
        # We check the last string only
        for i in range(strings-y, strings-x):
            # And go from the last element to the first one
            for j in range(columns-y, x, -1):
                a[i][j] = counter
                counter += 1
            # print(*a, end='\n')

        # STEP 4
        # Check the first column
        for j in range(x, y):
            for i in range(strings-y, x, -1):
                a[i][j] = counter
                counter += 1
            # print(*a[3], end='\n')

        x += 1
        y += 1


'''
# STEP 5
# We check the second string only
for i in range(1, 2):
    # Check every element in the second string
    for j in range(1, columns-2):
        a[i][j] = counter
        counter += 1
    # print(*a, end='\n')

# STEP 6
# Check the column before the last one
for j in range(columns-2, columns-1):
    # Check the all strings from 2nd to the string before the last one
    for i in range(1, strings-2):
        a[i][j] = counter
        counter += 1
    # print(*a, end='\n')

# STEP 7
for i in range(strings-2, strings-1):
    for j in range(columns-2, 1, -1):
        a[i][j] = counter
        counter += 1
    # print(*a, end='\n')

# STEP 8
for j in range(1, 2):
    for i in range(strings-2, 1, -1):
        a[i][j] = counter
        counter += 1
    # print(*a, end='\n')


# STEP 9
# We check the third string only
for i in range(2, 3):
    # Check every element in the third string
    for j in range(2, columns-2):
        a[i][j] = counter
        counter += 1
'''

# x += 1
# y += 1

for k in range(columns):
    print(*a[k], end='\n')








