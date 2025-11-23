import xmlrpc.server
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from lxml import etree
import sys

class CarService:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.tree = etree.parse(xml_file)
        self.root = self.tree.getroot()
    
    def _element_to_dict(self, elem):
        """Converte elemento XML para dicionário"""
        car_data = {}
        for child in elem:
            car_data[child.tag] = child.text if child.text is not None else ''
        return car_data
    
    def get_cars_by_make(self, make):
        """Retorna carros por marca usando XPath"""
        try:
            # XPath - buscar todos os carros
            elements = self.root.xpath("//car")
            result = []
            make_lower = make.lower()
            for elem in elements:
                make_elem = elem.find('make')
                if make_elem is not None and make_elem.text and make_elem.text.lower() == make_lower:
                    result.append(self._element_to_dict(elem))
            return result
        except Exception as e:
            return {'error': str(e)}
    
    def get_cars_by_state(self, state):
        """Retorna carros por estado usando XPath"""
        try:
            elements = self.root.xpath("//car")
            result = []
            state_lower = state.lower()
            for elem in elements:
                state_elem = elem.find('state')
                if state_elem is not None and state_elem.text and state_elem.text.lower() == state_lower:
                    result.append(self._element_to_dict(elem))
            return result
        except Exception as e:
            return {'error': str(e)}
    
    def get_average_price_by_make(self, make):
        """Retorna preço médio por marca usando XPath"""
        try:
            elements = self.root.xpath("//car")
            prices = []
            make_lower = make.lower()
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
                avg = sum(prices) / len(prices)
                return {'make': make, 'average_price': avg, 'count': len(prices)}
            return {'make': make, 'average_price': 0, 'count': 0}
        except Exception as e:
            return {'error': str(e)}
    
    def xpath_query(self, xpath_expr):
        """Executa consulta XPath no XML usando lxml"""
        try:
            elements = self.root.xpath(xpath_expr)
            results = []
            for elem in elements:
                if hasattr(elem, 'tag'):  # É um elemento
                    results.append(self._element_to_dict(elem))
                else:  # É texto ou outro tipo
                    results.append(str(elem))
            return results
        except Exception as e:
            return {'error': str(e)}
    
    def get_all_makes(self):
        """Retorna todas as marcas disponíveis usando XPath"""
        try:
            make_elements = self.root.xpath("//car/make")
            makes = set()
            for make_elem in make_elements:
                if make_elem.text and make_elem.text.strip():
                    makes.add(make_elem.text)
            return sorted([m for m in makes if m is not None])
        except Exception as e:
            return {'error': str(e)}
    
    def get_all_states(self):
        """Retorna todos os estados disponíveis usando XPath"""
        try:
            state_elements = self.root.xpath("//car/state")
            states = set()
            for state_elem in state_elements:
                if state_elem.text and state_elem.text.strip():
                    states.add(state_elem.text)
            return sorted([s for s in states if s is not None])
        except Exception as e:
            return {'error': str(e)}
    
    def get_cars_by_price_range(self, min_price, max_price):
        """Retorna carros por intervalo de preço usando XPath"""
        try:
            elements = self.root.xpath("//car")
            result = []
            for elem in elements:
                price_elem = elem.find('sellingprice')
                if price_elem is not None and price_elem.text and price_elem.text.strip():
                    try:
                        price = float(price_elem.text)
                        if min_price <= price <= max_price:
                            result.append(self._element_to_dict(elem))
                    except (ValueError, TypeError):
                        pass
            return result
        except Exception as e:
            return {'error': str(e)}
    
    def get_cars_by_year(self, year):
        """Retorna carros por ano usando XPath"""
        try:
            elements = self.root.xpath("//car")
            result = []
            year_str = str(year)
            for elem in elements:
                year_elem = elem.find('year')
                if year_elem is not None and year_elem.text and year_elem.text == year_str:
                    result.append(self._element_to_dict(elem))
            return result
        except Exception as e:
            return {'error': str(e)}
    
    def get_cars_by_year_range(self, min_year, max_year):
        """Retorna carros por intervalo de anos usando XPath"""
        try:
            elements = self.root.xpath("//car")
            result = []
            for elem in elements:
                year_elem = elem.find('year')
                if year_elem is not None and year_elem.text:
                    try:
                        year = int(year_elem.text)
                        if min_year <= year <= max_year:
                            result.append(self._element_to_dict(elem))
                    except (ValueError, TypeError):
                        pass
            return result
        except Exception as e:
            return {'error': str(e)}
    
    def get_cars_by_body_type(self, body_type):
        """Retorna carros por tipo de carroceria usando XPath"""
        try:
            elements = self.root.xpath("//car")
            result = []
            body_lower = body_type.lower()
            for elem in elements:
                body_elem = elem.find('body')
                if body_elem is not None and body_elem.text and body_elem.text.lower() == body_lower:
                    result.append(self._element_to_dict(elem))
            return result
        except Exception as e:
            return {'error': str(e)}
    
    def get_expensive_cars(self, limit=10):
        """Retorna os carros mais caros usando XPath"""
        try:
            elements = self.root.xpath("//car")
            cars_with_price = []
            for elem in elements:
                price_elem = elem.find('sellingprice')
                if price_elem is not None and price_elem.text and price_elem.text.strip():
                    try:
                        price = float(price_elem.text)
                        car_data = self._element_to_dict(elem)
                        car_data['_price_value'] = price
                        cars_with_price.append(car_data)
                    except (ValueError, TypeError):
                        pass
            
            # Ordenar por preço e retornar top N
            cars_with_price.sort(key=lambda x: x.get('_price_value', 0), reverse=True)
            result = cars_with_price[:limit]
            # Remover campo auxiliar
            for car in result:
                car.pop('_price_value', None)
            return result
        except Exception as e:
            return {'error': str(e)}
    
    def get_cars_by_make_and_state(self, make, state):
        """Retorna carros por marca e estado usando XPath"""
        try:
            elements = self.root.xpath("//car")
            result = []
            make_lower = make.lower()
            state_lower = state.lower()
            for elem in elements:
                make_elem = elem.find('make')
                state_elem = elem.find('state')
                if (make_elem is not None and make_elem.text and make_elem.text.lower() == make_lower and
                    state_elem is not None and state_elem.text and state_elem.text.lower() == state_lower):
                    result.append(self._element_to_dict(elem))
            return result
        except Exception as e:
            return {'error': str(e)}
    
    def get_statistics_by_make(self, make):
        """Retorna estatísticas de uma marca usando XPath"""
        try:
            elements = self.root.xpath("//car")
            make_lower = make.lower()
            filtered_elements = []
            for elem in elements:
                make_elem = elem.find('make')
                if make_elem is not None and make_elem.text and make_elem.text.lower() == make_lower:
                    filtered_elements.append(elem)
            
            total = len(filtered_elements)
            prices = []
            years = []
            
            for elem in filtered_elements:
                price_elem = elem.find('sellingprice')
                if price_elem is not None and price_elem.text and price_elem.text.strip():
                    try:
                        prices.append(float(price_elem.text))
                    except (ValueError, TypeError):
                        pass
                
                year_elem = elem.find('year')
                if year_elem is not None and year_elem.text:
                    try:
                        years.append(int(year_elem.text))
                    except (ValueError, TypeError):
                        pass
            
            stats = {
                'make': make,
                'total_cars': total,
                'average_price': sum(prices) / len(prices) if prices else 0,
                'min_price': min(prices) if prices else 0,
                'max_price': max(prices) if prices else 0,
                'min_year': min(years) if years else 0,
                'max_year': max(years) if years else 0
            }
            return stats
        except Exception as e:
            return {'error': str(e)}
            
            total = len(elements)
            prices = []
            years = []
            
            for elem in elements:
                price_elem = elem.find('sellingprice')
                if price_elem is not None and price_elem.text and price_elem.text.strip():
                    try:
                        prices.append(float(price_elem.text))
                    except (ValueError, TypeError):
                        pass
                
                year_elem = elem.find('year')
                if year_elem is not None and year_elem.text:
                    try:
                        years.append(int(year_elem.text))
                    except (ValueError, TypeError):
                        pass
            
            stats = {
                'make': make,
                'total_cars': total,
                'average_price': sum(prices) / len(prices) if prices else 0,
                'min_price': min(prices) if prices else 0,
                'max_price': max(prices) if prices else 0,
                'min_year': min(years) if years else 0,
                'max_year': max(years) if years else 0
            }
            return stats
        except Exception as e:
            return {'error': str(e)}

def main():
    server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0", 8000))
    server.register_introspection_functions()
    
    service = CarService("car_prices.xml")
    server.register_instance(service)
    
    print("Servidor XML-RPC rodando na porta 8000...")
    print("Métodos disponíveis (todos usam XPath):")
    print("  - get_cars_by_make(make)")
    print("  - get_cars_by_state(state)")
    print("  - get_average_price_by_make(make)")
    print("  - xpath_query(xpath_expr)")
    print("  - get_all_makes()")
    print("  - get_all_states()")
    print("  - get_cars_by_price_range(min_price, max_price)")
    print("  - get_cars_by_year(year)")
    print("  - get_cars_by_year_range(min_year, max_year)")
    print("  - get_cars_by_body_type(body_type)")
    print("  - get_expensive_cars(limit=10)")
    print("  - get_cars_by_make_and_state(make, state)")
    print("  - get_statistics_by_make(make)")
    
    server.serve_forever()

if __name__ == "__main__":
    main()

