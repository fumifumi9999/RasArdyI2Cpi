#!/usr/bin/python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import csv
import time
from datetime import datetime
from RasArdyI2C import RasArdyI2C

i2c = RasArdyI2C(1, 0x4); #(BusName, ArduinoI2cAddress)
triggerInputPin = 4;
plus = 0;

def callbackFromDue10ms(triggerInputPin):
    global plus;
    #-------receive--------
    #Byte = i2c.receiveByteData();
    #Word = i2c.receiveWordData();
    #ByteArray = i2c.receiveSomeByteData(5);
    WordArray = i2c.receiveSomeWordData(5);
    for i in range(5):
        print(hex(WordArray[i])+ ",", end="");
    plus += 1;
    print(plus);

    #---------send---------
    #i2c.sendByteData(testByte);
    #i2c.sendWordData(testWord);
    #i2c.sendSomeByteData(testByteArray);
    testWordArray = [  1000,   2000,   3000,   4000];
    i2c.sendSomeWordData(testWordArray);

GPIO.setmode(GPIO.BCM);
GPIO.setup(triggerInputPin, GPIO.IN);
GPIO.add_event_detect(triggerInputPin, GPIO.BOTH);
GPIO.add_event_callback(triggerInputPin, callbackFromDue10ms);

try:
    plus = 0;
    while True:
        time.sleep(1);

finally:
    GPIO.cleanup();

