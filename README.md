# DronProject

- Generowanie plików do servera grpc :
python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos\dron_app.proto
