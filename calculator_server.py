

from concurrent import futures
import time

import grpc

import calculator_pb2
import calculator_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Addition(calculator_pb2_grpc.AdditionServicer):

    def AddNumbers(self, request, context):
        return calculator_pb2.AddReply(result=request.num1 + request.num2)
        
    
   
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_AdditionServicer_to_server(Addition(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("\nServer initiated.. ready to serve client requests..")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
