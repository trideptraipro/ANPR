#Libraries
import RPi.GPIO as GPIO
from time import sleep


#Run forever loop


def buzzer_Active(a):
    #Disable warnings (optional)
    GPIO.setwarnings(False)
    #Select GPIO mode
    GPIO.setmode(GPIO.BOARD)
    #Set buzzer - pin 18 as output
    buzzer=12
    GPIO.setup(buzzer,GPIO.OUT)
    i = 0
    while i < a:
        GPIO.output(buzzer,GPIO.HIGH)
        print ("Beep")
        sleep(0.5) # Delay in seconds
        GPIO.output(buzzer,GPIO.LOW)
        print ("No Beep")
        sleep(0.5)
        i=i+1
    GPIO.cleanup()    

def main():
    buzzer_Active(4)
    GPIO.cleanup()
    return

if __name__ == "__main__":
    main()