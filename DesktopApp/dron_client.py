import dron_app_pb2_grpc
import dron_app_pb2
import grpc
import sys

HOST_ADDRESS = 'localhost:10001'
#HOST_ADDRESS = '192.168.1.68:10001'


def create_pid_configuration(
        _yaw_kp, _yaw_ki, _yaw_kd,
        _pitch_kp, _pitch_ki, _pitch_kd,
        _roll_kp, _roll_ki, _roll_kd):

    pidConfigurationMessage = dron_app_pb2.PIDConfigurationMessage()

    pidConfigurationMessage.yaw_kp = _yaw_kp
    pidConfigurationMessage.yaw_ki = _yaw_ki
    pidConfigurationMessage.yaw_kd = _yaw_kd
    pidConfigurationMessage.pitch_kp = _pitch_kp
    pidConfigurationMessage.pitch_ki = _pitch_ki
    pidConfigurationMessage.pitch_kd = _pitch_kd
    pidConfigurationMessage.roll_kp = _roll_kp
    pidConfigurationMessage.roll_ki = _roll_ki
    pidConfigurationMessage.roll_kd = _roll_kd

    return pidConfigurationMessage

def setPID(pidConfiguration):

    with grpc.insecure_channel(HOST_ADDRESS) as channel:
        stub = dron_app_pb2_grpc.DronStub(channel)
        print(pidConfiguration)
        print(sys.getsizeof(pidConfiguration))
        raspberryResponse = stub.SettingPID(pidConfiguration)
        if(raspberryResponse.successfullyCompleted == 1):
            print("set")
            return True
        else:
            print("error")
            return False
