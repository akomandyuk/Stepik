# We create a list of integers
l = [int(i) for i in input('Enter your numbers: ').split()]
# Create an integer
n = int(input('Type your number: '))
counter = 0
# A new list where we will put the indices of number n in list l
new_list = []


# Create a loop which will check all the integers from the list l
for i in l:
    counter += 1
    # If integer n not in the list l just print this phrase
    if n not in l:
        print('No such number')
        break
    # if the integer from the list l matches our integer n, we add the index of this integer to a new list
    if l[counter - 1] == n:
        new_list.append(counter - 1)


# Shows the list of indices of the numbers from list l which are equal to n
print(*new_list)