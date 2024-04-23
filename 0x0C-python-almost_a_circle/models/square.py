#!/usr/bin/python3
"""models for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super.__init__(size, size, x, y, id)

    def __str__(self):
        """format for string representation of the square class"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
