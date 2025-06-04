from picamera import PiCamera
import time
import predictest
import cv2
import RPi.GPIO as GPIO

sensor = 23 
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
def camera():
    print(GPIO.input(sensor))
    try:
        while True:
            if GPIO.input(sensor):
                print("Code reached here")
                time.sleep(5)
                camera = PiCamera()
#                 time.sleep(2)
                #camera.capture("/home/ananya/Desktop/wastebasket/waste.jpg"
                camera.capture("path.jpg")
                print("Done.")
                camera.close()
                test_img = cv2.imread("/file_path.jpg")
                #
                result = predictest.prediction(test_img)
#                 while GPIO.input(sensor):
#                     time.sleep(0.2)
                return result
                
            else:
                print(GPIO.input(sensor))

    except KeyboardInterrupt:
        GPIO.cleanup()

    
