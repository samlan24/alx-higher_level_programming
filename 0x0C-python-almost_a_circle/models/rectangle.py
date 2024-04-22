#!/usr/bin/python3
"""models for the rectangle claa"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        self.__height = value

    @property
    def x(self):
        """gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets value of x"""
        self.__x = value

    @property
    def y(self):
        """gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        self.__y = value
