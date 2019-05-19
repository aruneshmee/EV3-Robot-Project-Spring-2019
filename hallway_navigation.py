#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveTank, SpeedPercent, MediumMotor  
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM 
from ev3dev2.sensor.lego import TouchSensor, GyroSensor, UltrasonicSensor, TouchSensor, ColorSensor
from time import sleep
from ev3dev2.sound import Sound
import math
import os
import sys
import time

gy = GyroSensor()
#us = UltrasonicSensor()
#ts = TouchSensor()
#col = ColorSensor()
lm = LargeMotor('outB')    #defining a large motor
rm = LargeMotor('outC')
#sm = MediumMotor('outA')
tank_drive = MoveTank('outB','outC')

COMMAND_RESET = 'reset'

gy.mode = 'GYRO-RATE'
gy.mode = 'GYRO-ANG'

n = 100   # Enter distance in cm here
L = []

d = (n*16.51)

while lm.degrees < d:
    tank_drive.on(SpeedPercent(20),SpeedPercent(20))
    while gy.angle > 0:
        tank_drive.on(SpeedPercent(20),SpeedPercent(24))
    tank_drive.on(SpeedPercent(20),SpeedPercent(20))
    while gy.angle < 0:
        tank_drive.on(SpeedPercent(24),SpeedPercent(20))
    tank_drive.on(SpeedPercent(20),SpeedPercent(20))
tank_drive.off

rm.run_forever(speed_sp = 100), lm.run_forever(speed_sp = -100)
gy.mode = 'GYRO-RATE'
gy.mode = 'GYRO-ANG'

while abs(gy.angle) < 90:
    print(gy.angle)
tank_drive.on_for_degrees(20,20,(76.2*16.51))
