#!/usr/bin/env python3
import serial
import time

import dron_app_pb2

#SERIAL_PORT = '/dev/ttyACM0'
SERIAL_PORT = 'COM3'

class SerialConnection:

    def __init__(self):
        self.ser = serial.Serial(SERIAL_PORT, 9600, timeout=1)
        time.sleep(1)
        self.ser.reset_input_buffer()
        print("Serial OK")

    # def sendPID(self, pidConfigurationMessage):
    #     time.sleep(1)
    #     self.ser.write(pidConfigurationMessage.encode('utf-8'))
    #     while self.ser.in_waiting <= 0:
    #         time.sleep(0.01)
    #     response = self.ser.readline().decode('utf-8').rstrip()
    #     print(response)
    #
    #     return True

    def sendPID(self, pidConfigurationMessage):
        time.sleep(1)
        pidConfigurationMessageSerialized = pidConfigurationMessage.SerializeToString()
        self.ser.write(pidConfigurationMessageSerialized)
        while self.ser.in_waiting <= 0:
            time.sleep(0.01)
        response = int(self.ser.readline().decode('utf-8').rstrip())
        #print(response)
        if(response == 1):
            return True
        else:
            return False

    def close_connection(self):
        self.ser.close()
        print("Serial closed")



# pidConfigurationMessage = dron_app_pb2.PIDConfigurationMessage()
#
# pidConfigurationMessage.yaw_kp = 99
# pidConfigurationMessage.yaw_ki = 99
# pidConfigurationMessage.yaw_kd = 99
# pidConfigurationMessage.pitch_kp = 99
# pidConfigurationMessage.pitch_ki = 99
# pidConfigurationMessage.pitch_kd = 99
# pidConfigurationMessage.roll_kp = 99
# pidConfigurationMessage.roll_ki = 99
# pidConfigurationMessage.roll_kd = 99
#
# ser = SerialConnection()
# send = ser.sendPID(pidConfigurationMessage)
# print(send)