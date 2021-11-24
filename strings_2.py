a = input('Type your ')

# counter is set to 1 by default. We have at least 1 symbol
count = 1
# index of a symbol
i = 0
# index of a symbol next to 'i'
j = i + 1

# the iterator checks all the symbols
for k in a:
    if j < len(a):
        # if a current symbol is similar to the following one, we add 1 to the counter
        if a[i] == a[j]:
            # we add 1 to the counter
            count += 1
            i += 1
            j += 1
        # if a current symbol IS NOT similar to the following one, we print the number
        # of times we had similar symbols, like 'aaa' = 'a3'
        else:
            print(a[i] + str(count), end = '')
            count = 1
            i += 1
            j += 1
a = a[i] + str(count)
print(a)
