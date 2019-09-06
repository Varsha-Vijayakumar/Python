n=int(input())
k=int(input())
lis=[]
count=0
for i in range(0,n):
    a=int(input())
    lis.append(a)
for i in range(0,len(lis)):
    if(lis[i] is k):
        count=count+1
print(count)
