# PORTS

import serial
from firebase import firebase
import time

serial_port = "COM3"
serialArduino = serial.Serial(serial_port, 9600)

firebase_url = "https://iadobot-default-rtdb.firebaseio.com/"
firebase = firebase.FirebaseApplication(firebase_url, None)

def read_data_from_firebase():
    result = firebase.get('test_firebase/data_post', None)

    if result:
        data = list(result.values())[-1]
    print("Datos leídos desde Firebase:", data)
    return data

def send_data_to_port(data):
    cad = f"{data}"
    serialArduino.write(cad.encode('ascii'))
    print("Datos enviados al puerto serie:", data)

while True:
    firebase_data = read_data_from_firebase()

    if firebase_data:
        send_data_to_port(firebase_data)

    time.sleep(2)


# firebase

'''
from firebase import firebase

firebase = firebase.FirebaseApplication("https://iadobot-default-rtdb.firebaseio.com/", None)

def send_data(data):
    result = firebase.post('test_firebase/data_post', data)
    print("Datos enviados:", data)
    return result

def read_data():
    result = firebase.get('test_firebase/data_post', None)
    print(result)
    return result 
'''
'''
from firebase import firebase
import time

firebase_url = "https://iadobot-default-rtdb.firebaseio.com/"
firebase = firebase.FirebaseApplication(firebase_url, None)

def sent_data_to_firebase(sign):
    data = {
        'sign': sign,
        'timestamp': time.time() 
    }
    result = firebase.post('test_firebase/data_post', data)
    print("Datos enviados a Firebase:", data)
    return result

while True:
    sign = input('Ingrese el valor del sign: ')
    sent_data_to_firebase(sign)
    time.sleep(2)
'''






        
