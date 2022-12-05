My_list=["Ronbin","Bangla",True,1]
print(My_list)
print(type(My_list))

subject=[]
subject.append("statistics")
print(subject)

#subject.insert(position,value)

subject.append("physics")
print(subject)

subject.insert(1,"chemistry")
print(subject)
subject.append(My_list)
print(subject)

subject.extend(My_list)
print(subject)

# remove from list
#1.remove method
#2.Pop method

print(subject)
subject.remove("statistics")
print(subject)
subject.remove(My_list)
print(subject)

subject.pop(1)
print(subject)
subject.pop(4)
print(subject)
print(popped_item)