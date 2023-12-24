from datetime import date

from module.animals.animal_class import Animal


class DomesticAnimal(Animal):
    def __init__(self, name: str, age=date.today()):
        self.name = name
        self.age = age
        self.commands = []

    def __str__(self):
        respond = super().__str__() + \
                  f'\nТип животного: {DomesticAnimal.__name__}' + \
                  (f'\nКоманды: {self.commands}' if self.commands else "\nНе выполняет никаких команд")
        return respond

    def add_command(self, command: str):
        self.commands.append(command)
