s =input()
wrd=list(s)
lis=[]
for i in range(0,len(wrd)):
    if(i%2==0):
        x=wrd[i]
    elif(i%2!=0):
        y=wrd[i]
        lis.append(y)
        lis.append(x)
if(len(wrd)%2!=0):
    lis.append(x)
for i in lis:
    print(i, end="")
