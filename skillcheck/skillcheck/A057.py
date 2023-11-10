n=int(input())
A=[]
for k in range(n):
    A.append(list(map(int,list(input()))))
count0=1
maxcount0=[]
for i in range(n):
    for j in range(n):
        if j>0:
            if (A[i][j])==(A[i][j-1]+1):
                count0+=1
            else:
                maxcount0.append(count0)
                count0=1
    maxcount0.append(count0)
    count0=1

count2=1
maxcount2=[]
for i in range(n):
    for j in range(n):
        if j>0:
            if (A[j][i])==(A[j-1][i]+1):
                count2+=1
            else:
                maxcount2.append(count2)
                count2=1
    maxcount2.append(count2)
    count2=1


count1=1
maxcount1=[]
for i in range(n):
    for j in range(n):
        if j>0:
            if (A[i][j]+1)==(A[i][j-1]):
                count1+=1
            else:
                maxcount1.append(count1)
                count1=1
    maxcount1.append(count1)
    count1=1


count3=1
maxcount3=[]
for i in range(n):
    for j in range(n):
        if j>0:
            if (A[j][i]+1)==(A[j-1][i]):
                count3+=1
            else:
                maxcount3.append(count3)
                count3=1
    maxcount3.append(count3)
    count3=1


count4=1
maxcount4=[]
x=0
for i in range(n-1):
    for j in range(n):
        if x+j<n and i+j<n and x+j-1>=0 and i+j-1>=0:
            if (A[x+j][i+j]+1)==(A[x+j-1][i+j-1]):
                count4+=1
            else:
                maxcount4.append(count4)
                count4=1
    maxcount4.append(count4)
    count4=1


count6=1
maxcount6=[]
x=0
for i in range(n-1):
    for j in range(n):
        if x+j<n and i+j<n and x+j-1>=0 and i+j-1>=0:
            if (A[x+j][i+j])==(A[x+j-1][i+j-1]+1):
                count6+=1
            else:
                maxcount6.append(count6)
                count6=1
    maxcount6.append(count6)
    count6=1


count5=1
maxcount5=[]
x=0
for i in range(n-1):
    for j in range(n):
        if x+j<n and i+j<n and i+j-1>=0 and x+j-1>=0:
            if (A[i+j][x+j]+1)==(A[i+j-1][x+j-1]):
                count5+=1
            else:
                maxcount5.append(count5)
                count5=1
    maxcount5.append(count5)
    count5=1


count7=1
maxcount7=[]
x=0
for i in range(n-1):
    for j in range(n):
        if x+j<n and i+j<n  and i+j-1>=0 and x+j-1>=0:
            if (A[i+j][x+j]+1)==(A[i+j-1][x+j-1]):
                count7+=1
            else:
                maxcount7.append(count7)
                count7=1
    maxcount7.append(count7)
    count7=1

maxcount=maxcount0+maxcount1+maxcount2+maxcount3+maxcount4+maxcount5+maxcount6+maxcount7
print(max(maxcount))