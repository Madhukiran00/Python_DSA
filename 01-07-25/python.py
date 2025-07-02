# #1) Diagonal Elements

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# def dig_ele(mat):
#     res=""
#     for i in range(len(mat)):
#         res+=str(mat[i][i])
    
#     return res
# print(dig_ele(mat))

# #Output:
# #   1 5 9
# #---------------------------------------------
# # 2) Anti-Diagonal Elements

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(0,len(mat)):
#     print(mat[i][len(mat)-i-1],end=" ")

# #Output:
# #   3 5 7

# #-------------------------------------------------

# #3)Non -Diagonal

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# def non_diag(mat):
#     res=""
#     for i in range(len(mat)):
#         for j in range(len(mat)):
#             if mat[i][j]!=mat[i][i]:
#                 res+=str(mat[i][j])
#     return res

# print(non_diag(mat))

# #Output: 234678

# #----------------------------------------------

# #4)Non-Anti=Diag
# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# def nan_a_dig(mat):
#     res=""
#     for i in range(len(mat)):
#         for j in range(len(mat)):
#             if mat[i][len(mat)-i-1]!=mat[i][j]:
#                 res+=str(mat[i][j])
#     return res
# print(nan_a_dig(mat))

# #Output:
# #   1 2 4 6 8 9
# #------------------------------------------------
# #5) a)

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(len(mat)):
#     mat[i][len(mat)-i-1]=0
    
# for i in range(len(mat)):
#     for j in range(len(mat)):
#         print(mat[i][j],end=" ")
#     print("")
# #Output:
# #   1 2 0 
# #   4 0 6 
# #   0 8 9 
   
# #-----------------------------------------------
# # 5) b)
# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(len(mat)):
#     mat[i][i]=0
    
# for i in range(len(mat)):
#     for j in range(len(mat)):
#         print(mat[i][j],end=" ")
#     print("")
# #Output:
# #   0 2 3 
# #   4 0 6 
# #   7 8 0 
# #--------------------------------------------------
       
# # 6) 

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(len(mat)):
#     # print(mat[i][i:len(mat)])
    
#     for j in range(i,len(mat)):
#          print(mat[i][j],end=" ")

# #Output:
# #    1 2 3 5 6 9
# #-----------------------------------------------------

# # 7) 

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(len(mat)):
#     for j in range(i+1):
#         print(mat[i][j],end=" ")
    
# #Output:
# #   1 4 5 7 8 9  
# #----------------------------   
# # 8)
    
# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(len(mat)):
#     for j in range(len(mat)):
#         print(mat[j][i],end=" ")
#     print("")

# #Output:
# #   1 4 7 
# #   2 5 8 
# #   3 6 9 

# #----------------------------------

# # 9)Transpose

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(len(mat)):
#     for j in range(len(mat)):
#         print((mat[i][j])*2,end=" ")
#     print("")

# #Output:
# #   2  4  6 
# #   8  10 12 
# #   14 16 18 

# #------------------------------------------------------

# # 10)Identity

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(len(mat)):
#     for j in range(len(mat)):
#        if i==j:
#            mat[i][j]=1
#        else:
#            mat[i][j]=0

# for i in range(len(mat)):
#     for j in range(len(mat)):
#         print(mat[i][j],end=" ")
#     print("")

# #Output:
# #   1 0 0 
# #   0 1 0 
# #   0 0 1 

#---------------------------------------------
    
# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]   

# b=[[7,8,9],   #[8,10,12]
#    [4,5,6],   #[8,10,12]
#    [1,2,3]]   #[8,10,12]
        
# res=[]
# for i in range(len(a)):
#     l=[]
#     for j in range(len(a)):
#         l.append((a[i][j])+(b[i][j]))
#     res.append(l)
    
# print(res)

#---------------------------------------------------

# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]   

# b=[[7,8,9],   
#    [4,5,6],  
#    [1,2,3]]  


# res=[]
# for i in range(len(a)):
#     l=[]
#     for j in range(len(a)):
#         l.append((a[i][j])*(b[j][i]))
#     res.append(l)
        
# print(res)



    
    








