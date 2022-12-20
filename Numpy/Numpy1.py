import numpy as np
print(np.__version__)

######## Array #####

f_array=np.array([1,2,3,4,5,True,False,])
print(f_array)

# creating a single dimensional array

arry1=np.array([10,20,30,40])
print(arry1)
print(type(arry1))
# we will use array_name .shape() to know the shape of an array

print(arry1.shape)
# in shape Row,column

### Multi dimentional array
arry2=np.array([[10,20,30,40],[500,60,70,80]])
print(arry2)
print(arry2.shape)
print(type(arry2))
arry3=np.array([[1,2,3,4],[5,6,7,8],[2,3,4,5]])
print(arry3)

a=[10,20,30,40]
b=[50,60,70,80]
c=np.array([a,b])
print(c)
print(c.shape)
# change shape methode (change the valu shape of variable)

arry2.shape = (4,2)
print(arry2)
c.shape=(4,2)
print(c)

# Or reshape methode(do not change the value shape of variablebecause here we create a new variable with new shaoe)
arry_res=arry2.reshape(2,4)
print(arry_res)
print(arry2.shape)
print(arry2)
print(arry_res)

### .zeros() method
# .zeros method takes two parameters 'rows' and 'Column' numbers and makes an array using only zeros
#Initializing numpy array using .zeros(rows,columns) method
arr0=np.zeros((5,5))
print(arr0)
print(arr0.ndim)
print(type(arr0))
print(arr0.shape)
arr1=np.ones((5,5))
print(arr1)
print(arr0.ndim)

### Making an array with a specificc number
#creating an array using .full() method
arr_sn=np.full((4,5),16)
print(arr_sn)

### Initializing a numphy array within a range
# -To initialize an array within a range we will use
# -np.arange(start,stop,step(optional)

f_casee=np.arange(9)
print(f_casee)
s_case=np.arange(5,15)
print(s_case)
fi_case=np.arange(5,15,2)
print(fi_case)
arr5=np.arange(5,15)
print(arr5)
arr6=np.arange(5,15,3)
print(arr6)

