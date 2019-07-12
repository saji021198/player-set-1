n1,k=map(str,input().split())
n1=list(n1)
k=list(k)
count=0
for i in range(0,len(n1)):
        if(n1[i]!=k[i]):
            count=count+1
if(count==1):
    print("yes")
else:
    print("no")
        
