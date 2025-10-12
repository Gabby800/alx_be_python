# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static Method
    @staticmethod
    def add(a, b):
        """
        Static methods do not depend on class or instance data.
        They simply perform a function related to the class.
        """
        return a + b

    # Class Method
    @classmethod
    def multiply(cls, a, b):
        """
        Class methods have access to the class itself via 'cls'.
        They can read or modify class-level data.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
