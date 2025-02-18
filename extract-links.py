import sys
import xml.etree.ElementTree as ET

URL_PREFIX = "https://opendap.cr.usgs.gov"


def extract_links(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    for child in root:
        if child.tag.endswith('dataset'):
            datasets_root = child
            break

    for dataset in datasets_root:
        for suffix in ('dap', 'info', 'rdf', 'html'):
            print(f"{URL_PREFIX}{dataset.attrib['ID']}.{suffix}")






if __name__ == '__main__':
    extract_links(sys.argv[1])
