from typing import List
# We set a list of numbers
a = [int(i) for i in input().split()]
# We also set a new empty list where we will add numbers
# That were found in list 'a' more than once
new_list: List[int] = []
# Set the counter which will be equal to the indices in list 'a'
n = 0

a.sort()
# print(a)

# If the list has only one element, we print ''
if len(a) == 1:
    print('')

else:
    # Check every element of our list
    for i in a:
        if n == (len(a) - 1):
            pass
        elif n == (len(a) - 2):
            # If element 'i' is the same as the one next to him
            if i == a[n + 1]:
                # Add element with index 'i' to the new list
                new_list.append(i)
        # If element 'i' is the same as the one next to him and 'next to i' is not the same as 'next to that element'
        # Also add element with index 'i' to the new list
        elif i == a[n + 1] and a[n + 1] != a[n + 2]:
            new_list.append(i)
        n += 1
    print(*new_list)
