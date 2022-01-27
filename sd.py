'''
Project   :- PICO LOGGER 
Developed :- SB-COMPONENTS
Date      :- 16/06/2021
Firmware  :- Demo code  for PICO LOGGER
CODE DISCREPTION :-
                   
'''
from machine import Pin, SPI ,UART
import sdcard
import os
import utime

uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def sdtest(data):
    spi=SPI(1,sck=Pin(10),mosi=Pin(11),miso=Pin(8))
    sd=sdcard.SDCard(spi,Pin(9))
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/fc")
    print("Filesystem check")
    print(os.listdir("/fc"))

    fn = "/fc/File.txt"
    print()
    print("Single block read/write")
    with open(fn, "a") as f:
        n = f.write(data)  
        print(n, "bytes written")

    with open(fn, "r") as f:
        result2 = f.read()
        print(len(result2), "bytes read")

    os.umount("/fc")
while True:
    sdtest('hello')
    utime.sleep(0.5)