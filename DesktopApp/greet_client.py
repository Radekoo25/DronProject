import dron_app_pb2_grpc
import dron_app_pb2
import grpc

HOST_ADDRESS = 'localhost:10001'


def create_pid_configuration(
        _yaw_kp, _yaw_ki, _yaw_kd,
        _pitch_kp, _pitch_ki, _pitch_kd,
        _roll_kp, _roll_ki, _roll_kd):

    pidConfigurationMessage = dron_app_pb2.PIDConfiguration()

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
        raspberryResponse = stub.SettingPID(pidConfiguration)
        if(raspberryResponse.successfullyCompleted == 1):
            print("set")
        else:
            print("error")


def testing():

    with grpc.insecure_channel(HOST_ADDRESS) as channel:
        stub = dron_app_pb2_grpc.DronStub(channel)
        request = dron_app_pb2.TestRequest()
        request.text = "Radek"
        print("Before send: ")
        print(request)
        response = stub.TestFunction(request)

def run():
    pass


#if __name__ == "__main__":
#    run()
testing()