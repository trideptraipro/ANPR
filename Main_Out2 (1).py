import buzzer as bz
import FBase as fb
import Rasp_Cam as rc
import RFID
from Servo import MyServo
import Main
import PIR

sv= MyServo()
# while True:
#     if(RFID.DetectRFID()):
#         uid,text = RFID.ReadData()
#         dataID = fb.FB_GetNewID()
#         RFID.WriteRFID(dataID)
#         rc.RC_CarIn_TakePic()
#         bsx = Main.DetectPL('pl.jpg')
# #         print('Nhap bien so xe:')
# #         bsx=input()
#         fb.FB_CarIn_UploadData(dataID,uid,bsx)
#         bz.buzzer_Active(1)
#         sv.Servo_Open()
#         print("Having a nice day!!")
def CheckCarOut():
    while True:
        PIR.CheckPIR()
        rc.RC_CarOut_TakePic()
        bsx =Main.DetectPL('bsx.jpg')  
        check, data_id = fb.FB_CheckCarByPL(bsx)
        if check:
            fb.FB_CarOut_UploadData(data_id)
            bz.buzzer_Active(1)
            #Update Time In and Open Barier
            sv.Servo_Open()
            print("Having a nice day!!")
        else:
            print("ERROR!!")
            bz.buzzer_Active(1) 
    
def CheckRFID():
    while True:
        if(RFID.DetectRFID()):
            uid,text = RFID.ReadData()
            dt_tol= list(text)
            dataID = ""
            for i in dt_tol:
                if i != ' ':
                    dataID += i
            if (fb.FB_CheckByDataID(dataID)):
                fb.FB_CarOut_UploadData(dataID)
                bz.buzzer_Active(1)
                sv.Servo_Open()
                print("Having a nice day!!")
from threading import Thread  
def Check():
    try:
        t1= Thread(target=CheckRFID)
        t2= Thread(target=CheckCarOut)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except:
        print("error")
import sys
def Exit():
    sys.exit()
def switch():
    print('1.Check')
    print('2.Exit')
    option=int(input('Vui long chon:'))
    def default():
        print ('Chon sai')
    dict={
        1:Check,
        2:Exit
        }
    dict.get(option, default)()
if __name__ == "__main__":
    while True:
        switch()