################work
#1 square all elements of a list and print in reverse order
#2 find elements with frequecy greater than  k
#3 remove all occurences of an item from a list [1,2,31,1,3,4,1]
#4 create flat list from nested list l=[[1,2,3],[2,3,4],[4,5,6]]=[1,2,3,2,3,4,4,5,6]
#5 interchange first and last elements of a list
#6 count and filter even and odd numbers from a list of number
#7 from a list of names return names which are start with a or A
#8 from a list of names return name  which contain character "a"
#9 create alist of unique elements from a list



# l=[[1,2,3],[3,4,5]]==[1,2,3,3,4,5]
####################solutions
# ##############interchange first and last elements of a list
# l1=[1,2,3,4,5,6]
# l1[0],l1[-1]=l1[-1],l1[0]
# print(l1)
#
# #######find all the possible combination of alist with three elememts
# l1=[1,2,3]
# l2=[]
# for i in l1:
#     l2.append(i)
#     print(l2)
#     for j in l1:
#         l2.append(j)
#         print("l2=",l2)
#         l2.pop()
#     l2=[]
# print(l1)
#
#
# #######square all elements of a list and print in reverse order
# l1=[1,2,3,4,5]
# l2=[]#1 4 9 16 25
# for i in l1:#1 2 3 4 5
#     l2.append(i**2)#l2.append(4)
# l2.reverse()
# print(l2)
# print(l2[::-1])
#
#
#k=2
# #####find elements with frequecy greater than  k
k=int(input("enter the frequency"))#3
l1=[1,1,1,1,2,2,3,3,4]
l2=[]
for i in l1:#1
    if l1.count(i)>k and i not in l2:
        l2.append(i)
print(l2)
#
#
#
# #######remove all occurences of an item from a list [1,2,31,1,3,4,1]
# [1,2,31,1,3,4,1]  ==>[2,31,3,4]
list1=[4,5,6,5,6,6,6]#
l1=len(list1)#7
n=5#elemente to be removed
for i in range(l1):#7 0  1  2
    if n in list1:#if 5 in list1
        list1.remove(n)#l.remove(3)[4,6,6,6,6]
    else:
        break
print(list1)

#############method 2
list1=[4,5,6,5,6,6,6]
n=5
removed=[]
for i in list1:
    if i!=n:
        removed.append(i)
print(removed)

#############methos3
list1=[4,5,6,5,6,6,6]
n=5
rem=[i for i in list1 if i!=n]
print(rem)




#
# #######craete flat list from nested list

l1=[[1,2,3],[3,4,5],[4,5]]#[1,2,3,3,4,5,4,5]
flat=[]#[1,2,3,3,4,5,4,5]
for i in l1:#[4,5]
    # flat.extend(i)#flat.extend([4,5])
    flat=flat+i
print(flat)

############### method2
l1=[[1,2,3],[3,4,5],[4,5]]
flat=[]
for i in l1:#[1,2,3] [3,4,5],[4,5]
    for j in i:#[4,5],
        flat.append(j)
print(flat)
#
#
# ################count and filter even and odd numbers from a list of number

l=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even," count of even number ",len(even))
print(odd," count of even number ",len(odd))


##########from a list of names return names which are start with a or A

l1=['anju','Anu','anandhu','vasudha','midhun']
l=[]#anju Anu anandhu
for i in l1:#
    if i[0]=="a" or i[0]=="A":#i[0].upper=="A"
        l.append(i)
print(l)



################from a list of names return name  which contain character "a"
l1=['anu','vasu','midhu']#anu vasu
for i in l1:
    if "a" in i:
        print(i)

################### create alist of unique elements from a list
l=[1,2,3,4,2,3,4,5,6,6]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)







###########treassure hunt

# 1.creating a 3 x 3 grid
# list_1 = [" ", " ", " "]
# list_2 = [" ", " ", " "]
# list_3 = [" ", " ", " "]
#
# #2.create the grid(map)
# map = [list_1,list_2,list_3]
# print(map)
# print("Hiding Your Treasures!!!!")
# # Ask user to input the spot
# spot = input("Enter the spot means a letter with a number for the treasure")
# print("printing \'x\' marks on the treasure")
# # pick the first character of spot means letter that user has been entered
# spot_letter = spot[0].lower()
# # create a new list with characters a,b and c for checking the  spot letter in the new list
# abc = ['a','b','c']
# # for check the user entered spot letter in which index of the list abc
# spot_letter_index = abc.index(spot_letter)
# # for checking user entered second character which is number ,
# #convert it into integer
# #and subtract 1 from the number for zero based index
# number_index = int(spot[1])-1
# map[spot_letter_index][number_index] = "X"
# print(f"{list_1}\n{list_2}\n{list_3}")