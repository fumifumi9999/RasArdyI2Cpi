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

def callbackFromDue10ms(triggerInputPin):
    print("");
    #-------receive--------
    #Byte = receiveByteData();
    #print("Byte:",hex(Byte));

    #Word = receiveWordData();
    #print("Word:",hex(Word));
    #print("Word:",Word);

    #ByteArray = receiveSomeByteData(5);
    #for i in range(5):
    #    print("data[", i, "]:",ByteArray[i]);
    #for i in range(5):
    #    print("data[", i, "]:",hex(ByteArray[i]));

    #WordArray = receiveSomeWordData(5);
    #for i in range(5):
    #    print("data[", i, "]:",WordArray[i]);
    #for i in range(5):
    #    print("data[", i, "]:",hex(WordArray[i]));

    #---------send---------
    #testByte = 0x2d;
    #sendByteData(testByte);

    #testWord = 1234;
    #testWord = 0x1234;
    #sendWordData(testWord);

    #testByteArray = [  1,   2,   3,   4,   5];
    #testByteArray = [0x1, 0x2, 0x3, 0x4, 0x5];
    #sendSomeByteData(testByteArray);

    testWordArray = [  1000,   2000,   3000,   4001];
    #testWordArray = [0x1000, 0x2000, 0x3000, 0x4000];
    i2c.sendSomeWordData(testWordArray);

GPIO.setmode(GPIO.BCM);
GPIO.setup(triggerInputPin, GPIO.IN);
GPIO.add_event_detect(triggerInputPin, GPIO.BOTH);
GPIO.add_event_callback(triggerInputPin, callbackFromDue10ms);

if __name__ == '__main__':
    try:

        while True:
            time.sleep(1);

    finally:
        GPIO.cleanup();

