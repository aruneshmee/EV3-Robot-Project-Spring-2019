#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds
from time import sleep
from ev3dev2.motor import MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B,OUTPUT_C   #we're importing the motor function
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM #we're importing other functions related to speed

#sm = MediumMotor(OUTPUT_C)  #defining a large motor
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
# Connect ultrasonic sensor to any port 1,2 or 3 or 4

us = UltrasonicSensor()

while True: 
  if us.distance_centimeters > 10:
    tank_pair.on(10,10)
  else:
    tank_pair.on_for_degrees(-10,-10,180)
    tank_pair.on_for_degrees(-10,10,150)
