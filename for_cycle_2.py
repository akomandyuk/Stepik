a = int(input())
b = int(input())
s = 0
n = 0
average = 0



for i in range(a, b + 1):
    if i % 3 == 0:
        #print(i)
        s += i
        n += 1
print(s / n)