import smbus
import time
import psutil

bus = smbus.SMBus(1)

DEVICE = 0x20
IODIRA = 0x00
IODIRB = 0x01
RIGHTLED = 0x15
LEFTLED = 0x14 
GPIOA = 0x12

binarylist = [128,128,192,224,240,248,252,254,255,255]

#define all GPB pins as output
bus.write_byte_data(DEVICE,IODIRB,0x00)

#define all GPA pins as output
bus.write_byte_data(DEVICE,IODIRA,0x00)

def getCPU():
    cpuNum = int(psutil.cpu_percent()/10)
    bus.write_byte_data(DEVICE,LEFTLED,binarylist[cpuNum])
    bus.write_byte_data(DEVICE,RIGHTLED,binarylist[cpuNum])
    print(cpuNum)
    
while True:
    
    time.sleep(0.05)
    getCPU()
