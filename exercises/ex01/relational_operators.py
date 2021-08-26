"""EX01 Relational Operators."""
__author__ = "730448488"

lhs = input("Left-hand side: ")
rhs = input("Right-hand side: ")

intlhs = int(lhs)
intrhs = int(rhs)

a = intlhs < intrhs
print(lhs + " < " + rhs + " is " + str(a))

b = intlhs >= intrhs
print(lhs + " >= " + rhs + " is " + str(b))

c = intlhs == intrhs
print(lhs + " == " + rhs + " is " + str(c))

d = intlhs != intrhs
print(lhs + " != " + rhs + " is " + str(d))