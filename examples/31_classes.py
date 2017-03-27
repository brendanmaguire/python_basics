class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def describe(self):
        print('My name is {} and my age is {}'.format(self._name, self._age))

my_dog = Dog('Rover', 3)
my_dog.describe()

