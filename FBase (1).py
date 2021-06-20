import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import datetime
import time

cred = credentials.Certificate("detectPL.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def FB_GetNewID():
    new_data = db.collection(u'Data').document()
    return new_data.id

def FB_UploadData(data_id,card_id,bsx):
    car_record = db.collection(u'Data').document(data_id)                      
    data = {
        u'Car_plate' : bsx,
        u'CardID' : card_id,
        u'Time_In' : '',
        u'Time_Out' : '',
    }
    car_record.set(data)   

def FB_CarOut_UploadData(data_id):
    car_record = db.collection(u'Data').document(data_id)
    car_record.update({u'Time_Out' : datetime.datetime.now(), u'Paking': False})
    
def FB_CarIn_UploadData(data_id):
    car_record = db.collection(u'Data').document(data_id)
    car_record.update({u'Time_In' : datetime.datetime.now(), u'Paking': True})

def FB_GetInfoByDataID(data_id):
#     print(data_id)
#     print(type(data_id))
#     db = firestore.client()
    car_ref = db.collection(u'Data').document(data_id)
    doc = car_ref.get()
    print("This is",doc.to_dict())
    if doc.exists:
        return doc.to_dict()['Car_plate']
    else:
        return 'ERROR'
def FB_CheckByDataID(data_id):
    print(data_id)
    print(type(data_id))
    car_ref = db.collection(u'Data').document(data_id)
    doc = car_ref.get()
    print("This is",doc.to_dict())
    if doc.exists:
        return True
    else:
        return False
def FB_CheckCarByPL(pl):
    car_record = db.collection(u'Data').where("Car_plate","==",pl)
    docs=car_record.get()
    if not docs:
        return False , None
    else:
        for doc in docs:
            data_id= doc.id
            return True, data_id
def main():
    check, data_id = FB_CheckCarByPL("80R367Z55")
    print(check, data_id)
    
    
    return

if __name__ == "__main__":
    main()