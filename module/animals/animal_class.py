from datetime import date
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, age=date.today()):
        self.name = name
        self.age = age
        self.commands = []

    @abstractmethod
    def __str__(self):
        return f'Имя: {self.name}, Дата рождения: {self.age}'

    @abstractmethod
    def add_command(self, command: str):
        self.commands.append(command)
