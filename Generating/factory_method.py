from __future__ import annotations
from abc import ABC, abstractmethod


class FactoryRequest(ABC):
    @abstractmethod
    def createRequest(self):
        pass

    def some_operation(self):
        request = self.createRequest()
        result = f"Creator: The same creator's code has just worked with {request.operation()}"
        return result


class FactoryRequestA(FactoryRequest):
    def createRequest(self):
        return ConcrectRequestA()


class FactoryRequestB(FactoryRequest):
    def createRequest(self):
        return ConcrectRequestB()


class ConcretRequest(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcrectRequestA(ConcretRequest):
    def operation(self):
        return "{Result of the ConcrectRequestA}"


class ConcrectRequestB(ConcretRequest):
    def operation(self):
        return "{Result of the ConcrectRequestB}"


def client_code(creator: FactoryRequest):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcrectRequestA.")
    client_code(FactoryRequestA())
    print("\n")

    print("App: Launched with the ConcrectRequestB.")
    client_code(FactoryRequestB())