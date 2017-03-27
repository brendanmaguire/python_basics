class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def describe(self):
        return 'This is {} and she is {} years old.'.format(
            self._name, self._age)

    def speak(self):
        raise NotImplemented('speak method is not implemented')

