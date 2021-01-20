from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Стратегия — это поведенческий паттерн проектирования, который определяет
# семейство схожих алгоритмов и помещает каждый из них в собственный класс, после
# чего алгоритмы можно взаимозаменять прямо во время исполнения программы.


class RouteStrategy():
    def __init__(self, navigator: Navigator):
        self._navigator = navigator

    @property
    def navigator(self):
        return self._navigator

    @navigator.setter
    def navigator(self, navigator: Navigator):
        self._navigator = navigator

    def buildRoute(self):
        result = self._navigator.building_a_route()
        print(result)


class Navigator(ABC):
    @abstractmethod
    def building_a_route(self, data: List):
        pass


class RoadStrategy(Navigator):
    def building_a_route(self):
        _string = 'Route for Road build'
        return _string


class PublicTransportStrategy(Navigator):
    def building_a_route(self):
        _string = 'Route for Public Transport build'
        return _string


class WalkingStrategy(Navigator):
    def building_a_route(self):
        _string = 'Route for Walking build'
        return _string


if __name__ == "__main__":
    routeStrategy = RouteStrategy(RoadStrategy())
    print("Client: Building a route for Road.")
    routeStrategy.buildRoute()

    print("Client: Building a route for Walking.")
    routeStrategy.navigator = WalkingStrategy()
    routeStrategy.buildRoute()

    print("Client: Building a route for Public Transport")
    routeStrategy.navigator = PublicTransportStrategy()
    routeStrategy.buildRoute()