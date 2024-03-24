data = [('1', 'Aniket', 'Bhudke'), ('12', 'pratik', 'jadhao'), ('11', 'pratik', 'jadhao'), ('16    ', 'pratik', 'string'), 
 ('19    ', 'prratik', 'string'), ('18    ', 'pratik', 'string'), ('20    ', 'pj', 'string'), ('2', None, None), ('3', None, None),
   ('4', None, None), ('10', None, None), ('testingh', 'string', 'string'), ('om', 'string', 'string'), 
   ('string', 'string', 'string'), ('6', 'harshal', 'kharabe'), ('patil', 'om', 'hursal'), ('exit', 'datta', None),
     ('two', 'partik', 'jadhao'), ('n', 'suyog', 'ingle'), ('ompatil', 'om', 'hursal'), ('d', 'sd', 'string'), 
     ('200', 'aniket', 'bhudke'), ('dfghfd', 'string', 'string'), ('ten', 'amit', 'bajad'), ('gfds', 'string', 'string'), 
     ('testing', 'string', 'string'), ('D', 'Datta', 'string'), ('s', 'suyog', 'string'), ('8', None, None), ('33', None, None), ('111', None, None), ('9', None, None), ('123', 'kunal', 'aswar')]



dict = {'user_id':None,'first_name':None,'last_name':None,}
dict['user_id'] = 5
print(dict['user_id'])
for tup in data:
    dict['user_id']=tup[0]
    dict['first_name']=tup[1]
    dict['last_name']=tup[2]
    print(dict)

# list[1,2,3,4,5]
# list[1] = 5
# print(list)
    