# l=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]

# def spiralOrder(matrix):
#     result = []
#     if not matrix:
#         return result

#     top = 0
#     bottom = len(matrix) - 1
#     left = 0
#     right = len(matrix[0]) - 1

#     while top <= bottom and left <= right:
#         # Left to Right
#         for col in range(left, right + 1):
#             result.append(matrix[top][col])
#         top += 1

#         # Top to Bottom
#         for row in range(top, bottom + 1):
#             result.append(matrix[row][right])
#         right -= 1

#         # Right to Left
#         if top <= bottom:
#             for col in range(right, left - 1, -1):
#                 result.append(matrix[bottom][col])
#             bottom -= 1

#         # Bottom to Top
#         if left <= right:
#             for row in range(bottom, top - 1, -1):
#                 result.append(matrix[row][left])
#             left += 1

#     return result



# print(spiralOrder(l))



l=[1,2,3,4,5]




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
    









