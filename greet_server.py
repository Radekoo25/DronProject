import sys
from concurrent import futures
import grpc
import dron_app_pb2
import dron_app_pb2_grpc

HOST_ADDRESS = 'localhost:10001'


class DronServicer(dron_app_pb2_grpc.DronServicer):
    def SettingPID(self, request):
        #pidConfigurationMessage = dron_app_pb2.PIDConfiguration()

        #pidConfigurationMessage.yaw_kp = request.yaw_kp
        #pidConfigurationMessage.yaw_ki = request.yaw_ki
        #pidConfigurationMessage.yaw_kd = request.yaw_kd
        #pidConfigurationMessage.pitch_kp = request.pitch_kp
        #pidConfigurationMessage.pitch_ki = request.pitch_ki
        #pidConfigurationMessage.pitch_kd = request.pitch_kd
        #pidConfigurationMessage.roll_kp = request.roll_kp
        #pidConfigurationMessage.roll_ki = request.roll_ki
        #pidConfigurationMessage.roll_kd = request.roll_kd

        #print(pidConfigurationMessage)

        print(request)

        test = 1
        if test == 0:
            raspberry_response = dron_app_pb2.RaspberryResponse()
            raspberry_response.successfullyCompleted = 0
        else:
            raspberry_response = dron_app_pb2.RaspberryResponse()
            raspberry_response.successfullyCompleted = 1

        return raspberry_response

    def TestFunction(self, request):
        response = dron_app_pb2.TestResponse()
        print(request)
        print(sys.getsizeof(request))
        response.text2 = "Wysłano!"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dron_app_pb2_grpc.add_DronServicer_to_server(DronServicer, server)
    server.add_insecure_port(HOST_ADDRESS)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
