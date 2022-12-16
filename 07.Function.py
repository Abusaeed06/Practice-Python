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


# we have a list of string,string=["s","DOG","Donkey","desh"]
#we want a list which contains those string with all upercase  having length more then 4
#
