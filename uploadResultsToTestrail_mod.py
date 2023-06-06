import xml.etree.ElementTree as ET

def parse_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Access elements and perform further processing
        # Example: Print the tag and text of each element
        for element in root.iter():
            print("Tag:", element.tag)
            print("Text:", element.text)

    except ET.ParseError as e:
        print(f"Error parsing XML file: {str(e)}")

print("start v2")

# Provide the path to your XML file here
xml_file_path = "SxTestResult.trx"
parse_xml_file(xml_file_path)
