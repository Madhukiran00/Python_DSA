# n=2739
# 

# m500=int(string[-3:])//500
# m1000=n//1000
# print("1000:",m1000)
# temp1=n%1000 #539
# m500=temp1//500
# print("m500:",m500)
# m100=(temp1%500)//200 #239
# print("m100:",m100)
# m50=((temp1%500)%200)//50
# print("m50:",m50)
# m10=((temp1%500)%200)//10
# print("m10:",m10)
# temp2=temp1%500

# change=int(string[-3:])-500 #750
# m100=change//100. #250 2
# m50=(change-(m100*100))//50
# print(m50)
# print("1000s:{0} , 500s:{1} and 100s:{2} ,50s:{3}".format(m1000,m500,m100,m50))


# sec=38

# hours=sec//3600

# temp=sec%3600

# minutes=temp//60

# secounds=temp%60

# print("hours:",hours,"minutes:",minutes,"secounds:",secounds)

# n=5
# m=56
# for i in range(n,m+1):
#     print(i)


# n=8
# res=0
# print((n*(n+1))//2)
# n=6
# res=0
# for i in range(1,n+1):
#     if n%i==0:
#         res=res*10+i
# print(res)


# s="mada"

# i=0
# j=len(s)-1
# while i<j:
#     if s[i]==s[j]:
#         i=i+1
#         j=j-1
        
#     else:
#         print("False")
#         break
# if i>=j:
#     print("Yes")


# import math

# num=434
# res=num//10**int(math.log10(num))

# print(res)

# st="145"

# sum=0
# for i in range(len(st)):
#     v=1

#     for j in range(1,int(st[i])+1):
#         v=v*int(j)
    
#     sum=sum+v

# print(sum==int(st))

# Neon number:
# num=9

# sq=num**2
# sum=0
# while sq!=0:
#     rem=num%10
#     sum=sum+rem
#     sq=sq//10
    
# print(sum)

# def factorial(n):
#     if n==0 or n==1:
#         return 1
    
#     return n*factorial(n-1)
    
    
# n=5 
# print(factorial(5))


# def nat_sum(n):
#     if n==0:
#         return 1 
    
    
#     return nat_sum(n-1)+nat_sum(n-2)
# n=5
# print(nat_sum(n))

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# terms = 5 
# for i in range(terms):
#     print(fibonacci(i), end=" ")

# n=5
# a,b=0,1
# for i in range(n):
    
#     print(a,end='')
#     a,b=b,a+b

# def su(n):
#     if n==1:
#         return 1
#     return n+su(n-1)
# print(su(5))

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)


print(reverse_number(1234))







