##-------------------PROGRAMMING LANGAUGE ERA
# 1st generation:(1940-50):machine languages:
# 2nd generations:(1950-60):assembly languages:cobol,fortran
# 3rd generation:(1960-70):highlevel languages:c;pascal
# 4th generation:(1970-80):procedural,langauge:cpp,java
# 5th generation:(1980-90):oop based languages:java,cpp,python
# 6th generation(modern era):(2000s-present):script languages:python ,js,ruby

##----------------FEATURES OF PYTHON
# high level programic language
# easy to learn/understand/read
# general purpose language
# have a large community :
# interpreted language:does not need a compilation befor
# running,line by line execution.
# strictly dynamically typed:no need of variable declaration.
# datatype determined during runtime
# oop based
# 1980   1989   1991 feb 20
# Guido Van Rossum : monty python
# code readability and developer productivity==>python design philospy

#---------------PRINT FUNCTION

#print("welcome to python")# to print string data
#print(123) #int
# print(222.89) #float
# print(True) #bool
# print(False) #bool

##-------------------TYPE FUNCTION : to return type of data

# print(type(12345)) #int
# print(type("12345")) #str
# print(type(123.45)) #float
# print(type(True)) #bool

"type function are used to detemine type of a data"

"""twinkle twinle 
little star"""

##----------VARIABLES:temporary memory location to hold data

# b="welcome to python"
# print("welcome to python")
# print("welcome to python")
# print("welcome to python"+"vasudha")
# a="welcome to python"
# print(a)


##------variables rules: temp memry lctn to hold data
# varaibales names must start with alphabets or underscore
name="vasudha"
_name="vasudha"
# it cannot contains special symbols except underscore
my_name="vasudha"
# cannot contain whitespace
# any length can be accessed but practically we use small length variables
# keyword and identifiers cannot used as variable name
# case sensitive a=90 A=9

#----------------parallel assigment
# a=90
# b=89
# a,b=90,89

a=90
# print(type(a))
# a="lkjjhghg"
# print(a) #90
# print(type(a)) #

b="45"
print(type(b))
b=int(b)
print(type(b))


# name="vasudha"
# age=27
# com="future optima it solutions"
# print(name,age,com)
# print("i am ",name)
# print("iam ",age,"years old ")
# print("iam working at ",com)
# print(f"iam {age} years old")

#------------------------
# name="vasudha"
# age=27
# com="future optima it solutions"
# print(f"iam {name} {age} years old \nworking at {com}",end=" ")
# print("as a python tutor")

#-----------------------------------
# pet="cat"
# name="jerry"
# age=3

# print("i have a ",pet,"\nhis name is ",name,"\n",age," years old")
# print(f"i have a {pet} \nhis name is {name} \n{age} years old ")

##--------PRINT\n
# name="vasudha"
# age=27
# #-----vasudha
# print(name)
# #----my name is vasudha
# print("my name is ",name)
# #----my name is vasudha iam 27 years old
# print("my name is",name,"iam",age,"years old")
# #----python formater
# print(f"my name is {name} iam {age} years old")

##----------------------TYPE CONVERSION
# a=90
# print(type(a)) #int
# a=str(a)
# print(type(a)) #str

# b="67"
# print(type(b)) #str
# b=int(b)
# print(type(b)) #int

# b="67"
# print(type(b)) #str
# b=float(b)
# print(type(b)) #float

# n=9.9
# n=int(n)
# print(n)

##-----------------INPUT


# name=input("enter your name : ")
# print(f"hai {name}")
# print(type(name))
# age=input("enter your age : ")
# print(f"your age is {age}")
# print(type(age))
# # # #input data : default string
# age=int(age)
# print(type(age))
# num=int(input("enter a number : "))



##---------OPERATORS
# : special symbols or keywords use perform specific task
# 1 assignment :
# =  a=6 a assigns 6  += -+ *= /=  a=a-7  a-=7
# a=9
# a=a+3 #12
# a+=3
# name="vasudha"
# age=23
# agree=True

# num=1
# num=num+1
# num+=1

# num=9
# num=num-5
# num-=5

# num=9
# num=num*5
# num*=5

# num=9
# num=num/5
# num/=5



## -----work: swap two number a=9 b=8
# a=int(input("enter a number :"))
# b=int(input("enter a number :"))
# print(f"before swappin a={a} b={b}")
# c=a #9
# a=b #8
# b=c #9
# print(f"after swappin a={a} b={b}")
# # ##-------------------------- method 2: parallel assigment
# a,b=9,8
# print(f"before swappin a={a} b={b}")
# a,b=b,a
# print(f"after swappin a={a} b={b}")
#---------------------------------------------

