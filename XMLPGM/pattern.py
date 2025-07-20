# #1.--------------- print n star horizondally if n=4 ****
# n=4
# for i in range(n):
#     print("*",end=" ")



##------------------------------------ 2. square pattern
# if n=4
# * * * *
# * * * *
# * * * *
# * * * *
#-------------------method1
# n=4
# for row in range(n):# 4==>0-3==>0 1 2 3
#     print(n*"* ")#4* "*"  ****

# 0==>* * * *
# 1==>* * * *
# 2==>* * * *
# 3==>* * * *

#-------------------method2

# n=4
# for row in range(n): #4=> 0 1 2 3
#     for col in range(n):#4=>0 1 2 3 * * * *
#         print("*",end=" ")
#     print()
# 0=>  * * * *
# 1=>  * * * *
# 2

##3---------------------------right angled triangle pattern
# n=4  for i in range(1,n+1) 1,5  1-1 2-2 3-3 4-4  i=i
# *-----0----1
# **----1----2
# ***---2----3
# ****--3----4
#       i----i+1
#-------------------method1
# n=4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# #-------------------method2.1
# n=4
# for i in range(n):
#     print((i+1)*"* ")
# #-------------------method2.2
# n=4
# for i in range(1,n+1):
#     print((i)*"* ")
#4----------------------------------------revers right angled triangle
# n=4
# ****---0---n-0
# ***----1---n-1
# **-----2---n-2
# *------3---n-3
#------------------method1.1
# n=4
# for i in range(n):
#     print((n-i)*"* ")
#------------------method1.2
# **** 4--4  n4 3 2 1
# ***  3--3
# **   2--2
# *    1--1
# n=4
# for i in range(n,0,-1):#4 3 2 1
#     print(i*" *")

# #-----------------method2
# n=4
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=' ')
#     print()

#5----------------------------------parallelogram
# n=4
# * * * *       0----0space------4star
#  * * * *      1----1space------4star
#    * * * *    2----2space------4star
#     * * * *   3----3space------4star
#                 i----ispace------n star

#-----------------method1
# n=4
# for i in range(n):
#     print(i*" "+n*"* ")
#
# #-----------------------method 2
# n=4
# for i in range(n): #0 1 2
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n):
#         print("* ",end="")
#     print()


#6-----------------------------------pyramid
# n=4
#        *            0-----4space n-0------1star
#     *     *         1     3space n-1      2
#   *    *     *      2     2space n-2      3
# *    *     *    *   3     1space n-3      4
#-----------------------------method1 n-i    i+1
n=4
for i in range(n):
    print((n-i)*" "+(i+1)*"* ")

#------------------------method2
# n=4
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

#7--------------------pyramid with odd
# n=4
#       *         0------4space----- 1star 2*i+1=1
#     * * *       1      3           3     2*1+1=3
#   * * * * *     2      2           5     2*2+1=5
# * * * * * * *   3      1           7
#---------------- method 1
# n=4
# for i in range(n):
#     print((n-i)*"  "+(2*i+1)*"* ")


# ------------method2
# n=4
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()

