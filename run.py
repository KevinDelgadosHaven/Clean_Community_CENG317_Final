#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
from si7021 import *
from CCS811run import *

def ledRun():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(12,GPIO.OUT)
    for x in range(3):
        print ("LED on")
        GPIO.output(12,GPIO.HIGH)
        time.sleep(1)
        print ("LED off")
        GPIO.output(12,GPIO.LOW)
        time.sleep(1)

lcd_rs = 4
lcd_en = 17
lcd_d4 = 18
lcd_d5 = 22
lcd_d6 = 23
lcd_d7 = 24

lcd_backlight = 4

lcd_columns = 16
lcd_rows    = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.show_cursor(True)
time.sleep(2.0)
lcd.clear()
lcd.show_cursor(False)
lcd.message("Humidity:{0:0.2f}\nTemperature:{1:0.2f}".format(humidity, celsTemp))
time.sleep(5.0)
lcd.clear()
lcd.message("CO2:{0:0.2f}\ntVOC:{1:0.2f}".format(CO2, tVOC))
ledRun()
lcd.clear()
lcd.message("Done")