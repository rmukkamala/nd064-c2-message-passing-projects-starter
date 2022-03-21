
"""
Generating gRPC files
pip install grpcio-tools

python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ order.proto
"""


"""
main.py
"""
import time
from concurrent import futures

import grpc
import order_pb2
import order_pb2_grpc


class OrderServicer(order_pb2_grpc.OrderServiceServicer):
    def Get(self, request, context):
        first_order = order_pb2.OrderMessage(
            id="2222",
            created_by="USER123",
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at='2020-03-12',
            equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
        )

        second_order = order_pb2.OrderMessage(
            id="3333",
            created_by="USER123",
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at='2020-03-11',
            equipment=[order_pb2.OrderMessage.Equipment.MOUSE]
        )

        result = order_pb2.OrderMessageList()
        result.orders.extend([first_order, second_order])
        return result

    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "created_by": request.created_by,
            "status": request.status,
            "created_at": request.created_at,
            "equipment": ["KEYBOARD"]
        }
        print(request_value)

        return order_pb2.OrderMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)


################################

"""
getter.py
"""
import grpc
import order_pb2
import order_pb2_grpc


print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

response = stub.Get(order_pb2.Empty())
print(response)

################################

"""
writer.py
"""

import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
order = order_pb2.OrderMessage(
    id="2222",
    created_by="USER123",
    status=order_pb2.OrderMessage.Status.QUEUED,
    created_at='2020-03-12',
    equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
)

response = stub.Create(order)

#######

"""
kafka demo

Usage
Installation
pip install kafka-python

Load Consumer
python consumer.py

Run Producer
python producer.py
"""
#producer.py
from kafka import KafkaProducer


TOPIC_NAME = 'items'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'Test Message!!!')
producer.flush()

####################################
#conusmer.py

from kafka import KafkaConsumer


TOPIC_NAME = 'items'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)


#######################################




syntax = "proto3";

message locationEventServiceMessage {
  int32 userId = 1;
  int32 latitude = 2;
  int32 longitude = 3;
}

service ItemService {
  rpc Create(locationEventServiceMessage) returns (locationEventServiceMessage);
}