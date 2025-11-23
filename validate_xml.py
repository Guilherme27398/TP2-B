from lxml import etree
import sys

def validate_xml(xml_file, xsd_file):
    """Valida XML com schema XSD"""
    try:
        xml_doc = etree.parse(xml_file)
        xsd_doc = etree.parse(xsd_file)
        schema = etree.XMLSchema(xsd_doc)
        
        if schema.validate(xml_doc):
            print(f"[OK] XML válido conforme schema XSD")
            return True
        else:
            print("[ERRO] XML inválido:")
            for error in schema.error_log:
                print(f"  Linha {error.line}: {error.message}")
            return False
    except etree.XMLSyntaxError as e:
        print(f"[ERRO] Erro de sintaxe XML: {e}")
        return False
    except Exception as e:
        print(f"[ERRO] Erro na validação: {e}")
        return False

if __name__ == "__main__":
    xml_file = "car_prices.xml"
    xsd_file = "schema.xsd"
    
    print("Validando XML com schema XSD...")
    if validate_xml(xml_file, xsd_file):
        sys.exit(0)
    else:
        sys.exit(1)

