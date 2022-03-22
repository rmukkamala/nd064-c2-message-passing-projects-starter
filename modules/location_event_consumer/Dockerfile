FROM python:3.7

WORKDIR .

COPY . .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["python", "location_consumer.py"]