import math           

class CalculatorLogic:
    def __init__(self):
        self.expression = ""
        self.result_var = ""
    
    def evaluate(self):
        try:
            result = eval(self.expression)
            self.previous_expression = self.expression
            return str(result)
        except Exception as e:
            return "Error"

    def sqrt_root(self):
        try:
            result = math.sqrt(float(self.expression))
            result_var = str(result)
            self.previous_expression = f"√({self.expression})"
            return str(result_var)
        except Exception as e:
            return "Error"

    def power(self, exponent):
        try:
            result = pow(float(self.expression), exponent)
            self.previous_expression = f"({self.expression})\u00b2"
            return str(result)
        except Exception as e:
            return "Error"

    def logarithm(self):
        try:
            result = math.log(float(self.expression))
            self.previous_expression = f"log({self.expression})"
            return str(result)
        except Exception as e:
            return "Error"
