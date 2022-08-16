#!/usr/bin/env python3
import serial
import time

import dron_app_pb2

SERIAL_PORT = 'COM3'

class SerialConnection:

    def __init__(self):
        self.ser = serial.Serial(SERIAL_PORT, 9600, timeout=1)
        time.sleep(1)
        self.ser.reset_input_buffer()
        print("Serial OK")

    def sendPID(self, pidConfigurationMessage):
        time.sleep(1)
        self.ser.write(pidConfigurationMessage.encode('utf-8'))
        while self.ser.in_waiting <= 0:
            time.sleep(0.01)
        response = self.ser.readline().rstrip()
        print(response)
        return True

    def close_connection(self):
        self.ser.close()
        print("Serial closed")


# pidConfigurationMessage = dron_app_pb2.PIDConfigurationMessage()
#
# pidConfigurationMessage.yaw_kp = 1
# pidConfigurationMessage.yaw_ki = 1
# pidConfigurationMessage.yaw_kd = 1
# pidConfigurationMessage.pitch_kp = 2
# pidConfigurationMessage.pitch_ki = 2
# pidConfigurationMessage.pitch_kd = 2
# pidConfigurationMessage.roll_kp = 3
# pidConfigurationMessage.roll_ki = 3
# pidConfigurationMessage.roll_kd = 3
#
# ser = SerialConnection()
# ser.sendPID(pidConfigurationMessage.SerializeToString())