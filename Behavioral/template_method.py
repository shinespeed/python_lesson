from abc import ABC, abstractmethod

# Шаблонный метод — это поведенческий паттерн проектирования, который
# определяет скелет алгоритма, перекладывая ответственность за некоторые
# его шаги на подклассы. Паттерн позволяет подклассам переопределять шаги
# алгоритма, не меняя его общей структуры.

class GameAI(ABC):
    def template_method(self) -> None:
        self.base_operation()
        self.buildUnits()
        self.heavyWeapon()
        self.easyWeapon()


    def base_operation(self):
        print("GameAI: creating a basic template")

    @abstractmethod
    def buildUnits(self):
        pass

    def heavyWeapon(self):
        pass

    def easyWeapon(self):
        pass


class Teminators(GameAI):
    def buildUnits(self):
        print("Teminators: metal frame")

    def heavyWeapon(self):
        print("Teminators: MINIGAN!!!")


class Humans(GameAI):
    def buildUnits(self):
        print("Humans: Protein structure")

    def easyWeapon(self):
        print("Humans: ak - 47")


def client_code(gameAI: GameAI) -> None:
    gameAI.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(Teminators())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(Humans())
