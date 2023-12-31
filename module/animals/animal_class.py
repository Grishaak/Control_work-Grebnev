from datetime import date
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, age=date.today(), command='', type_animal=''):
        if command == '':
            self._commands = []
        elif type(command) == list:
            self._commands = command
        else:
            self._commands = [command]
        self._name = name
        self._age = age
        if type_animal == '':
            self._type_animal = ''
        else:
            self._type_animal = type_animal

    @abstractmethod
    def __str__(self):
        return f'Имя: {self._name}, Дата рождения: {self._age}'

    @abstractmethod
    def add_command(self, command: str):
        self._commands.append(command)

    @abstractmethod
    def delete_command(self, del_commands_list):
        for index in del_commands_list:
            self._commands.pop(index)

    @abstractmethod
    def clear_commands(self):
        self._commands = []

    @abstractmethod
    def show_name(self):
        return self._name

    @abstractmethod
    def show_age(self):
        return self._age

    def set_type(self, type_an):
        self._type_animal = type_an
