FROM python:3.11-slim

WORKDIR /app

# Copiar requirements primeiro (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar arquivos necessários
COPY car_service.proto .
COPY converter.py .
COPY xmlrpc_server.py .
COPY grpc_server.py .
COPY schema.xsd .
COPY car_prices.csv .

# Gerar código gRPC
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. car_service.proto

# O CSV será montado via volume, então não precisa copiar
# Os servidores esperam que o XML seja gerado pelo converter

CMD ["python", "xmlrpc_server.py"]


