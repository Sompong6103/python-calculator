class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            if b < 0:
                result = self.subtract(result, a)
                continue
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0: return "Undefined"
        is_negative = (a < 0) ^ (b < 0)

        result = 0

        numerator = abs(a)
        denominator = abs(b)

        while numerator >= denominator:
            numerator = self.subtract(numerator, denominator)
            result += 1

        if is_negative:
            result = -result
        return result
    
    def modulo(self, a, b):
        if b == 0: 
            return "Undefined"
        
        if a < 0 or b < 0:
            return "Error: Requires positive inputs for this method."
            
        while a >= b: 
            a = self.subtract(a, b) 

        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))