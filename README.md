# Sistema Distribuído RPC - TP2-B

Sistema distribuído para consultar dados de carros usando dois protocolos RPC: XML-RPC e gRPC.

## Estrutura do Projeto

- `car_prices.csv` - Dados originais em CSV
- `converter.py` - Converte CSV para XML e valida com XSD
- `schema.xsd` - Schema XSD para validação
- `xmlrpc_server.py` - Servidor XML-RPC (porta 8000)
- `grpc_server.py` - Servidor gRPC (porta 9000)
- `xmlrpc_client.py` - Cliente XML-RPC de teste
- `grpc_client.py` - Cliente gRPC de teste
- `car_service.proto` - Definição Protocol Buffer para gRPC
- `docker-compose.yml` - Orquestração dos serviços

## Instalação

1. Instalar dependências:
```bash
pip install -r requirements.txt
```

2. Gerar código gRPC a partir do arquivo .proto:
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. car_service.proto
```

3. Converter CSV para XML:
```bash
python converter.py
```

## Uso

### Opção 1: Executar manualmente

1. Iniciar servidor XML-RPC (Terminal 1):
```bash
python xmlrpc_server.py
```

2. Iniciar servidor gRPC (Terminal 2):
```bash
python grpc_server.py
```

3. Testar clientes (Terminal 3):
```bash
python xmlrpc_client.py
python grpc_client.py
```

### Opção 2: Usar Docker Compose

```bash
docker-compose up
```

## Funcionalidades

### XML-RPC (porta 8000)
- `get_cars_by_make(make)` - Retorna carros por marca
- `get_cars_by_state(state)` - Retorna carros por estado
- `get_average_price_by_make(make)` - Retorna preço médio por marca
- `xpath_query(xpath_expr)` - Executa consulta XPath
- `get_all_makes()` - Lista todas as marcas
- `get_all_states()` - Lista todos os estados

### gRPC (porta 9000)
- `GetCarsByMake` - Retorna carros por marca
- `GetCarsByState` - Retorna carros por estado
- `GetAveragePriceByMake` - Retorna preço médio por marca
- `XPathQuery` - Executa consulta XPath
- `GetAllMakes` - Lista todas as marcas
- `GetAllStates` - Lista todos os estados
- `StreamCarsByMake` - Streaming de carros por marca
- `StreamCarsByState` - Streaming de carros por estado

## Exemplos de Consultas XPath

- Todos os carros BMW: `.//car[make='BMW']`
- Carros com preço > 50000: `.//car[sellingprice > '50000']`
- Carros do estado CA: `.//car[state='ca']`
- Carros de 2015: `.//car[year='2015']`



