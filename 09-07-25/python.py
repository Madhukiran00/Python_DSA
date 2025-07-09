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
k=4
k=k%len(arr)
def rev_arr(i,j):
    while i<j:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1
rev_arr(0,len(arr)-1)
rev_arr(0,k-1)
rev_arr(k,len(arr)-1)
print(arr)
#Output: [8, 1, 2, 3, 4, 5, 6, 7]
    



        
    








