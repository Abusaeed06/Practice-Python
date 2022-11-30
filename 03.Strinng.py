#name=input("Enter your name?\n")
#Date_of_Birth=input("please enter your date of birth year\n")

#current_year=2022
#age=current_year-int(Date_of_Birth)
#message= name +", You are "+str(age)+" years old"
#print(message)


msg="Hello World"
#    012345678910
print(msg)
print(len(msg))
print("hello",len(msg))
print(msg[0:5])  #Srart:Stop

copy_m=msg[:]
print(copy_m)

## Using  some  Method
# .lower
print(copy_m.lower())

#.upper
print(copy_m.upper())

# .count
print(msg.count("Hello"))
print(msg.count("l"))

# .find

print(msg.find("o="))
print(msg.find("m"))

# .replace
new_msg=msg.replace("Hello","Hi")
print(new_msg)

# String Formatting

#general method
greting="Hello"
name="jahid"
#message=greting+ " "+name
#print(message)

#message="{} {}.welcome!".format(greting,name)
#print(message)

#message=f'{greting.lower()},{name.upper()} welcome!'
#print(message)

print(dir(name))
print(help(str.lower))


