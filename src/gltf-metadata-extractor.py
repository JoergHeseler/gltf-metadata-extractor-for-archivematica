# Title: gltf-metadata-extractor
# Version: 1.0.0
# Publisher: NFDI4Culture
# Publication date: 2024, October 25th
# License: CC BY 4.0

import json
import os
import hashlib
from datetime import datetime
import subprocess
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom

def calculate_checksum(file_path, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hash_func.update(chunk)
    return hash_func.hexdigest()

class GLTFValidatorException(Exception):
    pass

def parse_gltf_validator_data(target):
    # 'gltf_validator'
    args = ['gltf_validator', '-amo', target]

    try:
        output = subprocess.check_output(args).decode("utf8")
    except subprocess.CalledProcessError:
        raise GLTFValidatorException("gltf_validator failed when running: " + ' '.join(args))
    json_output = json.loads(output.encode("utf8"))
    return json_output

def extract_gltf_metadata(file_path):
    gltf_json_output = parse_gltf_validator_data(file_path)
    
    # Datei-Metadaten
    file_size = os.path.getsize(file_path)
    creation_date = datetime.utcfromtimestamp(os.path.getctime(file_path)).isoformat()
    modification_date = datetime.utcfromtimestamp(os.path.getmtime(file_path)).isoformat()
    checksum = calculate_checksum(file_path)
    
    # XML-Baum erstellen
    root = ET.Element('GLTFMetadataExtractor')
    ET.SubElement(root, 'formatName').text = 'GLTF'
    ET.SubElement(root, 'formatVersion').text = gltf_json_output['info']['version']
    ET.SubElement(root, 'size').text = str(file_size)
    ET.SubElement(root, 'SHA256Checksum').text = checksum
    ET.SubElement(root, 'creationDate').text = creation_date
    ET.SubElement(root, 'modificationDate').text = modification_date
    ET.SubElement(root, 'generator').text = gltf_json_output['info']['generator']
    ET.SubElement(root, 'hasDefaultScene').text = str(gltf_json_output['info']['hasDefaultScene'])
    ET.SubElement(root, 'totalVertexCount').text = str(gltf_json_output['info']['totalVertexCount'])
    ET.SubElement(root, 'totalTriangleCount').text = str(gltf_json_output['info']['totalTriangleCount'])
    ET.SubElement(root, 'materialCount').text = str(gltf_json_output['info']['materialCount'])
    ET.SubElement(root, 'hasTextures').text = str(gltf_json_output['info']['hasTextures'])
    ET.SubElement(root, 'animationCount').text = str(gltf_json_output['info']['animationCount'])
    ET.SubElement(root, 'hasSkins').text = str(gltf_json_output['info']['hasSkins'])
    ET.SubElement(root, 'rawGLTFValidatorOutput').text = json.dumps(gltf_json_output, indent=4)
    
    # XML-Ausgabe formatieren und in der Konsole ausgeben
    xml_output = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
    reparsed = minidom.parseString(xml_output)
    print(reparsed.toprettyxml(indent="    "))

def get_target_file_name_from_arguments():
    target = None
    for arg in sys.argv:
        if arg.startswith("--file-full-name="):
            # Extrahiere den Teil nach dem Gleichheitszeichen
            target = arg.split("=", 1)[1]
            break
    return target


# Beispielaufruf des Skripts
if __name__ == '__main__':
# Beispielaufruf der Funktion
    target = get_target_file_name_from_arguments()
    if not target:
        print("Kein Argument mit --file-full-name= gefunden.", file=sys.stderr)
    else:
        sys.exit(extract_gltf_metadata(target))
