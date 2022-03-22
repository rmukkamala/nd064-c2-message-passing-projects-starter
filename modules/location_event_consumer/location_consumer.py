import json
import requests

from kafka import KafkaConsumer


TOPIC_NAME = 'event'
KAFKA_SERVER = 'kafka-service.default.svc.cluster.local:9092'
LOCATION_ENDPOINT= ''

print('Listening ' + TOPIC_NAME)

consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=[KAFKA_SERVER])

for message in consumer:
    message = message.value.decode('utf-8')
    print (message)
    location_event_msg = json.loads(message)
    #new_location = requests.post(LOCATION_ENDPOINT + "api/locations", json=location_event_msg)
    print("Location msg saved !")