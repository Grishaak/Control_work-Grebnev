from datetime import date

from module.animals.animal_class import Animal


class DomesticAnimal(Animal):
    def __init__(self, name: str, age=date.today()):
        super().__init__(name, age)

    def __str__(self):
        respond = super().__str__() + \
                  f'\nТип животного: {DomesticAnimal.__name__}' + \
                  (f'\nКоманды: {self.__commands}' if self.__commands else "\nНе выполняет никаких команд")
        return respond

    def add_command(self, command: str):
        self.__commands.append(command)

    def change_name(self, new_name):
        self.__name = new_name

    def change_age(self, new_age):
        self.__age = new_age

    def show_name(self):
        return self.__name

    def show_age(self):
        return self.__age
