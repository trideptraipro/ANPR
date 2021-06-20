import buzzer as bz
import FBase as fb
import Rasp_Cam as rc
import RFID
import Servo as sv

while True:
    if(RFID.DetectRFID()):
        uid,text = RFID.ReadData()
        dt_tol= list(text)
        dataID = ""
        for i in dt_tol:
            if i != ' ':
                dataID += i
        if (fb.FB_CheckByDataID(dataID)):
            bz.buzzer_Active(1)
            sv.Servo_Open()
            print("Having a nice day!!")
        