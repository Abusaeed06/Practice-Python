# to print something for ten times
for i in range(10):
    print(i)
for num in range(10):
    print(num)

#using start,stop,step

for i in range(1,15,2):
    print(i)

#creating a single number list and looping through it
nums={1,2,3,4,5,6,7,8,9}
for num in nums:
    print(num)
Rolls={1,2,3,4,5,6,7,8,9}
for Roll in Rolls:
    print(Roll)

#Using break in a loop

for num in nums:
    if num ==8:
        print("object found")
        break
    print(num)

for Roll in Rolls:
    if Roll==5:
        print("congratulation")
        break
    print(Roll)

#Using continue
for num in nums:
    if num ==5:
        print("object found")
        continue
    print(num)
for Roll in Rolls :
    if Roll==5:
        print("congratulation")
        continue
    print(Roll)

####Loop in Lop or nested loop

for num in nums:
    for letter in "abcdef":
        print(num,letter)