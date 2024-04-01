class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print('bark bark')


class Cat(Animal):
    def sound(self):
        print('Meow meow')


dog = Dog('russel')
cat = Cat('lulu')

dog.get_name()
cat.get_name()
dog.sound()
cat.sound()
animal = Animal('amal')
animal.get_name()
animal.sound()  # this won't work since i didn't give this any statements to execute.
