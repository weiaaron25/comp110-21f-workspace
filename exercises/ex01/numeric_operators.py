"""EX01 Numeric Operators 8/26/21"""
__author__ = "730448488"
strx = input("Left-hand side number: ")
stry = input("Right-hand side number: ")
x = int(strx)
y = int(stry)
a = x ** y
print(strx + " ** " + stry + " is " + str(a))
b = x / y
print(strx + " / " + stry + " is " + str(b))
c = x // y
print(strx + " // " + stry + " is " + str(c))
d = x % y
print(strx + " % " + stry + " is " + str(d))