#!/usr/bin/python3
import json
import os
import models
from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.place import Place
# from models.amenity import Amenity
# from models.review import Review
"""
    file_storage module contains the class
    for the serialization/deserialization of data
"""

class FileStorage():
    """
        class FileStorage serializes instances
        to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        file = FileStorage.__file_path
        object = FileStorage.__objects
        content = {}

        for key, value in object.items():
            content[key] = value.to_dict()

        with open(file, 'w', encoding='utf-8'):
            return f.write(json.dumps(content))

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        file = FileStorage.__file_path
        # classes = models.classes

        if os.path.isfile(file):
            with open(file, 'r', encoding="utf-8") as f:
                content = f.read()
                formattedContent = json.loads(content)

                for value in formattedContent.values():
                    class_name = value["__class__"]
                    # self.new(classes[class_name](**value))
                    self.new(eval(class_name)(**value))

    def update(self, key, attr, value):
        """updates an instance"""
        model = FileStorage.__objects[key]
        setattr(model, attr, value)

    def delete(self, key):
        """deletes an instance"""
        del FileStorage.__objects[key]
