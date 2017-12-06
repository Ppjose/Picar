import socket
import time
import sys


class MotorController(object):
    def __init__(self, ip="localhost", port=8002):
        self.ip = ip
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.motor = Motor()
        
    def connect(self):
        print("Connectin to server at ", self.ip, " ", self.port)
        self.client_socket.connect((self.ip, self.port))

    def start(self):
        data = self.client_socket.recv(2048)

        if data.strip() == "start":
            while True:
                data = self.client_socket.recv(2048)
                direction = data.split(", ")
                print(direction)

                # code to run motor

                if data.strip() == "dack":
                    self.close()

    def close(self):
        self.client_socket.close()
        sys.exit()


mC = MotorController("localhost", 8002)
mC.connect()
mC.start()
