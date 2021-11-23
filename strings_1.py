genome = input('')
genome = genome.lower()

# symbols 'c' and 'g'
count = 0
# all symbols in a string
length = 0

for i in genome:
    if i == 'c' or i == 'g':
        count += 1
    length += 1

#print(count)
#print(length)
print(count / length * 100)
