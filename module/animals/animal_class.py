from datetime import date
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, age=date.today()):
        self.__name = name
        self.__age = age
        self.__commands = []

    @abstractmethod
    def __str__(self):
        return f'Имя: {self.__name}, Дата рождения: {self.__age}'

    @abstractmethod
    def add_command(self, command: str):
        self.__commands.append(command)
