from datetime import date

from module.animals.animal_class import Animal


class PetHorseAnimal(Animal):
    def __init__(self, name: str, age=0, commands='', type_animal=''):
        super().__init__(name, age, commands, type_animal)

    def __str__(self):
        respond = super().__str__() + \
                  f'\nТип животного: {PetHorseAnimal.__name__}' + \
                  (f'\nКоманды: {self._commands}' if self._commands else "\nНе выполняет никаких команд")
        return respond

    def add_command(self, command: str):
        self._commands.append(command)

    def delete_command(self, del_commands_list):
        for index in del_commands_list:
            self._commands.pop(index)

    def clear_commands(self):
        self._commands = []

    def change_name(self, new_name):
        self._name = new_name

    def change_age(self, new_age):
        self._age = new_age

    def show_name(self):
        return self._name

    def show_age(self):
        return self._age
