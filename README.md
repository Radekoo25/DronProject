# DronProject

- Generowanie plików do servera grpc :
python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos\dron_app.proto


Pamiętać o instalowaniu modułu "grpcio"!


Uwaga na bibliotekę Nanopb-0.4.6.4 !!!! W Programio mogą być maksymalnie 2 kropki w wersji, trzeba na twardo wpisać 0.4.6

