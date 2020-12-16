class Car:
    __model = 'undefined'
    __speed = 0

    def __init__(self, speed, model):
        self.__model = model
        self.__speed = speed

    def print_character(self):
        print(self.__model, self.__speed)


class ElectricalCar(Car):
    def __init__(self):
        super().__init__(self)


car = Car(250, "lada")
car.print_character()
