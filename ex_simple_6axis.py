'''
==========================================================
Pre-requisite on RaspberryPi
open terminal
sudo raspi-config > 3 Interface Options > P5 I2C > Enable Yes > Finish
sudo vi /etc/modules
  --> add 'i2c-dev' at the last line

sudo apt-get install i2c-tools
sudo apt-get install python-smbus
sudo i2cdetect -y 1
  --> you can see 68 (MPU6050 address) on the screen
==========================================================
'''    

import smbus
import math
import time
import RPi.GPIO as GPIO

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    
    if val >= 0x8000:
        return -((65535-val)+1)
    else:
        return val
    
def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus.SMBus(1) # 0 for old rpi

address = 0x68

bus.write_byte_data(address, power_mgmt_1, 0)

try:
    while True:
        time.sleep(1)
        
        print('--------------------------------')
        print('==> gyro data')
        print('----------')
        gyro_xout = read_word_2c(0x43)
        gyro_yout = read_word_2c(0x45)
        gyro_zout = read_word_2c(0x47)
        print('gyro_xout: ', gyro_xout, " scaled: ", (gyro_xout/131))
        print('gyro_yout: ', gyro_yout, " scaled: ", (gyro_yout/131))
        print('gyro_zout: ', gyro_zout, " scaled: ", (gyro_zout/131))
        
        print('')
        print('==> accelerometer data')
        print('----------------------')
        acc_xout = read_word_2c(0x3b)
        acc_yout = read_word_2c(0x3d)
        acc_zout = read_word_2c(0x3f)
        acc_xout_s = acc_xout/16384.0
        acc_yout_s = acc_yout/16384.0
        acc_zout_s = acc_zout/16384.0
        print('acc_xout: ', acc_xout, " scaled: ", (acc_xout_s/131))
        print('acc_yout: ', acc_yout, " scaled: ", (acc_yout_s/131))
        print('acc_zout: ', acc_zout, " scaled: ", (acc_zout_s/131))
        
        print('x rotation: ', get_x_rotation(acc_xout_s, acc_yout_s, acc_zout_s))
        print('y rotation: ', get_y_rotation(acc_xout_s, acc_yout_s, acc_zout_s))
        print('--------------------------------')
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
finally:
    GPIO.cleanup()
    
