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
#1752  Check if Array is Sorted and Rotated

'''li=[3,4,5,6,1,2]

c=0
for i in range(len(li)):
    if li[i]>li[(i+1)%(len(li))]:
        c+=1
if c<=1:
    print("True")
else:
    print("False")'''


#------------------------------
#  189- Rotate array k-times

'''li=[1,2,3,4,5,6,7]
k=3
k=k%len(li)

def reverse(i,j):
    while i<j:
        temp=li[i]
        li[i]=li[j]
        li[j]=temp
        i+=1
        j-=1
reverse(0,len(li)-1)
print(li)      #[7, 6, 5, 4, 3, 2, 1]
reverse(0,k-1)
print(li)       #[5, 6, 7, 4, 3, 2, 1]
reverse(k,len(li)-1)
print(li)       #[5, 6, 7, 1, 2, 3, 4]'''
    
#---------------------------------------

# 485-Max Consecutive ones in a list

'''li=[1,0,1,1,0,1,1,1,1,1,0,1,1,1]
c=0
max_count=0

for i in range(len(li)):
    if li[i]==1:
        c+=1
        if c>max_count:
            max_count=c
    else:
        c=0
print(max_count)'''

#--------------------------------------

# 1 Two -sum

# nums=[7,2,11,6,8]
# target=17

'''def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                if nums[i]+nums[j]==target:
                    return i,j
        
obj=two_sum(nums,target)
print(obj)'''
#----------------------------


'''def twosum(nums,target):
    d={}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d[target-nums[i]],i]
        d[nums[i]]=i
    

res=twosum(nums,target)
print(res)'''

#----------------------------------------

# 283 Moves Zeroes

'''nums=[0,1,0,3,12]

j=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[j],nums[i]=nums[i],nums[j]
        j+=1
        
print(nums) #1,3,12,0,0
'''
#------------------------- 
# 125 valid palindrome













