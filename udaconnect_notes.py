
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

## Docker Cmds

# location_event_consumer 


docker login
docker push rmukkamala/udaconnect_location_event_consumer:v1.0.0

# location_event_producer
docker build -t rmukkamala/udaconnect_location_event_producer:v1.0.0 .

docker push rmukkamala/udaconnect_location_event_producer:v1.0.0

# location_microservice
docker build -t rmukkamala/udaconnect_location_microservice:v1.0.0 .

docker push rmukkamala/udaconnect_location_microservice:v1.0.0

# connection_microservice



docker push rmukkamala/udaconnect_connection_microservice:v1.0.0

# person_microservice
docker build -t rmukkamala/udaconnect_person_microservice:v1.0.0 .

docker push rmukkamala/udaconnect_person_microservice:v1.0.0


Example:
# build the image
docker build -t go-helloworld .

# run the image
docker run -d -p 6111:6111 go-helloworld
# Access the application on: http://127.0.0.1:6111/ or http://localhost:6111/ or http://0.0.0.0:6111/

# tag the image
docker tag go-helloworld pixelpotato/go-helloworld:v1.0.0

# login into DockerHub
docker login

# push the image
docker push pixelpotato/go-helloworld:v1.0.0


## Docker commands used to build the application 
# TODO: insert the docker build command

docker build -t rmukkamala/udaconnect_location_event_consumer:v1.0.0 .


## Docker commands used to run the application
# TODO: insert the docker run command
docker run -d --name techtrendsv1.1.0 -p 7111:3111 rmukkamala/techtrends:v1.1.0

## Docker commands used to get the application logs
# TODO: insert the docker logs command
docker logs edf03f248665


############
#location_event_producer and location_event_consumer microservices
- The user locations are tracked from client mobiles and sent asynchronously to the Grpc server which also has the logic to act as a kafka producer.
- The Grpc message passing technique is used here since a lot of location data may be sent and Grpc will reduce the latency and be faster.

- The kafka is used to handle this traffic for pushing location data.  
- location_event_consumer microservice acts as the producer and location_event_consumer microservice acts as the consumer which then saves the data inot the DB.DeprecationWarning

- person microservice , connection microservice and location microservice are separated into independent microservices and use REST API to interact with the React Frontend Service.
- These microservices can improve their efficiency by using caches as way of lookup service for faster responses.  

############


## kubectl cmds for deployment of yaml files


