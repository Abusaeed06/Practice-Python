# Build a Temperature which will-
#1.assk for temperature in celsius scale from user.
#2.convert the temperature in fahrenheit scale. (9c/5)+32 or (1.8c+32)
#3.test the code using 25.8 degree celcius as input.
#Of your output 78.44 degree fahrenheit then submit your code


#Temp_c=float(input("Enter temp in celsius scale: "))

#Tem_f=1.8*Temp_c+32
#print("Temperature in fahrenheit scale is"+str(Tem_f)+"F")
#or
#print("Temperature in fahrenheit scale is",str(Tem_f),"F")



### Control flow

Temp=56
if Temp>30:
    print("It's Hot out there")
    print("Dont go out")
else:
    print("It's normal out there")

print(3==3)
print(3!=3)
print(3<2)
print(3>2)
print(3<=2)
print(3>=2)
print(3>2 or 3==2)
print(3>2 and 3==2)
#1
#age=16
# if age>18:
#     print("Applicanrt is eligible for loan")
# else:
#     print("Applicant is not eligible for loan")
#
#2
# age=14
# if age>=18:
#     msg="Eligible"
# else:
#     msg="not eligible"
#
# print(msg)

#3
age=12
msg="Eligible"if age>=18 else "not Eligible"
print(msg)

