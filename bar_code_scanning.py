#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from time import sleep
from ev3dev2.motor import MoveTank, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B,OUTPUT_C   #we're importing the motor function
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM 

cl = ColorSensor() 
ts = TouchSensor()
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B)
# Stop program by long-pressing touch sensor button
#his program will make the color sensor display RGB colors together
sm = MediumMotor(OUTPUT_A)
#sm.on_for_seconds(speed = -20, seconds = 8)
#sm.on_for_seconds(speed = -20, seconds = 8)
sm.on_for_seconds(speed = 20, seconds = 8) 
tank_pair.on_for_degrees(10,10,726)
tank_pair.on_for_degrees(10,-10,180) 

while not ts.is_pressed:
    # rgb is a tuple containing three integers
    # each 0-255 representing the amount of
    # red, green and blue in the reflected light
    print(cl.rgb)
    red = cl.rgb[0]
    green=cl.rgb[1]
    blue=cl.rgb[2]

    if red > 10 and green > 10 and blue > 10:
        tank_pair.on_for_degrees(3,3,45)
        tank_pair.on_for_degrees(-10,10,180)
        tank_pair.on_for_degrees(-3,-3,180)
        sm.on_for_seconds(speed = -20, seconds = 8)
        tank_pair.on_for_degrees(3,3,200)
        sm.on_for_seconds(speed = 20, seconds = 9.5)
        tank_pair.on_for_degrees(-3,-3,250)
        tank_pair.on_for_degrees(10,-10,345)
        tank_pair.on_for_degrees(10,10,500)
        tank_pair.on_for_degrees(10,-10,170)
        tank_pair.on_for_degrees(10,10,420)
        tank_pair.on_for_degrees(10,-10,180)
        sm.on_for_seconds(speed = -20, seconds = 10)

        break
    else:
    #tank_pair.on_for_degrees(3,3,27)
        tank_pair.on_for_degrees(20,20,27)


    print("Red: "+str(red)+", Green: "+str(green)+", Blue: "+str(blue)+'\n')
    # '\n' is the newline character so an extra (blank) line is printed
    sleep(1)
