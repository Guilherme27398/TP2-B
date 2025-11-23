import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
from lxml import etree
import sys

def csv_to_xml(csv_file, xml_file):
    """Converte CSV para XML"""
    root = ET.Element('cars')
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            car = ET.SubElement(root, 'car')
            
            # Campos obrigatórios
            ET.SubElement(car, 'year').text = row.get('year', '')
            ET.SubElement(car, 'make').text = row.get('make', '')
            ET.SubElement(car, 'model').text = row.get('model', '')
            ET.SubElement(car, 'trim').text = row.get('trim', '')
            ET.SubElement(car, 'body').text = row.get('body', '')
            
            # Campos opcionais
            if row.get('transmission'):
                ET.SubElement(car, 'transmission').text = row.get('transmission', '')
            
            ET.SubElement(car, 'vin').text = row.get('vin', '')
            ET.SubElement(car, 'state').text = row.get('state', '')
            
            if row.get('condition') and row.get('condition').strip():
                ET.SubElement(car, 'condition').text = row.get('condition', '')
            
            if row.get('odometer') and row.get('odometer').strip():
                ET.SubElement(car, 'odometer').text = row.get('odometer', '')
            
            ET.SubElement(car, 'color').text = row.get('color', '')
            ET.SubElement(car, 'interior').text = row.get('interior', '')
            ET.SubElement(car, 'seller').text = row.get('seller', '')
            
            if row.get('mmr') and row.get('mmr').strip():
                ET.SubElement(car, 'mmr').text = row.get('mmr', '')
            
            if row.get('sellingprice') and row.get('sellingprice').strip():
                ET.SubElement(car, 'sellingprice').text = row.get('sellingprice', '')
            ET.SubElement(car, 'saledate').text = row.get('saledate', '')
    
    # Formatar XML
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
    
    with open(xml_file, 'w', encoding='utf-8') as f:
        f.write(xml_str)
    
    print(f"CSV convertido para XML: {xml_file}")


if __name__ == "__main__":
    csv_file = "car_prices.csv"
    xml_file = "car_prices.xml"
    xsd_file = "schema.xsd"
    
    print("Convertendo CSV para XML...")
    csv_to_xml(csv_file, xml_file)
    

