#(link unavailable)
class Calculator:
    def __init__(self):
        self.operations = {
            "1": self.add,
            "2": self.subtract,
            "3": self.multiply,
            "4": self.divide,
        }

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")

    def calculate(self):
        print("Simple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose an operation (1/2/3/4): ")

        if choice in self.operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                result = self.operations[choice](num1, num2)
                print(f"Result: {num1} {self.get_symbol(choice)} {num2} = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid operation choice.")


    def get_symbol(self, choice):
        symbols = {
            "1": "+",
            "2": "-",
            "3": "*",
            "4": "/",
        }
        return symbols[choice]


def main():
    calculator = Calculator()
    calculator.calculate()


if __name__ == "__main__":
    main()


 
