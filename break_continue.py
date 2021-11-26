a = 0

# If a number > 100 we stop reading numbers
while a <=100:
    # We type a number
    a = int(input('Type your number: '))
    # If a number < 10, we skip it
    if a < 10:
        continue
    # If a number > 100, we end the cycle
    if a > 100:
        break
    print(a)
