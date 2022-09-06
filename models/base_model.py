#!/usr/bin/python3
import uuid
from datetime import datetime
from datetime import timedelta
import models

"""
    class BaseModel defines all common attributes/methods for other classes
"""


class BaseModel():
    """BaseModel is a parent class that will take care of initialization,
    serialization and deserialization of future instances
    """

    def __init__(self, *args, **kwargs):
        """
            Initializes each instance with a unique id,
            creation time and updation time
        """
        if kwargs:
            for attribute, value in kwargs.items():
                if attribute == 'created_at' or attribute == 'updated_at':
                    setattr(self, attribute, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                if attribute != '__class__':
                    setattr(self, attribute, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            prints the class name, instance id and dictionary representation
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute
            "updated_at" with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary
            containing all keys/values of "__dict__" of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        return dict_copy
