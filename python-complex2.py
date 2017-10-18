#!/usr/bin/python
#Lstoll
#Complex 2 (10/18/17)

import math
pi = 3.1415926535897932384626433

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


def rect_to_polar(x, y):
    angle = math.atan((y/x))
    angle = angle * (180/pi)
    magnitude = (math.sqrt((x*x)+(y*y)))
    answer = magnitude, angle
    return answer


def polar_to_rect(polar_num):
    y = polar_num[0] * (math.sin(polar_num[1] * pi/180))
    x = polar_num[0] * (math.cos(polar_num[1] * pi/180))
    rect = x, y
    return rect


def magnitude(number):
    absolute = math.sqrt((number[0] * number[0]) + (number[1]* number[1]))
    return absolute

# Getting the basic information from the user.

# coordinate_system = raw_input('Greetings User! Shall you be working in rectangular or polar format today?:\n')
print('For this particular experiment, I (the pi) am only capable of series AC calculations with one R, L & C.\n')
frequency = input('\nWhat is the frequency of the source? (Hz): ')
voltage = input('\nWhat is the voltage of the source? (RMS): ')
resistor_value = input('\nWhat value of resistor is present? (Ohms): ')
inductor_value = input('\nWhat is the value of your inductor? (Henrys): ')
capacitor_value = input('\nWhat is the value of your capacitor? (Farads): ')

# Some basic calculations
omega = 2 * pi * frequency
inductance = omega * inductor_value
capacitance = (1/(omega * capacitor_value))
impedance = resistor_value, (inductance + -capacitance)
mag_impedance = magnitude(impedance)
current = float(voltage) / float(mag_impedance)
v_r = current * resistor_value
v_l = current * inductance
v_c = current * capacitance
print('\nYour total impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))
print('That means the magnitude of your impedance is: %.2f' % mag_impedance)
print('Which then means your current is: %f A' % current)
print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (v_r, v_l, v_c))
