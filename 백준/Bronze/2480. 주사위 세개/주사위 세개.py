A,B,C = input().split()
a = int(A)
b = int(B)
c = int(C)
if(a==b==c) : 
    print(10000+a*1000)
elif((a==b and b!=c) or (c==b and a!=b) or (a==c and b!=c)):
    if(a==b):
        print(1000+a*100)
    if(c==b):
        print(1000+b*100)
    if(a==c):
        print(1000+c*100)
else : 
    print(max(a,b,c)*100)