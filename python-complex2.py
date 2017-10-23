#!/usr/bin/python
#LoganStoll123
#Complex 2 (10/23/17)

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
mode_select = raw_input


# coordinate_system = your_input
frequency = input('\nWhat is the frequency of the source? (Hz): ')
voltage = input('\nWhat is the voltage of the source? (RMS): ')
resistor_value = input('\nWhat value of resistor is present? (Ohms): ')
inductor_value = input('\nWhat is the value of your inductor? (Henrys): ')
capacitor_value = input('\nWhat is the value of your capacitor? (Farads): ')
inductor_resistance = input('\nWhat is the resistance of the wiring of the inductor? ( Ohms): ')

# calculations
total_resistance = inductor_resistance + resistor_value
inductance = 2 * pi * frequency * inductor_value
capacitance = (1/(2 * pi * frequency * capacitor_value))
impedance = resistor_value, (inductance + -capacitance)
mag_impedance = magnitude(impedance)
mag_inductance = (inductor_resistance, inductance)
mag_inductance = magnitude(mag_inductance)
current = float(voltage) / float(mag_impedance)
v_r = current * resistor_value
v_l = current * inductance
v_c = current * capacitance

# theta 
if inductance > capacitance:
    argument_send = impedance[1] / impedance[0]
else:
    if capacitance > inductance:
        argument_send = impedance[0] / impedance[1]
    else:
        argument_send = 0

phase_radians = math.atan(argument_send)
phase_angle = phase_radians * 180/pi

if inductance > capacitance:
    print('Your current will lag your voltage by %f degrees' % phase_angle)
if capacitance > inductance:
    print('Your current will lead your voltage by %f degrees ' % phase_angle)    
    
print('\nYour total impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))
print('That means the magnitude of your impedance is: %.2f' % mag_impedance)
print('Which then means your current is: %f A' % current)
print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (v_r, v_l, v_c))

# parallel
if (mode_select == 'Parallel') or (mode_select == 'parallel'):
    print('This experiment I will be performing parallel calculations. One R,L, and C is expected')
    print('If a value is not present, please type 0')
    frequency = input('\nWhat is the frequency of the source? ( Hz): ')
    voltage = input('\nWhat is the voltage of the source? ( RMS): ')
    resistor_value = input('\nWhat value of resistor is present? ( Ohms): ')
    inductor_value = input('\nWhat is the value of your inductor? ( Henrys): ')
    inductor_resistance = input('\nWhat is the resistance of the wiring of the inductor? ( Ohms): ')
    capacitor_value = input('\nWhat is the value of your capacitor? ( Farads): ')

# calculations
    inductance = inductor_resistance, 2 * pi * frequency * inductor_value
    capacitance = 0, 1 / (2 * pi * frequency * capacitor_value)
    polar_capacitance = rect_to_polar(capacitance[0], -capacitance[1])
    polar_inductance = rect_to_polar(inductance[0], inductance[1])
    resistance = resistor_value, 0
    one = 1, 0
    inverse_p_capacitance = complex_division(one, polar_capacitance)
    inverse_p_inductance = complex_division(one, polar_inductance)
    inverse_p_resistance = complex_division(one, resistance)
    denominator = complex_add(inverse_p_capacitance, inverse_p_inductance)
    denominator_f = complex_add(denominator, inverse_p_resistance)
    total_impedance = complex_division(one, denominator_f)
    







