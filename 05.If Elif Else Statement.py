# Build a Temperature which will-
#1.assk for temperature in celsius scale from user.
#2.convert the temperature in fahrenheit scale. (9c/5)+32 or (1.8c+32)
#3.test the code using 25.8 degree celcius as input.
#Of your output 78.44 degree fahrenheit then submit your code


Temp_c=float(input("Enter temp in celsius scale: "))

Tem_f=1.8*Temp_c+32
print("Temperature in fahrenheit scale is"+str(Tem_f)+"F")
#or
print("Temperature in fahrenheit scale is",str(Tem_f),"F")

