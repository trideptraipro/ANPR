import buzzer as bz
import FBase as fb
import Rasp_Cam as rc
import RFID
from Servo import MyServo
import Main
import PIR
import time


msv=MyServo()

def CheckCarIn():
    while True:
        try:
            PIR.CheckPIR()
            rc.RC_CarIn_TakePic()
            bsx =Main.DetectPL('pl.jpg')
            if bsx == None:
                print ('No plate detected')
            else:
                check, data_id = fb.FB_CheckCarByPL(bsx)
                if check:
                    fb.FB_CarIn_UploadData(data_id)
                    bz.buzzer_Active(1)
                    #Update Time In and Open Barier
                    msv.Servo_Open()
                    print("Having a nice day!!")
                else:
                    print("ERROR!!")
                    bz.buzzer_Active(1)
            time.sleep(0.5)
        except KeyboardInterrupt:
            break
def DangKy():
    PIR.CheckPIR()
    rc.RC_CarIn_TakePic()
    bsx = Main.DetectPL('pl.jpg')
    if bsx == None:
        print ('No plate detected')
    else:
        check, data_id = fb.FB_CheckCarByPL(bsx)
        if check:
            if (RFID.DetectRFID()):
                RFID.WriteRFID(data_id)
        else:
            if(RFID.DetectRFID()):
                uid,text = RFID.ReadData()
                dataID = fb.FB_GetNewID()
                RFID.WriteRFID(dataID)
                fb.FB_UploadData(dataID,uid,bsx)
                bz.buzzer_Active(1)
                print("Having a nice day!!")
        #endif
    #endif
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
                fb.FB_CarIn_UploadData(dataID)
                bz.buzzer_Active(1)
                msv.Servo_Open()
                print("Having a nice day!!")
            else:
                print("Card error")
        time.sleep(0.5)
    
from threading import Thread    
def Check():
    try:
        t1= Thread(target=CheckRFID)
        t2= Thread(target=CheckCarIn)
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
    print('1.Dang ky xe')
    print('2.Nhan dien xe')
    print('3.Ket thuc')
    option=int(input('Vui long chon:'))
    def default():
        print ('Chon sai')
    dict={
        1:DangKy,
        2:Check,
        3:Exit
        }
    dict.get(option, default)()
if __name__ == "__main__":
    while True:
        switch()
    