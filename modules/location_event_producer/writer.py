import grpc
import events_pb2
import events_pb2_grpc

"""
implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending location event payload...")

channel = grpc.insecure_channel("localhost:5005", options=(('grpc.enable_http_proxy', 0),))
stub = events_pb2_grpc.eventServiceStub(channel)

# Update this with desired payload
sample_event_data= events_pb2.locationEventServiceMessage(
    userid=2,
    latitude=2000,
    longitude=7000
)

response = stub.Create(sample_event_data)
