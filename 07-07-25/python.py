
l=[1,2,3,4,5]
res=[]
for i in range(len(l)-1,-1,-1):
    res.append(l[i])

print(res)
#Output:[5,4,3,2,1]
#-------------------------------------
l=[1,2,3,4,5]
i=0
j=len(l)-1
while i<j:
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    i+=1
    j-=1
print(l)
#Output:[5,4,3,2,1]
#-------------------------------------
l=[1,2,3,4,5]
i=0
j=len(l)-1
while i<j:
    l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
print(l)
#Output:[5,4,3,2,1]










