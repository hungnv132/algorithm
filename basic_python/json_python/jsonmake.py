import json
from json import JSONDecoder, JSONEncoder


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    stu = Student('hungnv132', 24)

    print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))