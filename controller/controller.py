from module.constructor.constructor_animal import ConstructorAnimal
from module.exceptions import InputException
from module.exceptions.InputException import InputExceptions


class Controller:
    def __init__(self):
        self.constructor = ConstructorAnimal()

    def create_animal(self, type_id, animal_id, name, age):
        try:
            self.constructor.create_animal(type_id, animal_id, name, age)
        except KeyError:
            return KeyError.__name__

    def show_certain_animals(self, type_id):
        try:
            x = self.constructor.show_certain_animals(type_id)
            return x
        except InputExceptions:
            return InputExceptions("Нет такого животного.")


    def delete_animal(self, type_id, animal_index):
        try:
            x = self.constructor.remove_animal(type_id, animal_index)
            return x
        except InputException:
            return InputException
        except KeyError:
            return KeyError("Нет такого id.")

    def show_all_animal(self):
        return self.constructor.show_all_animals()

    def add_command(self, type_id, animal_index, command):
        try:
            self.constructor.add_command(type_id, animal_index, command)
        except (InputException, KeyError):
            return False

    def delete_command(self, type_id, animal_index, del_command):
        try:
            self.constructor.delete_command(type_id, animal_index, del_command)
        except (InputException, KeyError):
            return False

    def save_data(self, type_id):
        try:
            self.constructor.save_to_json(type_id)
        except IOError as io:
            return io('Не удалось записать файл')

    def load_data(self):
        try:
            self.constructor.load_saves()
        except OSError as oe:
            return oe
