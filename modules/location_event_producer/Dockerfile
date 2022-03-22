FROM python:3.7

WORKDIR .

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
ENTRYPOINT ["python", "grpc_server.py"]