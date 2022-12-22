import numpy as np
row1=[1,2,3,4]
row2=[4,5,6,7]
row3=[7,8,9,10]
row4=[10,11,12,13]
row5=[13,14,15,16]
array_a=np.array([row1,row2,row3,row4,row5])
print(array_a)

print(array_a[:])

print(array_a[:,1:3])

print(array_a[:,1:3:1])

print(array_a[:,-1:-3:-1])

##Booean Indexing

greater_than_4=array_a>4
print(greater_than_4)

print(array_a[greater_than_4])
#where method

drop_under_4=np.where(array_a>4,array_a,0)
print(drop_under_4)

##Logical_and
drop_under_4_above13=np.logical_and(array_a>4,array_a<13)
print(drop_under_4_above13)
#Arithmetic operations
array_b=np.array([[1,2],[3,4]])
array_c=np.array([[2,2],[4,6]])

print(array_b)
print(array_c)

#single arry operation

print(array_b.sum(axis=1)) ## axis 1 indicate row
print(array_b.sum(axis=0)) ## axis 0 indiicate column

print(array_b.cumsum())
print(array_b.prod())
