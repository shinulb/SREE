#1-----------------------------------o
#0   *  *
#1 *      *
#2 *      *
#3 *      *
#4    * *


# for i in range(5):
#     for j in range(4):
#         if(i==0 or i==4) and (j==1 or j==2):
#             print("*",end=" ")
#         elif(i in range(1,4)) and (j==0 or j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

r=5
c=4
for i in range(r):
    for j in range(c):
        if (i==0 or i==r-1) and(j in range(1,c-1)):
            print("*",end=" ")
        elif((i in range (1,r-1)) and (j==0 or j==c-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()






# 2------------------------------------X
# *     *
#  *   *
#    *
#  *   *
# *     *

n=7
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#3--------------------*
# n=7
# for i in range(n):
#     for j in range(n):
#         if (i==j) or (i+j==n-1) or (j==n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#4----------------------------*
# n=7
# for i in range(n):
#     for j in range(n):
#         if (i==j) or (i+j==n-1) or (j==n//2) or (i==n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()