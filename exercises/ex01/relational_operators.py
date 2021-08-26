"""EX01 Relational Operators"""
__author__ = "730448488"

lhs: int = input("Left-hand side: ")
rhs: int = input("Right-hand side: ")

a = lhs<rhs
print(str(lhs) + " < " + str(rhs) + " is " + str(a))

b = lhs >= rhs
print(str(lhs) + " >= " + str(rhs) + " is " + str(b))

c = lhs == rhs
print(str(lhs) + " == " + str(rhs) + " is " + str(c))

d = lhs != rhs
print(str(lhs) + " != " + str(rhs) + " is " + str(d))