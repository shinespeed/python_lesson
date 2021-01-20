from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

# Цепочка обязанностей — это поведенческий паттерн проектирования, который
# позволяет передавать запросы последовательно по цепочке обработчиков.
# Каждый последующий обработчик решает, может ли он обработать запрос сам и
# стоит ли передавать запрос дальше по цепи.


class Command(ABC):
    @abstractmethod
    def set_next(self, command: Command):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractCommand(Command):
    _next_command: Command = None

    def set_next(self, command: Command):
        self._next_command = command
        return command

    @abstractmethod
    def handle(self, request: Any):
        if self._next_command:
            return self._next_command.handle(request)
        return None


class ServerA(AbstractCommand):
    def handle(self, request: Any):
        if request == "ScriptA":
            return f"I'm ServerA and i like {request}"
        else:
            return super().handle(request)


class ServerB(AbstractCommand):
    def handle(self, request: Any):
        if request == "ScriptB":
            return f"I'm ServerB and i like {request}"
        else:
            return super().handle(request)


class ServerC(AbstractCommand):
    def handle(self, request: Any):
        if request == "ScriptC":
            return f"I'm ServerC and i like {request}"
        else:
            return super().handle(request)


def client_code(command: Command):
    for request in ["ScriptA", "ScriptB", "ScriptC"]:
        print(f"\nClient: Who wants a {request}?")
        result = command.handle(request)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {request} was left untouched.", end="")


if __name__ == "__main__":
    serverA = ServerA()
    serverB = ServerB()
    serverC = ServerC()

    serverA.set_next(serverB).set_next(serverC)

    print("Chain: ServerA > ServerB > ServerC")
    client_code(serverA)
    print("\n")

    print("Subchain: ServerB > ServerC")
    client_code(serverB)