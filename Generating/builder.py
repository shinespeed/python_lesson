from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class RequestA:
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Request: {', '.join(self.parts)}", end="")


class RequestB:
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Request parts: {', '.join(self.parts)}", end="")


class BuilderRequest(ABC):
    @abstractmethod
    def request(self):
        pass

    @abstractmethod
    def requestStepA(self):
        pass

    @abstractmethod
    def requestStepB(self):
        pass

    @abstractmethod
    def requestStepC(self):
        pass


class CreateRequestA(BuilderRequest):
    def __init__(self):
        self.reset()

    def reset(self):
        self._request = RequestA()

    @property
    def request(self):
        request = self._request
        self.reset()
        return request

    def requestStepA(self):
        self._request.add("Request A Step A")

    def requestStepB(self):
        self._request.add("Request A Step B")

    def requestStepC(self):
        self._request.add("Request A Step C")


class CreateRequestB(BuilderRequest):
    def __init__(self):
        self.reset()

    def reset(self):
        self._request = RequestB()

    @property
    def request(self):
        request = self._request
        self.reset()
        return request

    def requestStepA(self):
        self._request.add("Request B Step A")

    def requestStepB(self):
        self._request.add("Request B Step B")

    def requestStepC(self):
        self._request.add("Request B Step C")


class Director:
    def __init__(self):
        self._builderRequest = None

    @property
    def builderRequest(self):
        return self._builderRequest

    @builderRequest.setter
    def builderRequest(self, builderRequest: BuilderRequest):
        self._builderRequest = builderRequest

    def build_min_request(self):
        self.builderRequest.requestStepC()

    def build_mid_request(self):
        self.builderRequest.requestStepA()
        self.builderRequest.requestStepC()

    def build_max_request(self):
        self.builderRequest.requestStepA()
        self.builderRequest.requestStepB()
        self.builderRequest.requestStepC()


if __name__ == "__main__":
    builder = CreateRequestB()
    director = Director()
    director.builderRequest = builder
    director.build_max_request()
    builder.request.list_parts()
