import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def DetectRFID():
    print('Waiting for card')
    uid,text = reader.read()
    print('Card Detected')
    return True
    
def ReadData():
    uid,text = reader.read()
    print('Read success')
    print('DataID:' , text)
    print('CardID:' , uid)
    return uid,text

def WriteRFID(dataID):
    print('Waiting for card to write')
    text = dataID
    reader.write(text)
    print('Write success')
    

def ClearRFID():
    print('Waiting for card to clear')
    text = ""
    reader.write(text)
    print('Clear success')
    
    
def main():
    uid,text = ReadData()
    print(type(text))
    bsx = 'smth'
    print(type(bsx))
    GPIO.cleanup()
    return

if __name__ == "__main__":
    main()
