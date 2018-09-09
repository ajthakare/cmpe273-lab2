

from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc

print("\nClient initiated..\n")

n1 = input("Enter first number: ")
n2 = input("Enter second number: ")


def run():
    channel=grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.AdditionStub(channel)
    print('Add request sent to server..')
    response = stub.AddNumbers(calculator_pb2.AddRequest(num1=int(n1),num2=int(n2)))
    print("Addition client received sum: " + response.result)


if __name__ == '__main__':
    run()
