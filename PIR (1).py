from gpiozero import MotionSensor
import time

pir=MotionSensor(4)

def CheckPIR():
    print('waiting car')
    pir.wait_for_motion()
#     pir.wait_for_no_motion
#     print (456)
    time.sleep(0.3)
    #end
import Rasp_Cam as rc
def CheckPIRtoTakePhotoOut():
    pir.wait_for_motion()
    rc.RC_CarOut_TakePic()
    time.sleep(0.1)
def CheckPIRtoTakePhoto():
    pir.wait_for_motion()
    rc.RC_CarIn_TakePic()
    time.sleep(0.1)
if __name__ == "__main__":
    while True:
        CheckPIRtoTakePhoto()
    