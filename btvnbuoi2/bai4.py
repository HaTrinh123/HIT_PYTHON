n = int(input())
a, b = 0, 1
print(a, end=" ")
for i in range(1, n):
    print(b, end=" ")
    a, b = b, a + b