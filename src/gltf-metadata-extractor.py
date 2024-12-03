# Title: gltf-metadata-extractor
# Version: 1.0.0
# Publisher: NFDI4Culture
# Publication date: November 22, 2024
# License: CC BY 4.0

import json
import os
import hashlib
from datetime import datetime
import subprocess
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom

def get_target_file_name_from_arguments():
    target = None
    for arg in sys.argv:
        if arg.startswith("--file-full-name="):
            # Extract the part after the equals sign
            target = arg.split("=", 1)[1]
            break
    return target

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
    # Run the official gltf_validator
    validator_path = '/usr/share/gltf_validator'
    args = [validator_path, '-amo', target]

    try:
        output = subprocess.check_output(args).decode("utf8")
    except subprocess.CalledProcessError:
        raise GLTFValidatorException("gltf_validator failed when running: " + ' '.join(args))
    json_output = json.loads(output.encode("utf8"))
    return json_output

def extract_gltf_metadata(file_path):
    gltf_json_output = parse_gltf_validator_data(file_path)
    
    # File metadata
    file_size = os.path.getsize(file_path)
    creation_date = datetime.utcfromtimestamp(os.path.getctime(file_path)).isoformat()
    modification_date = datetime.utcfromtimestamp(os.path.getmtime(file_path)).isoformat()
    checksum = calculate_checksum(file_path)
    
    # Create XML tree with namespace and schema location
    ET.register_namespace('', "http://nfdi4culture.de/gltf-metadata-extractor1") # Register default namespace
    root = ET.Element('GLTFMetadataExtractor', {
        'xmlns': "http://nfdi4culture.de/gltf-metadata-extractor1",
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'xsi:schemaLocation': "http://nfdi4culture.de/gltf-metadata-extractor1 https://raw.githubusercontent.com/JoergHeseler/gltf-metadata-extractor-for-archivematica/refs/heads/main/src/gltf-metadata-extractor.xsd"
    })

    # Create XML tree
    #root = ET.Element('GLTFMetadataExtractor')
    ET.SubElement(root, 'formatName').text = 'glTF (Graphics Library Transmission Format)'
    ET.SubElement(root, 'formatVersion').text = gltf_json_output['info']['version']
    ET.SubElement(root, 'size').text = str(file_size)
    ET.SubElement(root, 'SHA256Checksum').text = checksum
    ET.SubElement(root, 'creationDate').text = creation_date
    ET.SubElement(root, 'modificationDate').text = modification_date
    ET.SubElement(root, 'generator').text = gltf_json_output['info']['generator']
    ET.SubElement(root, 'hasDefaultScene').text = str(gltf_json_output['info']['hasDefaultScene']).lower()
    ET.SubElement(root, 'totalVertexCount').text = str(gltf_json_output['info']['totalVertexCount'])
    ET.SubElement(root, 'totalTriangleCount').text = str(gltf_json_output['info']['totalTriangleCount'])
    ET.SubElement(root, 'materialCount').text = str(gltf_json_output['info']['materialCount'])
    ET.SubElement(root, 'hasTextures').text = str(gltf_json_output['info']['hasTextures']).lower()
    ET.SubElement(root, 'animationCount').text = str(gltf_json_output['info']['animationCount'])
    ET.SubElement(root, 'hasSkins').text = str(gltf_json_output['info']['hasSkins']).lower()
    
    # Convert ElementTree to minidom document for CDATA support
    xml_str = ET.tostring(root, encoding='utf-8')
    dom = minidom.parseString(xml_str)
    
    # Add CDATA section for rawGLTFValidatorOutput
    raw_output = dom.createElement('rawGLTFValidatorOutput')
    cdata_section = dom.createCDATASection(json.dumps(gltf_json_output, indent=4))
    raw_output.appendChild(cdata_section)
    dom.documentElement.appendChild(raw_output)

    # Print formatted XML with CDATA
    print(dom.toprettyxml(indent="    "))


if __name__ == '__main__':
# Main
    target = get_target_file_name_from_arguments()
    if not target:
        print("No argument with --file-full-name= found.", file=sys.stderr)
    else:
        sys.exit(extract_gltf_metadata(target))
