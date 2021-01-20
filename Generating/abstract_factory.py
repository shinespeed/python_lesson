from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactoryResponse(ABC):
    @abstractmethod
    def createResponseA(self):
        pass

    @abstractmethod
    def createResponseB(self):
        pass


class FactoryChrome(AbstractFactoryResponse):
    def createResponseA(self):
        return ChromeResponseA()

    def createResponseB(self):
        return ChromeResponseB()


class FactorySafari(AbstractFactoryResponse):
    def createResponseA(self):
        return SafariResponseA()

    def createResponseB(self):
        return SafariResponseB()


class ResponseA(ABC):
    @abstractmethod
    def someOperationA(self):
        pass


class ChromeResponseA(ResponseA):
    def someOperationA(self):
        return "Chrome Response A"


class SafariResponseA(ResponseA):
    def someOperationA(self):
        return "Safari Response A"


class ResponseB(ABC):
    @abstractmethod
    def someOperationB(self):
        pass


class ChromeResponseB(ResponseB):
    def someOperationB(self):
        return "Chrome Response B"


class SafariResponseB(ResponseB):
    def someOperationB(self):
        return "Safari Response B"


def client_code(factory: AbstractFactoryResponse):
    response_a = factory.createResponseA()
    response_b = factory.createResponseB()

    print(f"{response_b.someOperationB()}")
    print(f"{response_a.someOperationA()}", end="")


if __name__ == "__main__":
    client_code(FactorySafari())
    print("\n")
    client_code(FactoryChrome())
