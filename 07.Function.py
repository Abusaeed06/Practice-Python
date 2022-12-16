# def fun_nam(x,y):
#     print(x+"is a string "+y)
# print(fun_nam("string","string"))
### using function ad calculating addition,substraction,multiplication,division
# def arithmetic(x,y,kind):
#     if kind=="add":
#         return x+y
#     elif kind=="sub":
#         return x-y
#     elif kind=="mul":
#         return x*y
#     elif kind=="div":
#         return x/y
#     else:
#         print("please type add,mul,subb,dev")
#
# x=float(input("Enter your pass number:"))
# y=float(input("Enter second num:"))
# kind=input("What do you want to do:")
# print(arithmetic(x,y,kind))


#PROBLEM 1
# we have a list of numbers,nums[2,3,4,5,6]
#we want a list which contains square of valued of each num in nums
#new_nums=[4,9,16,25,36]

nums=[2,3,4,5,6]
square_names=[]
for num in nums:
    square_names.append(num**2 )
print(square_names)

project_value=[]
for numb in nums:
    if numb>4:
        project_value.append(numb)
print(project_value)

###PROBLEM 2

# we have a list of string,string=["s","DOG","Donkey","desh","fruits","monkey"]
#we want a list which contains those string with all upercase  having length more then 4
#
strings=["s","DOG","Donkey","desh","fruits","monkey"]
mod_strings=[]
for val in strings:
    if len(val)>4:
        mod_strings.append(val.upper())

print(mod_strings)


########## COMPREHENSION #######

#for 1 nno problem
new_nums=[num**2 for num in nums]
new_nums1={num**2 for num in nums}
print(new_nums)
print(new_nums1)

#for 2 number problem

all_len=[len(x) for x in strings]
print(all_len)
# if i want to all least then i use least [] and if i want unic least  then i use {} set funtionn

unic_all_len={len(x) for x in strings}
print(unic_all_len)

print(set(map(len,strings)))



