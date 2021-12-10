# Create an empty dictionary
dct = {}
# Enter a number
# Below there will be n lines with some single numbers
n = int(input())
# We will input number x n times
# For example, we are going to input number x 5 times if n = 5
for i in range(n):
    x = int(input())

    def f(x):
        return x + 1
    # Still go through every key in the dict
    if x in dct.keys():
        # If there's such a key just print it
        print(dct[x])
    # If there's no such key, add it to the dictionary and give it value = 'f(x)'
    # For example: if key 'x' = 5, value 'f(x)' = 6
    elif x not in dct.keys():
        dct[x] = f(x)
        # Print the key
        print(dct[x])



