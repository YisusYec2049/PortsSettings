import serial
import time
from firebase_admin import credentials, initialize_app, db

serial_port = "COM3"
serialArduino = serial.Serial(serial_port, 9600)

firebase_url = "https://prueba-dobot-default-rtdb.firebaseio.com/"
cred_path = "serviceAccountKey.json"

cred = credentials.Certificate(cred_path)
initialize_app(cred, {"databaseURL": firebase_url})

firebase_db = db.reference('/test_firebase/data_post')

def read_and_delete_sign_from_firebase():
    result = firebase_db.get()

    if result:
        last_entry_key = list(result.keys())[-1]
        sign = result[last_entry_key]['sign']
        print("Dato leído desde Firebase:", sign)

        firebase_db.child(last_entry_key).delete()

        return sign
    else:
        return None

def send_sign_to_port(sign):
    cad = f"{sign}"
    serialArduino.write(cad.encode('ascii'))
    print("Dato enviado al puerto serie:", sign)

while True:
    firebase_sign = read_and_delete_sign_from_firebase()

    if firebase_sign:
        send_sign_to_port(firebase_sign)
    
    time.sleep(2)
