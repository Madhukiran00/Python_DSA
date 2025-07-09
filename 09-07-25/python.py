# arr=[1,2,3,4,5,6,7,8]

# n=3
# for i in range(n):
#     print(l)
#     l.insert(0,l[-1])
#     print(l)
#     l.pop()
# print(l)
# i=0
# j=-1
# def reverse(i,j,arr):
#     while i<j:
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1
#         print(arr)
#     return arr

# res_arr=reverse(i,j,arr)
# print(res_arr)






arr=[4,5,6,7,8,1,2,3]

count=0

for j in range(len(arr)-1):
    if arr[j]>arr[j+1]:
        count+=1
        
if arr[len(arr)-1] > arr[0]:
    count+=1
print(count==1)
        
    








