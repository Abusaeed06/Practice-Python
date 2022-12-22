import numpy as np
seq_a=[1,2,3]
seq_b=[4,5,6]
seq_c=[7,8,9]
array_list=np.array([seq_a,seq_b,seq_c])
print(array_list)
print(type(array_list.shape))

## create an (5,2)array
new=np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
print(new)
print(np.shape(new))

### Reshapping
# size
print(array_list.size)
array_re=array_list.reshape(1,9)
print(array_re)

# Transpose matrix
array_tr=array_list.T
print(array_tr)
array_tr_tr=array_tr.T
print(array_tr_tr)
#split matrix (row,column)
print(array_list[0])
# indexing:array_name[rows,column
print(array_list[:,0])

print(array_list[:,2])

print(array_list[2,2])
