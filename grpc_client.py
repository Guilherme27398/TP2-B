import grpc
import car_service_pb2
import car_service_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:9000')
    stub = car_service_pb2_grpc.CarServiceStub(channel)
    
    print("=== Cliente gRPC ===\n")
    
    # Teste 1: Listar marcas
    print("1. Todas as marcas disponíveis:")
    makes_response = stub.GetAllMakes(car_service_pb2.Empty())
    makes = list(makes_response.makes)
    print(f"   {len(makes)} marcas encontradas")
    print(f"   Primeiras 10: {makes[:10]}\n")
    
    # Teste 2: Carros por marca
    print("2. Carros da marca 'BMW':")
    bmw_request = car_service_pb2.MakeRequest(make="BMW")
    bmw_cars = stub.GetCarsByMake(bmw_request)
    print(f"   {len(bmw_cars.cars)} carros encontrados")
    if bmw_cars.cars:
        car = bmw_cars.cars[0]
        print(f"   Exemplo: {car.year} {car.make} {car.model} - ${car.sellingprice}\n")
    
    # Teste 3: Preço médio
    print("3. Preço médio da marca 'Audi':")
    audi_request = car_service_pb2.MakeRequest(make="Audi")
    avg = stub.GetAveragePriceByMake(audi_request)
    print(f"   Marca: {avg.make}")
    print(f"   Preço médio: ${avg.average_price:.2f}")
    print(f"   Quantidade: {avg.count}\n")
    
    # Teste 4: XPath
    print("4. Consulta XPath (carros BMW):")
    try:
        # Usar sintaxe XPath com aspas duplas (mais compatível)
        xpath_request = car_service_pb2.XPathRequest(xpath='//car[make = "BMW"]')
        xpath_result = stub.XPathQuery(xpath_request)
        print(f"   {len(xpath_result.cars)} carros encontrados")
        if xpath_result.cars:
            car = xpath_result.cars[0]
            print(f"   Exemplo: {car.year} {car.make} {car.model} - ${car.sellingprice}\n")
        else:
            print("   Nenhum carro encontrado\n")
    except grpc.RpcError as e:
        print(f"   Erro na consulta XPath: {e.details()}\n")
    
    # Teste 5: Streaming
    print("5. Streaming - Carros da marca 'Kia' (primeiros 5):")
    kia_request = car_service_pb2.MakeRequest(make="Kia")
    count = 0
    for car in stub.StreamCarsByMake(kia_request):
        if count < 5:
            print(f"   {car.year} {car.make} {car.model} - ${car.sellingprice}")
            count += 1
        else:
            break
    print("   ... (streaming continua)\n")
    
    channel.close()

if __name__ == "__main__":
    main()

