from __future__ import annotations
from collections.abc import Sequence
from typing import Protocol


class Product:
    ...


class StoreSubscriber(Protocol):
    def do_update(self, info: str):
        ...


class Store:
    def __init__(self, stock: Sequence[Product]):
        self._stock: list[Product] = list(stock)
        self._observers: list[StoreSubscriber] = []

    def add_to_stock(self, product: Product):
        ...
        self.send_notifications()

    def add_subscriber(self, customer: Customer):
        ...

    def remove_subscriber(self, customer: Customer):
        ...

    def send_notifications(self):
        for observer in self._observers:
            observer.do_update(...)


class Customer:
    def __init__(self, name: str):
        ...

    def do_update(self, info: str):
        ...
