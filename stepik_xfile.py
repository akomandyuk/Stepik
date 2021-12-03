# Set the first list of integers
# Like a = [1, 2, 3]
a = [[int(i) for i in input().split()]]
# Set a string
# Like 4 5 6
b = input()
# The cycle will work unless we write 'end' in the 'b' string
while b != 'end':
    # Transform 'b' string into a list and add it to 'a' list
    # So we'll have a = [[1, 2, 3], [4, 5, 6]]
    a.append([int(i) for i in b.split()])
    # Set a 'b' string once again
    b = input()

# Save the number of strings
# We'll need them when we'll set the sums to the new list
strings = len(a)
# Save the number of columns
columns = len(a[0])
new_nested_list = []


''' Snippets
topi = a[j - 1][k]
bottomi = a[j + 1][k]
rightj = a[j][k - 1]
leftj = a[j][k + 1]
'''

if strings == 1 and columns == 1:
    a[0][0] = a[0][0] * 4
    new_nested_list.append(a[0][0])
    print(*new_nested_list)

else:
    # We take the 1st string
    for j in range(strings):
        # Set the new list to empty
        new_nested_list = []
        # Set variable m to zero
        m = 0
        # And check every element of the 1 string
        for k in range(columns):
            # We set the sum of a current number (a[j][k]) in a nested list to the variable 'm'
            m = a[j - 1][k] + a[(j + 1) % strings][k] + a[j][k - 1] + a[j][(k + 1) % columns]
            # We add 'm' to a new list
            # The last operation of the inner cycle
            new_nested_list.append(m)
        # The outer cycle continues
        # We print a new list (elements of one string only)
        # end='\n' means we move to the next line
        print(*new_nested_list, end='\n')

