H,M = input().split()
h = int(H)
m = int(M)
n = int(input())
sum = m + n
if(sum>=60):
    h = h + int(sum/60)
    m = int(sum%60)
    if(h>=24) : 
        h=h-24
    print(h,m)
else : 
    print(h, sum)