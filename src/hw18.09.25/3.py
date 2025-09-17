n = int(input())

row = [int(x)for x in range(2, n+1)]



for i in range(0,len(row)-1):
    for j in range(i+1,len(row)):
        if row[i]!=0 and row[j]%row[i]==0:
            row[j]=0


res = [x for x in row if x != 0]

print(res[-1])