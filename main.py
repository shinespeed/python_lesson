from abc import ABC, abstractmethod


class Animal:
    @abstractmethod
    def func_say(self):
        pass


class Dog(Animal):
    def func_say(self):
        print('gav gav')


class Cat(Animal):
    def func_say(self):
        print('may may')


class Speak:
    def __init__(self, animal: Animal):
        animal.func_say()


if __name__ == '__main__':
    cat = Dog()
    Speak(cat)