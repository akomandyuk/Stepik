# we create a list of numbers
data = list(map(int, input().split()))
# print(data)
# also create a new empty list
new_list = list()
# set a counter
n = 0

# if we have only 1 number in the list, just print this number
if len(data) == 1:
    print(data[0])
# if no, do the following:
else:
    for i in data:
        # if n is the 1st number, add the 2nd and the last
        if n == 0:
            i = data[0 + 1] + data[-1]
        # if n is the last number, add the 1st and number before the last
        elif n == (len(data) - 1):
            i = data[-2] + data[0]
        # if it's in the middle, just add one number before and one number after it
        else:
            i = data[n + 1] + data[n - 1]
        # add these sums to the new list
        new_list.append(i)
        # here we reset the counter to check elements of a list one by one
        n += 1

    # print a new list without brackets
    print(*new_list)
