import time
from concurrent import futures
import grpc
import dron_app_pb2
import dron_app_pb2_grpc
import arduino

HOST_ADDRESS = 'localhost:10001'
#HOST_ADDRESS = '192.168.1.68:10001'
ard = arduino.SerialConnection()


class DronServicer(dron_app_pb2_grpc.DronServicer):

    def SettingPID(self, request, context):

        # Receiving message from DesktopApp
        # pidConfigurationMessage = dron_app_pb2.PIDConfigurationMessage()
        # pidConfigurationMessage = request
        print(request)

        # Sending message to Arduino
        arduino_response = ard.sendPID(request)
        # arduino_response = ard.sendPID("pidConfigurationMessage\n")

        # Sending Arduino response back to desktop client
        raspberry_response = dron_app_pb2.RaspberryResponse()
        raspberry_response.successfullyCompleted = arduino_response
        return raspberry_response


def serve():
    # Starting gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dron_app_pb2_grpc.add_DronServicer_to_server(DronServicer(), server)
    server.add_insecure_port(HOST_ADDRESS)
    server.start()

    # Waiting for shutdown the server
    try:
        while True:
            print("No problems detected!")
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)
        ard.close_connection()


if __name__ == "__main__":
    serve()