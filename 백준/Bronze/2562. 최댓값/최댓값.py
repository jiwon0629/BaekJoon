arr=[0]*9
for i in range (9):
    arr[i] = int(input())
print(max(arr))
for b in range (9):
    if(max(arr)==arr[b]):
        print(b+1)
