class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed

    def speak(self):
        return 'Woof woof!'

    def describe(self):
        return super().describe() +
            ' She is a {}'.format(self._breed)

