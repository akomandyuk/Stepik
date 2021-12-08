# The function modifies a list
# It deletes all the odd numbers
# And divides even numbers by 2
def modify_list(lst):
    # Set a variable which is equal to the index of the last element in the list
    # For example: lst = [1, 2, 3 ,4]; 'n' = 3
    n = len(lst) - 1
    # Variable 'm' is the element with index 0 in the list
    m = 0
    # The first cycle for
    # Here we iterate the whole list from the last element to the first one
    # And delete the elements which are odd
    for i in range(n, -1, -1):
        # Check if the number is odd
        if lst[n] % 2 == 1:
            # If it's odd - we delete it
            del lst[n]
        # Check the next element from the end
        # For example: lst = [1, 2, 3 ,4]; 'n' = 3, 'n -= 1' = 2
        n -= 1

    # Second for cycle
    # It's already filtered by the 1st for cycle and doesn't contain any odd numbers
    for j in lst:
        # We check if the number is even
        if lst[m] % 2 == 0:
            # If it's even we divide it by 2
            lst[m] = lst[m] // 2
        # Check the next element from the beginning
        # For example: lst = [1, 2, 3 ,4]; 'm' = 0(in the list it's 1), 'm += 1' = 1(in the list it's 2)
        m += 1
    return lst

# As an example we create a list 'lst'
lst = [6, 6, 6, 6]
# Implement our function
modify_list(lst)
# Print 'lst' to see the result
# The result will be 'lst = [3, 3, 3, 3]'
print(lst)
# Implement our function again, with an updated list 'lst = [3, 3, 3, 3]'
modify_list(lst)
# # The result will be 'lst = []'
print(lst)
