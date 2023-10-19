from lxml import etree
import json


class JSON_to_XML:
    def __init__(self, path) -> None:
        with open(path, 'r') as file:
            self.file = json.loads(file.read())
    
    def converter(self, path) -> None:
        root = etree.Element('root')
        for key_1 in self.file:
            element = etree.Element(key_1.replace(' ', '_'))
            for key_2 in self.file[key_1]:
                attr = etree.Element(key_2.replace(' ', '_'))
                attr.text = str(self.file[key_1][key_2])
                element.append(attr)
            root.append(element)
        tree = etree.ElementTree(root)
        tree.write(path, pretty_print=True, encoding = 'utf-8')



JSON_to_XML(path='test.json').converter(path='json.xml')
