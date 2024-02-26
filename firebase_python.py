import json
import time
from firebase_admin import credentials, initialize_app, db

firebase_url = "https://prueba-dobot-default-rtdb.firebaseio.com/"
cred_path = "PortsSettings\serviceAccountKey.json"


cred = credentials.Certificate(cred_path)
initialize_app(cred, {"databaseURL": firebase_url})

firebase_db = db.reference('/test_firebase/data_post')

def sent_data_to_firebase(sign):
    data = {
        'sign': sign,
        'timestamp': time.time() 
    }
    result = firebase_db.push(data)
    print("Datos enviados a Firebase:", data)
    return result

while True:
    sign = input('Ingrese el valor del sign: ')
    sent_data_to_firebase(sign)
    time.sleep(2)
