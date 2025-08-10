
class Calculator:
    
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Performs addition without accessing class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Performs multiplication and can access class attributes via 'cls'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
