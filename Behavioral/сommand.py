from __future__ import annotations
from abc import ABC, abstractmethod

#Команда — это поведенческий паттерн проектирования, который
# превращает запросы в объекты, позволяя передавать их
# как аргументы при вызове методов, ставить запросы в очередь,
# логировать их, а также поддерживать отмену операций.


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class OkCommand(Command):
    def __init__(self, payload: str):
        self._payload = payload

    def execute(self):
        print(f"OkCommand: "
              f"({self._payload})"
              f" ...command executed")


class SaveCommand(Command):
    def __init__(self, controller: Controller, a: str, b: str):
        self._controller = controller
        self._a = a
        self._b = b

    def execute(self):
        print("SaveCommand: call controller", end="")
        self._controller.do_something(self._a)
        self._controller.do_something_else(self._b)


class Controller:
    def do_something(self, a: str):
        print(f"\nController: Working on ({a}.)", end="")

    def do_something_else(self, b: str):
        print(f"\nController: Also working on ({b}.)", end="")


class Button:
    _first_command = None
    _second_command = None

    def set_first_command(self, command: Command):
        self._first_command = command

    def set_second_command(self, command: Command):
        self._second_command = command

    def execute_command(self):
        print("Button: I'm waiting for the command...")
        self._first_command.execute()
        print("Button: ...doing something really important...")
        self._second_command.execute()


if __name__ == "__main__":
    button = Button()
    button.set_first_command(OkCommand("Hi!"))
    controller = Controller()
    button.set_second_command(SaveCommand(controller, "Send email", "Save report"))
    button.execute_command()