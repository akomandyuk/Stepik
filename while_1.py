# We set a sum variable
sum = 0
# We set a variable where we type numbers
a = int(input('Type your number: '))
# The cycle works until we type '0'
while a != 0:
    # In case we don't write '0' we add our number to 'sum' variable
    sum += a
    # Then we type our number again
    a = int(input('Type your number: '))
# When the cycle is over we print the total sum
print(sum)