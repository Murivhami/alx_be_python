#!/bin/bash

class Calculator:
    calculation_type = "Arithmetic Operations"
    def __init__(self, calculation_type):
        self.calculation_type = "multiply"
    
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

