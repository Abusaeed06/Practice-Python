My_list=["Ronbin","Bangla",True,1]
print(My_list)
print(type(My_list))

subject=[]
subject.append("statistics")
print(subject)

#subject.insert(position,value)

subject.append("physics")
print(subject)

subject.insert(1,"Chemistry")
print(subject)
subject.append(My_list)
print(subject)

subject.extend(My_list)
print(subject)

# remove from list
# 1.remove method
# 2.Pop method

print(subject)
subject.remove("statistics")
print(subject)
subject.remove(My_list)
print(subject)

subject.pop(1)
print(subject)
subject.pop(4)
print(subject)


a="Bangla"
print(len(a))
num_sub=len(subject)
print(num_sub)

print("there are",num_sub,"subject in our list")

subject.reverse()
subject.remove(True)
subject.sort()

print(subject)
c=sorted(subject)
print(c)

# Finding value

print(subject.index("Ronbin"))

print('Chemistry'in subject)
print("Bangla" in subject)
print("jamai" in subject)


subject.append("Physics")
print(subject)

#list for loop
# For Loop & While loop

for item in subject:
    print(item)
#with index number

for index, item in enumerate(subject):
    print(index,item)
# with index start with 1

for index, item in enumerate(subject,start=1):
    print(index,item)

########## Tuple

# Tuple make in first bracket

tup=('name','value','subject')
print(tup)
print(type(tup))

#nothing can be addedor remover
#print(tup.append('gua'))

print(tup[1])

#tuole makeig list

tup_list=list(tup)
print(tup_list)

#then we can add

tup_list.append("age")

#and list make tuple

list_tup=tuple(tup_list)
print(type(list_tup))



