import keyword
from sqlalchemy import null


data=[
  (  "1", "Aniket",  "Bhudke",),(  "12",  "pratik",  "jadhao")]

dict={
    "user_id":None,
    "first_name":None,
    "last_name":None}
for i in data:
    dict["user_id"]=i[0]
    dict["first_name"]=i[1]
    dict["last_name"]=i[2]
    print(dict)
    
# dict={"user_id":"none","first_name":"none","last_name":"none"}
# dict["user_id"]=5
# print(dict["user_id"])

# lst1=(1,2,3)
# lst1[1]==5
# print(lst1)


# for i in data:
#     print(i)

        
