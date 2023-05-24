import time
import RPi.GPIO as GPIO
import camfinal
from gpiozero import Servo

servoPipe = Servo(25)
servoGate = Servo(24)

servoPipe.detach()
servoGate.detach()
count = 0

def gate():
    servoGate.max()
    time.sleep(0.5)
    servoGate.detach()
    time.sleep(4)
    servoGate.min()
    time.sleep(0.6 )
    servoGate.detach()        
while True:  
    k = camfinal.camera()
    #print(k)
    if count == 0 or count == 2 or count == 3:
        k = 0
    else:
        k = 1
    count = count+1
    if count == 5:
          count = 0
    while k == 1:
        servoPipe.max()
        time.sleep(0.7)
        servoPipe.detach()
        time.sleep(2)
        gate()
        time.sleep(2)
        servoPipe.min()
        time.sleep(0.7)
        servoPipe.detach()
        break
     
    while k == 0:
        servoPipe.min()
        time.sleep(0.7)
        servoPipe.detach()
        time.sleep(2)
        gate()
        time.sleep(2)
        servoPipe.max()
        time.sleep(0.7)
        servoPipe.detach()
        break

    # GPIO.cleanup()


  