n5=input()
n5=list(n5)
x=[]
for i in range(0,len(n5),2):
  x.append(n5[i+1])
  x.append(n5[i])
res="".join(x)
print(res)
