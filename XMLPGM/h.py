# # import xml.etree.ElementTree as ET

# # # Parse the XML file
# # tree = ET.parse('sample.xml')
# # root = tree.getroot()

# # # Print student info
# # for student in root.findall('student'):
# #     name = student.find('name').text
# #     age = student.find('age').text
# #     course = student.find('course').text
# #     print(f"Name: {name}, Age: {age}, Course: {course}")
# # def func(x, y=[]):
# #     y.append(x)
# #     return y

# # print(func(1))
# # print(func(2))
# # print(func(3, []))



# # set1={1,2,3,4,5}
# # print(1 not in set1)


# # set1={"a","b","c","d","e"}
# # set1.add("f")
# # print(set1)

# # set1={"a","b","c","d","e"}
# # set2={1,2,3,4,5,6}
# # set1.update(set2)
# # print(set1)

# # set1={"a","b","c","d","e"}
# # set1.remove("a")
# # print(set1)

# # set1={"a","b","c","d","e"}
# # set1.discard("a")
# # print(set1)

# # set1={"a","b","c","d","e"}
# # res=set1.pop()
# # print(res)

# # set1={"a","b","c","d","e"}
# # del set1

# # tp=("a","b","c","d","e")
# # del tp
# # print(tp)

# # tp1=1,2,3,4,5
# # print(type(tp1))
# # tp2=(1,)
# # print(type(tp2))

# # tp=("a","b","c","d","e")
# # for i in tp:
# #     print(i)

# # set1={"a","b","c","d","e"}
# # set2={1,2,3,4,5,6}
# # set3=set1.union(set2)
# # print(set3)

# # set1={"a","b","c","d","e"}
# # set2={1,2,3,4,5,6}
# # set3=set1|set2
# # print(set3)

# # set1={"a","b","c","d","e"}
# # set2={1,2,3,4,5,6,"a"}
# # set3=set1.intersection(set2)
# # print(set3)

# # set1={"a","b","c","d","e"}
# # set2={1,2,3,4,5,6,"a"}
# # set3=set1&set2
# # print(set3)


# # dict={
# #     "name":"shinu",
# #     "age":30,
# #     "place":"tdpa"
# # }
# # # res=dict['name']
# # # res=dict.get('name')
# # # res=dict.keys()
# # # res=dict.values()
# # # dict['qualification']='Btech'
# # # dict['age']=31
# # # dict.update({'qualification':'poly'})
# # # dict.pop('age') 
# # # dict.popitem()
# # # dict.clear()

# # for x in dict.items():
# #     print(x)
# # # print(dict)

# # a=20
# # b=30
# # if a>b:
# #     print("a is greater than b")
# # elif a<b:
# #     print("b is greater than a")
# # else:
# #     print("a is equal to b")


# # for i in range(10):
# #     if i==5:
# #         continue
# #     print(i)

# # def sample():
# #     print("Jthread")
# # sample()

# # def sum(a,b):
# #     return a+b

# # result=sum(1,1)
# # print(result)   


# # class person:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age

# #     def display(self):
# #         print(f"Name: {self.name}, Age: {self.age}")


# # p=person("shinu",30)
# # p.display()


# n=5
# for i  in range(n):
#     for j in range(i,n):
#         print(" ",end=" ") 
#     for k in range(i+1):
#         print("*",end=" ")
#     for k in range(i):
#         print("*",end=" ")
    
#     print()

import pandas as pd

df = pd.DataFrame({
    'Name': ['anu', 'babu', 'Charlie'],
    'Age': [25, 30, 35]
})
print(df.iloc[1, 0])

