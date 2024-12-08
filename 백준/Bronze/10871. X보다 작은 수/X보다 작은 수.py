n,v = map(int, input().split())
nlist = list(map(int, input().split()))
for i in range(n):
    if(nlist[i] < v):
        print(nlist[i], end=" ")