# 2 aritehmatic :+ - * / //  % **
# + - / 5/2=2.5  // floor 5//2=2   *  % modul: reminder  ** exp a**10 a**2
# 5/2=2.5    5//2=2  9/2=4.5 9//2=4  10/2=5.0
# modulo reminder  5%2=1 14%3=2
#  ** expo 2**3  x**10  x**3
##-------------work 1: add two number 2 3 2+3=5
# a=int(input("enter a number :"))
# b=int(input("enter a number :"))
# c=a+b #94
# print(c)
# print("sum=",c)
# print(f"{a} + {b}={c}")
#-----------------------------

# work:  find area of rectangle
# l=int(input("enter length of rectangle "))
# b=int(input("enter width of rectangle "))
# area=l*b
# print("area = ",area)

#work find area of a square
# side=int(input("enter side of sqaure"))
# area=side**2
# print(area)

# work: find square root of a  number
# num=int(input("enter a number : "))
# s=num**0.5
# s=num**(1/2)
# print("squre root =",s)


##---------------work 2: find reminder
# a=67
# b=8
# c=a%b
# print(c)


##--------------work 3:return last digit of a number
# num=int(input("enter a number : "))#456
# lastd=num%10  #456%10=6
# print(f"last digit of {num} is {lastd}")

##--------------work 4:sum of digits of 2 digit number num=45 9  67
# num=int(input("enter 2 digit number :"))#45
# f=num//10  #45//10=4
# lst=num%10 #45%10=5
# print("sum of digit = ",lst+f)
# print(f"sum of digit of {num} ==> {lst+f}")

# work---------------------------
#1. difference between sum of squar of 2 num
# and square of sum of the same
#2. swap/reverse two digit number   input=89   output=98
#3.solve quadratic equation

# difference between sum of squar of 2 num
# and square of sum of the same
# a=3
# b=2
# sum=a**2 + b**2
# square=(a+b)**2
# dif=sum-square
# print("answer=",dif)
# print(f"{sum}- {square}= {dif}")

#---------------------swap digit of two digit num
# num=int(input("enter a number :"))#45  5*10+4
# f=num//10 #4
# s=num%10  #5
# swapped=s*10+f
# print(num,"===>",swapped)

# work:  solve quantratic eqaution
# a,b,c=2,4,6
# root=(b**2-4*a*c)**0.5
# x=(-b+root)/(2*a)
# y=(-b-root)/(2*a)
# print("x=",x)
# print("y=",y)

##-------------------OPERATOR PRECEDENCE
# () **ex  /* +-
# print(10/2*6)
# print(12/6/2)  #left asso
# print(2+8-9-2)
# print(3**2**1) # right associative

#3 COMPARISON : == identity != < <= > >= :return true or false
# a=90
# b=90
# c=67
# print(a!=b)#f
# print(b==c)#f
# print(a<b)#f
# print(a<=b)#t
# print(b<a)#f
# print(a>b)#f
# print(a>=b)#t
# print(b>=c)
# print(b<=c)

#4 LOGICAL :Condition : and or not : precdence==> not and or
#not : oposit
#and: both true
#or :any one true
# a=True
# b=False
# c=True
# print(a or b) # t or f==>t
# print(a or a) # t or t==>t
# print(not(a and a)) #   t and t=t=> not t=>f
# print(a and b) #t and f==>f
# print(a or b and not c) #   t or f==>t
# print(not a or b or c or not c) #

a=90
b=89
c=67
print(not(a<b or b<c)) #t


#---------------------CHANEG COLOR
#print("\033[91m HAI IAM RED \033[0m")
#("\033[92m HAI IAM GREEN \033[0m")
#print("\033[93m HAI IAM YELLOW \033[0m")
# print("\033[94m HAI IAM BLUE \033[0m")
# print("\033[95m HAI IAM MAGENTA \033[0m")
# print("\033[96m HAI IAM CYAN \033[0m")
# print("\033[97m HAI IAM WHITE \033[0m")


# *************************work

# find area and perimeter of circle
# 2pi R  pi r**2
# r=int(input("enter radius : "))
# area=3.14*r**2
# peri=2*3.14*r
# print("area= ",area)
# print("perimeter= ",peri)

# step1:start
# step2:take user input r
# step:calculate area
# step4:calculate perimaeter
# step5:print area and perimeter
# ste6:stop




