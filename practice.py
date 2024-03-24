#list
# a=[4,5,2,6,3,1,8]
# print(a[1:4])
# a[5]=9
# print(a)
# a.append(3)
# print(a)
# print(a.count(3))
# a.remove(3)
# print(a)
# a.insert(2,30)
# print(a)

# b=[]
# for i in range(1,10):
#     b.append(i)
# print(b)
# b.reverse()
# print(b)
# print(len(b))

# c=["abhi","abhay","abhijeet","abhishek"]
# for i in range(3,-1,-1):
#     print(c[i])
# c[0]="amit"
# print(c)
# print(c[1:4])
# c.append("sharma")
# print(c)
# c.remove("sharma")
# print(c)
# c.reverse()
# print(c)
# c.sort()
# print(c)
# print(len(c))

######tuple

# a=(3,2,1,5,6)
# print(a)
# c=(4,3)
# d=a+c
# print(d)


# b=("amit","abhi","rushi","ram")
# print(b)

# m=()
# for i in range(10):
#     i=input("enter the element")
#     m+=(i,)
# print(m)

# max_elements = 10
# user_tuple = ()
# for _ in range(max_elements):
#     element = input("Enter an element: ")
#     user_tuple += (element,)  
# print("Final tuple:", user_tuple)

# elements = []
# for _ in range(10):
#     element = input("Enter an element: ")
#     elements.append(element)
# user_tuple = tuple(elements)
# print("Tuple created from user input:", user_tuple))

dict={"Legend":"MSD","King":"Virat","Hitman":"Rohit"}
keys=dict.keys()
print(keys)
values=dict.values()
print(values)
print(dict["Legend"])