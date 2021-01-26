from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

# Итератор — это поведенческий паттерн, позволяющий
# последовательно обходить сложную коллекцию, без
# раскрытия деталей её реализации.

переписать юмл !

class FilterController(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: DataBase, reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class DataBase(Iterable):
    def __init__(self, collection: List[Any] = []):
        self._collection = collection

    def __iter__(self):
        return FilterController(self._collection)

    def get_reverse(self):
        return FilterController(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    dataBase = DataBase()
    dataBase.add_item("First Record")
    dataBase.add_item("Second Record")
    dataBase.add_item("Third Record")

    print("Straight traversal:")
    print("\n".join(dataBase))
    print("")

    print("Reverse traversal:")
    print("\n".join(dataBase.get_reverse()), end="")