my_set = {'Rakib','Robin','Abdul','Basir'}
print(my_set)
my_list=['Rakib','Robin','Abdul','Basir']
print(my_list)

A={'Math','Statistics','Physics','ict','bangla'}
B={'History','English','Socioligy', 'ict','bangla'}
#intersection()
#difference()
#union()
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.union(B))

###################
##Dictonary##
#key,value pair

my_dict={'name':'rajib','age': 25 ,'sub':'math'}
print(my_dict)

my_dict={'name':'rajib',
         'age': 25 ,
         'sub':'math'
         }
print(my_dict)
print(my_dict['name'])
print(my_dict['age'])

#Add new variable

my_dict['phone']='01700524464'
print(my_dict)

##get method
my_dict.get('sex')
print(my_dict)
print(my_dict.get('name','not exist'))
# change value nae or rename
my_dict['name']='Rakib'
print(my_dict)

my_dict.update({
    'name':'Shakib',
    'age':28,
    'phone':'01641083323'
})
print(my_dict)

##delete value

del my_dict['sub']
print(my_dict)
del_age=my_dict.pop('age')
print(del_age)
print(my_dict)

print(len(my_dict))
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

for key in my_dict:
    print(key)

for key,values in my_dict.items():
    print(key,values)