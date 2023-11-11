n=int(input())
day=[]
c=0
for i in range(n):
    day.append(list(map(int,input().split())))
for h in day:
    if c<max(h):
        c=max(h)
a=[0]*(c+1)
for j in day:
    for k in range(j[0],j[1]+1):
        a[k]=1
count=0
maxcount=[]
for b in a:
    if b==1:
        count+=1
    else:
        maxcount.append(count)
        count=0
    maxcount.append(count)
print(max(maxcount))