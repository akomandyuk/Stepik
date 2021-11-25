# The first integer
a = int(input())
# The second integer
b = int(input())
# Sum of the numbers between 'a' and 'b' that are divided by 3
s = 0
# Amount of the numbers between 'a' and 'b' that are divided by 3
n = 0
# Their average
average = 0


# Check all the numbers between 'a' and 'b'
for i in range(a, b + 1):
    # If a number is divided by 3, add this number to the sum 's'
    # And add 1 to their amount 'n'
    if i % 3 == 0:
        # print(i)
        s += i
        n += 1
# We calculate their average
print(s / n)