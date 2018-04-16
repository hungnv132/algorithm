from abc import ABCMeta

import xml.etree.ElementTree as ET
import json


class Reader(metaclass=ABCMeta):

    @property
    def parsed_data(self):
        raise NotImplementedError("You must implement method 'parsed_data()'")


class JSONReader(Reader):

    def __init__(self, filepath):
        self.data = {}
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLReader(Reader):

    def __init__(self, filepath):
        self.tree = ET.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def reader_factory(filepath):
    if filepath.endswith('json'):
        reader = JSONReader
    elif filepath.endswith('xml'):
        reader = XMLReader
    else:
        raise ValueError("Cannot read file '{}'".format(filepath))
    return reader(filepath)


def reader_file(filepath):
    factory = None
    try:
        factory = reader_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


if __name__ == '__main__':
    json_factory = reader_file('data.json')
    json_data = json_factory.parsed_data
    print(json_data)

    xml_factory = reader_file('data.xml')
    xml_data = xml_factory.parsed_data
    print(xml_data)