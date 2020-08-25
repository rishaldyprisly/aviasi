import socket
import sys





#results1 = bytes(result1, encoding= 'utf-8') #Translating Bytes To String


HOST = 'localhost' # IP Address PC Kasir - Ganti Baris Ini

PORT = 6667 # Sock Port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
   # data = 'result'
    s.sendall(b'snap')
    s.close()
#print(result)
            

