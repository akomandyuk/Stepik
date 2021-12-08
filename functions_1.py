# Create a function
# Depending on the number the function will give different outputs
# which are written below
def f(x):
    if x <= -2:
        return 1 - ((x + 2) ** 2)
    elif 2 >= x > -2:
        return -x / 2
    else:
        return ((x - 2) ** 2) + 1

# As an example we create a variable 'a' with number 1
a = f(1)
print(a)