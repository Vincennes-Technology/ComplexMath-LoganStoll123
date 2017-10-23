#!/usr/bin/python
#Lstoll
#Complex beginning
def complexAdd(a, b):
    realAnswer = a[0] + b[0]
    imageAnswer = a[1] + b[1]
    return (realAnswer,imageAnswer)
print complexAdd((1,2),(3,1))
def complexSubtract(a, b):
    realAnswer = a[0] - b[0]
    imageAnswer = a[1] - b[1]
    return (realAnswer,imageAnswer)
print complexSubtract((2,2),(1,1))

def complexMultiply(a, b):
    realAnswer = a[0] * b[0]
    imageAnswer = a[1] * b[1]
    return (realAnswer,imageAnswer)
print complexMultiply((2,3),(2,4))
def complexDivide (a, b):
    realAnswer = a[0] / b[0]
    imageAnswer = a[1] / b[1]
    return (realAnswer,imageAnswer)
print complexDivide((8,8),(2,4))

