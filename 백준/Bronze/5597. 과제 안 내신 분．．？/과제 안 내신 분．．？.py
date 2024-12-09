n = [i for i in range(1,31)]
for a in range(28):
    b = int(input())
    n.remove(b)
print(min(n))
print(max(n))