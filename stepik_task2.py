# We enter some integer
number = int(input('Type your number: '))
# Set a counter
n = 0

# We set a loop and check all the numbers in range from 1 to 'number'
for i in range(1, number + 1):
    # a condition to finish the loop when counter n = our number
    # For example: number = 7; We will have 7 characters in our final string: 1 2 2 3 3 3 4
    if n == number:
        break
    # We set a second loop and print number 'i' a number of times from 1 to 'i + 1'
    # for example: i = 4; here we will type '4' four times: 4 4 4 4
    for num in range(1, i + 1):
        # a condition to finish the loop when counter n = our number
        # here if n = number, we will break from this loop to the upper one,
        # so we will not print unnecessary numbers
        # For example: number = 7; when n = 7, we will not continue printing
        # and just will move upper
        if n == number:
            break
        # here we print number 'i', a number of times in range from 1 to 'i + 1'
        # for example: i = 4; here we will type '4' four times: 4 4 4 4
        print(i, end=' ')
        # Makes our counter 1 point bigger
        n += 1

# Just moves the cursor from the end of the line to the next line
print()
