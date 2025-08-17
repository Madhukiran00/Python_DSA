# sec_max in a lis
'''
l=[3,5,6,7,83,5,7]

max=0
sec_max=0
for i in range(len(l)):
    if l[i]>max:
        sec_max=max
        max=l[i]
    elif l[i]<max and l[i]>sec_max:
        sec_max=l[i]
print(sec_max)'''

#----------------------------------
# Kth max element 
   
'''l = [3, 5, 6, 7, 83, 5, 7]
k = 3   # 3rd max
unique = list(set(l))  # keep distinct elements

max_list = []

for _ in range(k):
    m = max(unique)
    max_list.append(m)
    unique.remove(m)

print(f"{k}th max:", max_list[-1])'''

#---------------------------------

#list reverse
'''lis=[8,7,6,5,4,3,2,1]
i=0
j=len(lis)-1
while i<j:
    temp=lis[i]
    lis[i]=lis[j]
    lis[j]=temp
    i+=1
    j-=1
print(lis)'''

#---------------------------------
# Leetcode =26

# Remove duplicates from an sorted array

'''lis=[1,2,2,3,4,4,4,6,7,7]
i=0
for j in range(1,len(lis)):
    if lis[i]!=lis[j]:
        lis[i+1]=lis[j]
        i+=1
print(lis[:i+1])'''

#print the number of unique elements
# print(i)
#-------------------------------------

# Leetcode:- 1796. Second Largest Digit in a String

'''s="sdgdf3hkk6lj9ljl34"

max=-1
sec_max=-1

for i in range(len(s)):
    if s[i].isdigit():
        if int(s[i])>max:
            sec_max=max
            max=int(s[i])
        if int(s[i])>sec_max and int(s[i])<max:
            sec_max=int(s[i])'''
            
# print(sec_max)

#-------------------------------------
    






