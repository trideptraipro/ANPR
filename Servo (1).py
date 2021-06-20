# Import libraries
import RPi.GPIO as GPIO
import time


class MyServo:
    duty=2
    def __init__(self):
        self.duty=2
        
    def Servo_Open(self):
        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BOARD)
        servo=11
        # Set pin 17 as an output, and set servo1 as pin 17 as PWM
        GPIO.setup(servo,GPIO.OUT)
        servo1 = GPIO.PWM(servo,50) # Note 17 is pin, 50 = 50Hz pulse
        #start PWM running, but with value of 0 (pulse off)
        servo1.start(2.5)
        self.duty=2
        # Loop for duty values from 2 to 12 (0 to 180 degrees)
        while self.duty <= 7:
            servo1.ChangeDutyCycle(self.duty)
            time.sleep(0.3)
            self.duty = self.duty + 5
        print ("Gate Open!!")
        #GPIO.cleanup()
        time.sleep(5)
#     def Servo_Close(self):    
        #turn back to 0 degrees
        self.duty=2
        print ("Turning back to 0 degrees")
        servo1.ChangeDutyCycle(self.duty)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

        #Clean things up at the end
        servo1.stop()
#         GPIO.cleanup()
        print ("Gate Close!!")

def main():
    sv=MyServo()
    sv.Servo_Open()
    
    return

if __name__ == "__main__":
    main()