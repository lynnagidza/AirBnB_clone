#!/usr/bin/python3
"""Module that holds class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """class that defines all common attributes/methods for other classes"""
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates updated_at attribute with the current datetime"""
        self.updated_at = datetime.now

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        d = self.__dict__.copy
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat
        d['updated_at'] = self.updated_at.isoformat
        return d
