#Arithmetic Operator

# "+"  Addition
print(30+10)

# "-" Subtraction
print(30-10)

#"*" Multiplication
print(5*6)

#"/" Division
print(30/10)

#"%" Modulus or Reaminder
print(30%4)

#"**" Exponent or power
print(3**2)

#"//" Floor Division
print(30//4)

# "+= , -= , *= , /= " augmented / enhanchd asingment operator
x=10
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x /=3
print(x)

# Operator Sequence
#PEMDAS
#P=Parenthesis
#E=Exponent
#M=Multipication
#D=Division
#A=Addition
#S=Substraction

y=(10+5)*2**3
print(y)

# Arithmetic function
#round

x=4.5
y=4.7
print(round(x))
print(round(y))

#abs
j=-40
print(abs(j))
print(abs(-4))

#pow
print(pow(5,2))
h=10
print(pow(h,2))
#import math function
import math
l=10
print(math.cbrt(l))

from math import *
t=math.ceil(6.1)
print(t)
print(math.ceil(4.2))

r=math.floor(4.2)
print(r)
print(math.floor(6.1))

#factorial
# n(n-1)(n-2)(n-3)(n-4)(n-5)...
#5!
a=5*4*3*2*1
print(a)

b=math.factorial(5)
print(b)

#lcm= loest common multiple (losagu)

print(math.lcm(5,25))

# gcd =gretest commom divisor (gosagu)
print(math.gcd(5,25))

#minimum,maximum

print(max(23,26,19,23))
print(min(23,26,19,23))

# square root
print(math.sqrt(49))