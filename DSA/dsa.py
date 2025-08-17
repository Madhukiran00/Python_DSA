#list reverse
lis=[8,7,6,5,4,3,2,1]
i=0
j=len(lis)-1
while i<j:
    temp=lis[i]
    lis[i]=lis[j]
    lis[j]=temp
    i+=1
    j-=1
print(lis)

#---------------------------------
# Leetcode =26

# Remove duplicates from an sorted array


