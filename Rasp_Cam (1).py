from picamera import PiCamera
from time import sleep
import datetime
camera = PiCamera()
def getFileName():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
def RC_CarIn_TakePic():
    path = '/home/pi/Desktop/CarIn/'+getFileName()
    pl='pl.jpg'
    camera.start_preview()
    sleep(3)
    camera.capture(path)
    camera.capture(pl)
    camera.stop_preview()
def RC_CarOut_TakePic():
    #picname = dataID
    path = '/home/pi/Desktop/CarOut/'+getFileName()
    bsx = 'bsx.jpg'
    camera.start_preview()
    sleep(3)
    camera.capture(path)
    camera.capture(bsx)
    camera.stop_preview()
    
def main():
    RC_CarIn_TakePic()
    return

if __name__ == "__main__":
    main()
    