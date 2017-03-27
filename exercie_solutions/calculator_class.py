class Calculator:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def add(self):
        return self._num1 + self._num2

    def subtract(self):
        return self._num1 - self._num2

    def mult(self):
        return self._num1 * self._num2

    def divide(self):
        return self._num1 / self._num2

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

calc = Calculator(num1, num2)

print('add: {}'.format(calc.add()))
print('subtract: {}'.format(calc.subtract()))
print('mult: {}'.format(calc.mult()))
print('divide: {}'.format(calc.divide()))
