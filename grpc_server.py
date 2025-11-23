import grpc
from concurrent import futures
import xml.etree.ElementTree as ET
from lxml import etree
import car_service_pb2
import car_service_pb2_grpc
import sys

class CarServiceServicer(car_service_pb2_grpc.CarServiceServicer):
    def __init__(self, xml_file):
        self.xml_file = xml_file
        # Usar lxml para XPath completo
        self.lxml_tree = etree.parse(xml_file)
        self.lxml_root = self.lxml_tree.getroot()
    
    def _car_to_proto(self, car_elem):
        """Converte elemento XML para protobuf Car"""
        car = car_service_pb2.Car()
        
        year_elem = car_elem.find('year')
        car.year = year_elem.text if year_elem is not None and year_elem.text else ""
        
        make_elem = car_elem.find('make')
        car.make = make_elem.text if make_elem is not None and make_elem.text else ""
        
        model_elem = car_elem.find('model')
        car.model = model_elem.text if model_elem is not None and model_elem.text else ""
        
        trim_elem = car_elem.find('trim')
        car.trim = trim_elem.text if trim_elem is not None and trim_elem.text else ""
        
        body_elem = car_elem.find('body')
        car.body = body_elem.text if body_elem is not None and body_elem.text else ""
        
        transmission_elem = car_elem.find('transmission')
        car.transmission = transmission_elem.text if transmission_elem is not None and transmission_elem.text else ""
        
        vin_elem = car_elem.find('vin')
        car.vin = vin_elem.text if vin_elem is not None and vin_elem.text else ""
        
        state_elem = car_elem.find('state')
        car.state = state_elem.text if state_elem is not None and state_elem.text else ""
        
        condition = car_elem.find('condition')
        if condition is not None and condition.text:
            car.condition = int(condition.text)
        
        odometer = car_elem.find('odometer')
        if odometer is not None and odometer.text:
            car.odometer = int(odometer.text)
        
        color_elem = car_elem.find('color')
        car.color = color_elem.text if color_elem is not None and color_elem.text else ""
        
        interior_elem = car_elem.find('interior')
        car.interior = interior_elem.text if interior_elem is not None and interior_elem.text else ""
        
        seller_elem = car_elem.find('seller')
        car.seller = seller_elem.text if seller_elem is not None and seller_elem.text else ""
        
        mmr = car_elem.find('mmr')
        if mmr is not None and mmr.text and mmr.text.strip():
            try:
                car.mmr = float(mmr.text)
            except (ValueError, TypeError):
                pass
        
        sellingprice = car_elem.find('sellingprice')
        if sellingprice is not None and sellingprice.text and sellingprice.text.strip():
            try:
                car.sellingprice = float(sellingprice.text)
            except (ValueError, TypeError):
                pass
        
        saledate_elem = car_elem.find('saledate')
        car.saledate = saledate_elem.text if saledate_elem is not None and saledate_elem.text else ""
        
        return car
    
    def GetCarsByMake(self, request, context):
        """Retorna carros por marca usando XPath"""
        car_list = car_service_pb2.CarList()
        try:
            if not request.make:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("Make parameter is required")
                return car_list
            
            # Usar mesma abordagem do XML-RPC: buscar todos e filtrar em Python
            elements = self.lxml_root.xpath("//car")
            make_lower = request.make.lower()
            
            for elem in elements:
                make_elem = elem.find('make')
                if make_elem is not None and make_elem.text and make_elem.text.lower() == make_lower:
                    try:
                        car_list.cars.append(self._car_to_proto(elem))
                    except Exception as conv_err:
                        # Continuar com próximo elemento se houver erro na conversão
                        continue
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error processing request: {str(e)}")
        return car_list
    
    def GetCarsByState(self, request, context):
        """Retorna carros por estado usando XPath"""
        car_list = car_service_pb2.CarList()
        try:
            if not request.state:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("State parameter is required")
                return car_list
            
            # Usar mesma abordagem do XML-RPC: buscar todos e filtrar em Python
            elements = self.lxml_root.xpath("//car")
            state_lower = request.state.lower()
            
            for elem in elements:
                state_elem = elem.find('state')
                if state_elem is not None and state_elem.text and state_elem.text.lower() == state_lower:
                    try:
                        car_list.cars.append(self._car_to_proto(elem))
                    except Exception as conv_err:
                        # Continuar com próximo elemento se houver erro na conversão
                        continue
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error processing request: {str(e)}")
        return car_list
    
    def GetAveragePriceByMake(self, request, context):
        """Retorna preço médio por marca usando XPath"""
        avg_price = car_service_pb2.AveragePrice()
        avg_price.make = request.make
        try:
            if not request.make:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("Make parameter is required")
                return avg_price
            
            # Usar mesma abordagem do XML-RPC: buscar todos e filtrar em Python
            elements = self.lxml_root.xpath("//car")
            make_lower = request.make.lower()
            prices = []
            
            for elem in elements:
                make_elem = elem.find('make')
                if make_elem is not None and make_elem.text and make_elem.text.lower() == make_lower:
                    price_elem = elem.find('sellingprice')
                    if price_elem is not None and price_elem.text and price_elem.text.strip():
                        try:
                            prices.append(float(price_elem.text))
                        except (ValueError, TypeError):
                            pass
            
            if prices:
                avg_price.average_price = sum(prices) / len(prices)
                avg_price.count = len(prices)
            else:
                avg_price.average_price = 0.0
                avg_price.count = 0
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error processing request: {str(e)}")
        return avg_price
    
    def XPathQuery(self, request, context):
        car_list = car_service_pb2.CarList()
        try:
            # Usar lxml que suporta XPath completo
            # Tentar executar o XPath
            try:
                elements = self.lxml_root.xpath(request.xpath)
            except Exception as xpath_error:
                # Se o XPath falhar, tentar uma sintaxe alternativa mais simples
                # ou retornar erro mais claro
                raise Exception(f"Invalid XPath syntax: {str(xpath_error)}")
            
            if not elements:
                # XPath não retornou resultados, mas não é um erro
                return car_list
            
            for elem in elements:
                # Verificar se é um elemento (não texto ou atributo)
                if not hasattr(elem, 'find'):
                    continue
                    
                # Elementos lxml têm interface compatível com ET
                try:
                    car_list.cars.append(self._car_to_proto(elem))
                except Exception as e:
                    # Se houver erro ao converter um elemento, continuar com os outros
                    continue
        except Exception as e:
            error_msg = str(e)
            if "Invalid XPath syntax" not in error_msg:
                error_msg = f"XPath error: {error_msg}"
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(error_msg)
        return car_list
    
    def GetAllMakes(self, request, context):
        """Retorna todas as marcas usando XPath"""
        make_list = car_service_pb2.MakeList()
        try:
            xpath = "//car/make[text()]"
            make_elements = self.lxml_root.xpath(xpath)
            makes = set()
            for make_elem in make_elements:
                if make_elem.text and make_elem.text.strip():
                    makes.add(make_elem.text)
            make_list.makes.extend(sorted([m for m in makes if m is not None]))
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
        return make_list
    
    def GetAllStates(self, request, context):
        """Retorna todos os estados usando XPath"""
        state_list = car_service_pb2.StateList()
        try:
            xpath = "//car/state[text()]"
            state_elements = self.lxml_root.xpath(xpath)
            states = set()
            for state_elem in state_elements:
                if state_elem.text and state_elem.text.strip():
                    states.add(state_elem.text)
            state_list.states.extend(sorted([s for s in states if s is not None]))
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
        return state_list
    
    def StreamCarsByMake(self, request, context):
        """Streaming: envia múltiplas respostas usando XPath"""
        try:
            if not request.make:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("Make parameter is required")
                return
            
            # Usar mesma abordagem do XML-RPC: buscar todos e filtrar em Python
            elements = self.lxml_root.xpath("//car")
            make_lower = request.make.lower()
            
            for elem in elements:
                make_elem = elem.find('make')
                if make_elem is not None and make_elem.text and make_elem.text.lower() == make_lower:
                    try:
                        yield self._car_to_proto(elem)
                    except Exception as conv_err:
                        # Continuar com próximo elemento se houver erro na conversão
                        continue
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error processing request: {str(e)}")
    
    def StreamCarsByState(self, request, context):
        """Streaming: envia múltiplas respostas usando XPath"""
        try:
            if not request.state:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("State parameter is required")
                return
            
            # Usar mesma abordagem do XML-RPC: buscar todos e filtrar em Python
            elements = self.lxml_root.xpath("//car")
            state_lower = request.state.lower()
            
            for elem in elements:
                state_elem = elem.find('state')
                if state_elem is not None and state_elem.text and state_elem.text.lower() == state_lower:
                    try:
                        yield self._car_to_proto(elem)
                    except Exception as conv_err:
                        # Continuar com próximo elemento se houver erro na conversão
                        continue
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error processing request: {str(e)}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    car_service_pb2_grpc.add_CarServiceServicer_to_server(
        CarServiceServicer("car_prices.xml"), server
    )
    server.add_insecure_port('[::]:9000')
    server.start()
    print("Servidor gRPC rodando na porta 9000...")
    print("Métodos disponíveis (todos usam XPath):")
    print("  - GetCarsByMake")
    print("  - GetCarsByState")
    print("  - GetAveragePriceByMake")
    print("  - XPathQuery")
    print("  - GetAllMakes")
    print("  - GetAllStates")
    print("  - StreamCarsByMake (streaming)")
    print("  - StreamCarsByState (streaming)")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

