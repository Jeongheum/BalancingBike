import RPi.GPIO as GPIO
from time import sleep

## pin setting ##
GPIO.setwarnings(False)
pwm1 = 14
dir1 = 15
brk1 = 18
pwm2 = 2
dir2 = 3
brk2 = 4
speed = 50
freq = 100
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm1, GPIO.OUT)
GPIO.setup(dir1, GPIO.OUT)
GPIO.setup(brk1, GPIO.OUT)
GPIO.setup(pwm2, GPIO.OUT)
GPIO.setup(dir2, GPIO.OUT)
GPIO.setup(brk2, GPIO.OUT)

pwm1 = GPIO.PWM(pwm1, freq)
pwm2 = GPIO.PWM(pwm2, freq)
pwm1.start(0)
pwm2.start(0)
 
## define function
def moveMotor(dir): ## dir: 0(forward), 1(backward), 2(left), 3(right)
    if dir==0:
        d1 = True
        d2 = True
    elif dir==1:
        d1 = False
        d2 = False
    elif dir==2:
        d1 = True
        d2 = False
    else:
        d1 = False
        d2 = True
    GPIO.output(dir1, d1)
    GPIO.output(dir2, d2)
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
 
def stopMotor(sec): ## stop the motors for input time
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    sleep(sec)
     
## move motor: repetetivley go straight for 3 seconds and turn left 1 second
 
sleep(3)
for i in range(0,5):
    moveMotor(0) ## move forward
    sleep(5)
    stopMotor(1)
    moveMotor(2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    sleep(2)
    stopMotor(1)
 
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
