# 1796

# s="dfa1234678"
# l=[]
# c=0
# for i in range(len(s)):
#     if s[i].isdigit():
#         l.append(int(s[i]))
# l.sort()
# new_li=[]
# for j in range(len(l)):
    
#     if l[j] not in new_li:
#         new_li.append(int(l[j]))
# if len(new_li)==1 or len(new_li)==0:
#     c=1
# # print(l)
# # print(new_li)
# if c==1:
#     print(-1)
# else:
#     print(new_li[-2])


# l=[1,1,2,2,2,3,3,4,9,9]
# count=0
# for i in range(len(l)):
#     if l.count(l[i])==1:
#         print(l[i])



 
# s="abc1234431def"
# max=-1
# se_max=-1

# for i in range(len(s)):
#     if s[i].isdigit():
#         if int(s[i])>max:
#             se_max=max
#             max=int(s[i])
#         elif int(s[i])>se_max and int(s[i])<max:
#             se_max=int(s[i])
# print(se_max)

        
# l=[1,1,2,2,2,3,3]

# j=0
# for i in range(1,len(l)):
#     if l[i]!=l[j]:
#         l[j+1]=l[i]
#         j+=1
# print(j+1)
    

l=[2,7,11,15]
# j=0
# target=18
# for i in range(1,len(l)):
#     if int(l[i])+int(l[j])==target:
#         print(j,i)
#     else:
#         j+=1

    
# x=-121
# n=x
# r=0
# while n!=0:
#     rem=n%10
#     r=r*10+rem
#     n=n//10
# print( (r==x))

dic={'}':'{',')':'(',']':'['}

s="{[(]}"

l=[]
for i in range(len(s)):
    if s[i] in "{[(":
        l.append(s[i])
    elif s[i] in "}])":
        if l[-1]==dic[s[i]]:
            l.pop()
            
    
print(len(l)==0)
        
    

