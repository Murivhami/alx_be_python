#!/bin/bash
import math

class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = self.length * self.width
    def __str__(self):
        return f"The area of the Rectangle is: {self.area}"
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        area = math.pi * self.radius, "** 2"
    
    def __str__(self):
        return f"The area of the Circle is: {self.area}"
