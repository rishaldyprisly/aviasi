import cv2
from time import sleep
import keyboard
import pymysql.cursors
import uuid
import sys
import socket
import os
import subprocess

key = cv2.waitKey(1)
HOST = 'localhost' 
PORT = 6668

webcam = cv2.VideoCapture(1)
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))


connection = pymysql.connect(host='av-parking-3.local',
                             port=3306,
                             user='root',
                             password='ANJING',
                             db='avparkin_parking',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData



while True:
        
        s.listen()
        conn, addr = s.accept()
        z = conn.recv(10)
        print(z)
        
            
        if (b'snap' in z):
            check, frame = webcam.read()
            print(check) 
            print(frame) 
            cv2.imshow("Capturing", frame)
            filename = str(uuid.uuid4()).replace('-','')+'.jpg'
            cv2.imwrite(filename, img=frame)
            img_ = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(img_,(350,250))
            print("Resized...")
            img_resized = cv2.imwrite(filename=filename, img=img_)
            print("Image saved!")
            with connection.cursor() as cursor:
               sql = "UPDATE Check_In SET Img = (%s)"
               files = convertToBinaryData(filename)
               cursor.execute(sql, (files))
               connection.commit()
               os.remove(filename)
               
                
                
        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break
