import xmlrpc.client

def main():
    server = xmlrpc.client.ServerProxy("http://localhost:8000")
    
    print("=== Cliente XML-RPC ===\n")
    
    # Teste 1: Listar marcas
    print("1. Todas as marcas disponíveis:")
    makes = server.get_all_makes()
    if isinstance(makes, dict) and 'error' in makes:
        print(f"   Erro: {makes['error']}\n")
    else:
        print(f"   {len(makes)} marcas encontradas")
        print(f"   Primeiras 10: {makes[:10]}\n")
    
    # Teste 2: Carros por marca
    print("2. Carros da marca 'BMW':")
    bmw_cars = server.get_cars_by_make("BMW")
    if isinstance(bmw_cars, dict) and 'error' in bmw_cars:
        print(f"   Erro: {bmw_cars['error']}\n")
    else:
        print(f"   {len(bmw_cars)} carros encontrados")
        if bmw_cars:
            print(f"   Exemplo: {bmw_cars[0]}\n")
    
    # Teste 3: Preço médio
    print("3. Preço médio da marca 'Audi':")
    avg = server.get_average_price_by_make("Audi")
    if isinstance(avg, dict) and 'error' in avg:
        print(f"   Erro: {avg['error']}\n")
    else:
        print(f"   {avg}\n")
    
    # Teste 4: XPath
    print("4. Consulta XPath (carros BMW):")
    # XPath simples que funciona
    xpath_result = server.xpath_query("//car[make = 'BMW']")
    if isinstance(xpath_result, dict) and 'error' in xpath_result:
        print(f"   Erro na consulta XPath: {xpath_result['error']}\n")
    else:
        print(f"   {len(xpath_result)} carros encontrados")
        if xpath_result:
            print(f"   Exemplo: {xpath_result[0]}\n")
    
    # Teste 5: Carros por estado
    print("5. Carros no estado 'ca':")
    ca_cars = server.get_cars_by_state("ca")
    if isinstance(ca_cars, dict) and 'error' in ca_cars:
        print(f"   Erro: {ca_cars['error']}\n")
    else:
        print(f"   {len(ca_cars)} carros encontrados\n")
    
    # Teste 6: Novas funções XPath
    print("6. Carros entre 20000 e 50000:")
    price_range_cars = server.get_cars_by_price_range(20000, 50000)
    if isinstance(price_range_cars, dict) and 'error' in price_range_cars:
        print(f"   Erro: {price_range_cars['error']}\n")
    else:
        print(f"   {len(price_range_cars)} carros encontrados\n")
    
    print("7. Top 5 carros mais caros:")
    expensive = server.get_expensive_cars(5)
    if isinstance(expensive, dict) and 'error' in expensive:
        print(f"   Erro: {expensive['error']}\n")
    else:
        print(f"   {len(expensive)} carros encontrados")
        if expensive:
            print(f"   Exemplo: {expensive[0]}\n")

if __name__ == "__main__":
    main()

