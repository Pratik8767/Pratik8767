list=[('1', 'Aniket', 'Bhudke'), ('12', 'pratik', 'jadhao')]

dict={"user_id":None,"first_name":None,"last_name":None}
print(dict)

dict['user_id']=5
print(dict)

list=[1,2,3]
list[1]=5
print(list)

list=[('1', 'Aniket', 'Bhudke'), ('12', 'pratik', 'jadhao')]

dict={"user_id":None,"first_name":None,"last_name":None}

for i in list:
    dict['user_id']=i[0]
    dict['first_name']=i[1]
    dict['last_name']=i[2]
    print(dict)