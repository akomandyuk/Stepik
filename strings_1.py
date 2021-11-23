# You write a genome sequence
genome = input('')
# We make all the letters in lowercase, so the code will work no matter what the input was
genome = genome.lower()

# symbols 'c' and 'g'
count = 0
# all symbols in a string
length = 0

# for all the letters in 'genome' we check how many 'c' and 'g' are in it
for i in genome:
    if i == 'c' or i == 'g':
        count += 1
    length += 1

print(count)
print(length)
# We print the percentage of 'c' and 'g' in the genome string
print(count / length * 100)
