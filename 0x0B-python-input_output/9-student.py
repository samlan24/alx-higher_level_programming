#!/usr/bin/python3
"""this is a student class"""


class Student:
    """student class initialization"""


def __init__(self, first_name, last_name, age):
    """student initialization"""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self):
    """retrieves dictionary representation of student instance"""
    return self.__dict__
