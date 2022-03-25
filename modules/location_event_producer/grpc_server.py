import time
import json
import os
from concurrent import futures
from kafka import KafkaProducer


import grpc
import events_pb2
import events_pb2_grpc


KAFKA_TOPIC_NAME = 'event'
#KAFKA_SERVER = '127.0.0.1:9092'
#KAFKA_SERVER = 'kafka-service.default.svc.cluster.local:9092'
KAFKA_SERVER = 'kafka.default.svc.cluster.local:9092'
#KAFKA_SERVER = 'kafka-service:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)



class eventServicer(events_pb2_grpc.eventServiceServicer):

    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "userid": int(request.userid),
            "latitude": int(request.latitude),
            "longitude": int(request.longitude)
        }
        print(request_value)
        event_encode_data = json.dumps(request_value, indent=2).encode('utf-8')
        producer.send(KAFKA_TOPIC_NAME, event_encode_data)

        return events_pb2.locationEventServiceMessage(**request_value)


##sleep/wait
time.sleep(25)
# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
events_pb2_grpc.add_eventServiceServicer_to_server(eventServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

