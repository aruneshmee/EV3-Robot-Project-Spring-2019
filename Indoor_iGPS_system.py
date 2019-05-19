#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.sound import Sound
from time import sleep
import math

J= 89.196
K = 46.86
r3 = 75.18

L = 120

x = (J * math.sin(math.acos((J*J + L*L - K*K) / (2 * J * L)))) + 6
y = (J * math.cos(math.acos((J*J + L*L - K*K) / (2 * J * L)))) - 6

print('    ') 
print('    ') 
print('    ')
print("Dist A: "+str(J)+" , Dist C: "+str(K)+" , Dist D: "+str(r3)+'\n')
print('    ')
print("X Coord: "+str(x)+" , Y Coord: "+str(y))

sleep(20)
