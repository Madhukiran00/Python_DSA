
# num=2518 #5182
# list=["1534","2518","86","2001"]
# new_list=[]

# res=""
# for j in range(len(list)):
#     new_num=list[j]
#     for i in range(len(new_num)):
#         if int(new_num[i]) % 2 != 0:
#             new_list.append( new_num[i:] + new_num[:i])
#             break
#         elif (len(new_num)-1)==i:
#             new_list.append(new_num)
            
            
# print(new_list)




# s="abcde"
# sub="ec"
# k=0
# for i in range(len(s)):
#     if sub[k]==s[i]:
#         k=k+1
        
# if k==len(sub):
#     print("yes")
# else:
#     print("no")
  

# n = "21582940"
# res = ""
# for i in range(len(n)):
#     if int(n[i]) % 2 != 0:
#         res = n[i:]
#         break
# while int(res)%2==0:
#     res=str(int(res)//10)
# print(res)
    
    
    
# l=[5,4,3,2,1]
# max_num=max(l)
# for i in range(len(l)):
#     if l[-1]==max_num:
#         break
#     else:
#         l.insert(0,l[-1])
#         l.pop()
# print(l)
# c=0
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         c=c+1
# print(c==(len(l)-1))




# l=[5,4,3,2,1]

# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]<l[j]:
#             temp=l[i]
#             l[i]=l[j]
#             l[j]=temp
# print(l)




# temp=l.copy()
# temp.sort()
# print(temp)
# print(l)
# for i in range(len(l)):
    
# res=[]
# ind=(l.index(min(l)))
# res.append(l[ind:])
# res.append(l[:ind])

# print(res)


# l=[1,2,3,4,1,2,3,4]
# new_li=[]
# for i in range(len(l)):
#     if (new_li.index(l[i]))==-1:
#         new_li.append(l[i])
# print(new_li)


l=[2,3,4,5,6,7,8]

for i in range(len(l)):
    for j in range(2,l[i]):
        if  l[i]==2 or l[i]%2!=0 :
            l[i]="True"
            break
        else:
            l[i]="False"
print(l)
            







