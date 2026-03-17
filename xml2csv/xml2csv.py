import xml.etree.ElementTree as ET
import csv
import re

def parse_xml_to_csv(xml_file, csv_file):
    # Parser le fichier XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialiser une liste pour stocker les données CSV
    csv_data = []

    # Parcourir tous les éléments <property>
    for property_elem in root.findall('.//property'):
        key = property_elem.find('key').text if property_elem.find('key') is not None else ''
        value = property_elem.find('value').text if property_elem.find('value') is not None else ''
        description = property_elem.find('description').text if property_elem.find('description') is not None else ''

        # Remplacer les espaces multiples et les sauts de ligne par un espace unique
        if description:
            description = re.sub(r'\s+', ' ', description.replace('\n', ' ')).strip()

        # Ajouter les données à la liste
        csv_data.append([key, value, description])

    # Écrire les données dans un fichier CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Écrire l'en-tête
        writer.writerow(['Key', 'Value', 'Description'])
        # Écrire les données
        writer.writerows(csv_data)

# Exemple d'utilisation
filename = 'example.appProperties'


xml_file = 'xml/' + filename + '.xml'
csv_file = 'xml/' + filename + '.csv'
parse_xml_to_csv(xml_file, csv_file)
