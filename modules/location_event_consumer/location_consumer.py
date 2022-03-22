import json
from sqlalchemy import create_engine
from geoalchemy2.functions import ST_AsText, ST_Point
import requests
import os

from kafka import KafkaConsumer

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

TOPIC_NAME = 'event'
#KAFKA_SERVER = 'kafka-service.default.svc.cluster.local:9092'
KAFKA_SERVER= "kafka-service:9092"
LOCATION_ENDPOINT= ''

print('Listening ' + TOPIC_NAME)

consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=[KAFKA_SERVER])

"""
SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print(f"SQLALCHEMY_DATABASE_URI - {SQLALCHEMY_DATABASE_URI}")

def kafka_to_db(location):
    db = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = db.connect()

    insert = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" \
        .format(location["person_id"], int(location["latitude"]), int(location["longitude"]))

    print(insert)
    connection.execute(insert)

"""


for message in consumer:
    message = message.value.decode('utf-8')
    print (message)
    location_event_msg = json.loads(message)
    #new_location = requests.post(LOCATION_ENDPOINT + "api/locations", json=location_event_msg)
    #kafka_to_db(location_event_msg)
    print("Location msg saved !")