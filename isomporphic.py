a1,a2=map(str,input().split())
for i in a1:
    f=a1.count(i)
for j in a2:
    u=a2.count(j)
if(f==u):
    print("yes")
else:
    print("no")
