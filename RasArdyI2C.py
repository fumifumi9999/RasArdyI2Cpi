#!/usr/bin/python
# -*- coding: utf-8 -*-
import smbus

class RasArdyI2C:
    def __init__(self, Bus, ArduinoAddress):
        self.bus = smbus.SMBus(Bus);
        self.address = ArduinoAddress;
        print(self.address);
        print(Bus);
    
    def receiveByteData(self):
        Byte = self.bus.read_byte_data(self.address, 0x1);
        return(Byte)
    def receiveWordData(self):
        data = self.bus.read_i2c_block_data(self.address,0x1,2);
        Word = int.from_bytes([data[0],data[1]],byteorder='big');
        #print("data[0]:",data[0], ",data[1]:", data[1]);
        return(Word)
    def receiveSomeByteData(self,ByteLength):
        ByteArray = self.bus.read_i2c_block_data(self.address,0x1,ByteLength);
    #    for i in range(ByteLength):
    #        print("data[", i, "]:",hex(ByteArray[i]));
        return(ByteArray)
    def receiveSomeWordData(self,WordLength):
        WordArray = [0]*WordLength;
        ByteArray = self.bus.read_i2c_block_data(self.address,0x1,WordLength*2);
        for i in range(WordLength):
            WordArray[i] = int.from_bytes([ByteArray[i*2],ByteArray[i*2+1]],byteorder='big');
        #    print("WordArray[", i, "]:",hex(WordArray[i]));
        #    print("WordArray[", i, "]:",WordArray[i]);
        return(WordArray)

    def sendByteData(self,Byte):
        Byte = self.bus.write_byte_data(self.address, 0x0, Byte);
    def sendWordData(self,Word):
        ByteArray = Word.to_bytes(2,byteorder='big');
        self.bus.write_i2c_block_data(self.address, 0x0, [ByteArray[0], ByteArray[1]]);
    def sendSomeByteData(self,ByteArray):
        self.bus.write_i2c_block_data(self.address,0x0, ByteArray[0:]);
    def sendSomeWordData(self,WordArray):
        ByteArray = [0]*len(WordArray)*2;
        for i in range(len(WordArray)):
            [ByteArray[i*2],ByteArray[i*2+1]] = WordArray[i].to_bytes(2,byteorder='big');
    #        print("ByteArray[", i*2, "]:",hex(ByteArray[i*2]), ":ByteArray[", i*2+1, "]:",hex(ByteArray[i*2+1]));
        self.bus.write_i2c_block_data(self.address,0x0,ByteArray[0:]);    #        print("ByteArray[", i*2, "]:",hex(ByteArray[i*2]), ":ByteArray[", i*2+1, "]:",hex(ByteArray[i*2+1]));
        self.bus.write_i2c_block_data(self.address,0x0,ByteArray[0:]);
        
if __name__ == '__main__':
    print("single drive");
