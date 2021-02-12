from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IMenu(ABC):
    @abstractmethod
    def operation(self):
        pass


class CompositeMenu(IMenu):
    def __init__(self, name: str):
        self._children: List[IMenu] = []
        self._name = name

    def add(self, child: IMenu):
        self._children.append(child)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"{self._name}({'/'.join(results)})"


class LeafMenu(IMenu):
    def __init__(self, name: str):
        self._name = name

    def operation(self):
        return self._name


def client_code(menu: IMenu):
    print(menu.operation())


if __name__ == "__main__":
    menu1 = CompositeMenu("Main page")
    menu1.add(LeafMenu("1Page"))
    menu1.add(LeafMenu("2Page"))
    menu1.add(LeafMenu("3Page"))
    menu1.add(LeafMenu("4Page"))

    menu2 = CompositeMenu("Main2")
    menu2.add(LeafMenu("1str"))
    menu2.add(LeafMenu("2str"))

    menu1.add(menu2)
    client_code(menu1)