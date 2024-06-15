

class NumberOperations:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sum_numbers(self):
        return self.num1 + self.num2 + self.num3

    def multiply_numbers(self):
        return self.num1 * self.num2 * self.num3


# Create an instance of the NumberOperations class
operations = NumberOperations(2, 3, 4)

# Sum the numbers
print("Sum:", operations.sum_numbers())  # Output: Sum: 9

# Multiply the numbers
print("Product:", operations.multiply_numbers())  # Output: Product: 24
