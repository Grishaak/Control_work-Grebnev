from module.animals.TypesOfAnimal.camel_animal import CamelAnimal
from module.animals.TypesOfAnimal.cat_animal import CatAnimal
from module.animals.TypesOfAnimal.dog_animal import DogAnimal
from module.animals.TypesOfAnimal.donkey_animal import DonkeyAnimal
from module.animals.TypesOfAnimal.hamster_animal import HamsterAnimal
from module.animals.TypesOfAnimal.horse_animal import HorseAnimal
from module.constructor.encode import Encoder
from module.exceptions.InputException import InputExceptions


class ConstructorAnimal:

    def __init__(self):
        self.domestic_file = 'domestic_data.json'
        self.pethorse_file = 'pethorse_data.json'
        self.encoder = Encoder()
        self.domestic_list_animals = dict()
        self.domestic_index = 1
        self.pethorse_list_animals = dict()
        self.pethorse_index = 1

    def show_all_animals(self):
        result = ''
        result += 'Domestic animals:\n'
        for id_an, animal in self.domestic_list_animals.items():
            result += f'Индекс: {id_an}\n' + animal.__str__()
            result += "\n\n"
        result += '---------' * 3
        result += '\nPethorse animals:'
        for id_an, animal in self.pethorse_list_animals.items():
            result += f'Индекс: {id_an}\n' + animal.__str__()
            result += "\n"
        return result

    def show_certain_animals(self, type_id):
        result_animals = ''
        if type_id == "1":
            for i, animal in self.domestic_list_animals.items():
                result_animals += f'Индекс: {i}, Имя : {animal.show_name()}\n'
        elif type_id == '2':
            for i, animal in self.pethorse_list_animals.items():
                result_animals += f'Индекс: {i}, Имя : {animal.show_name()}\n'
        else:
            raise InputExceptions('Нет такого типа животного.')
        return result_animals

    def create_animal(self, type_an: int, animal_id: int, name, age):
        match type_an:
            case "1":
                match animal_id:
                    case "1":
                        animal = CatAnimal(name, age)
                    case "2":
                        animal = DogAnimal(name, age)
                    case "3":
                        animal = HamsterAnimal(name, age)
                    case _:
                        raise KeyError
                self.domestic_list_animals[self.domestic_index] = animal
                self.domestic_list_animals[self.domestic_index].set_type(type(animal).__name__)
                self.domestic_index += 1
            case "2":
                match animal_id:
                    case "1":
                        animal = HorseAnimal(name, age)
                    case "2":
                        animal = DonkeyAnimal(name, age)
                    case '3':
                        animal = CamelAnimal(name, age)
                    case _:
                        raise KeyError
                self.pethorse_list_animals[self.pethorse_index] = animal
                self.pethorse_list_animals[self.pethorse_index].set_type(type(animal).__name__)
                self.pethorse_index += 1
            case _:
                raise InputExceptions

    def add_command(self, type_id, animal_index, command: str):
        try:
            if type_id == '1':
                command = command.strip().split()
                for comm in command:
                    self.domestic_list_animals[animal_index].add_command(comm)
            elif type_id == '2':
                command = command.strip().split()
                for comm in command:
                    self.pethorse_list_animals[animal_index].add_command(comm)
            else:
                return InputExceptions('Нет таких типов животных.')
        except KeyError as key_err:
            return KeyError('Нет такого id животного.')

    def remove_animal(self, type_an: int, animal_index):
        try:
            if type_an == '1':
                result = self.domestic_list_animals.pop(animal_index)
            elif type_an == '2':
                result = self.pethorse_list_animals.pop(animal_index)
            else:
                return InputExceptions("Нет такого типа животного.")
            return f'Животное {result.show_name()} c индексом {animal_index} было удалено.'
        except KeyError:
            return KeyError("Нет такого id.")

    def count_all_animals(self):
        return (f"Домашних животных: {[animal.show_name() for animal in self.domestic_list_animals.values()]}"
                f"Вьючный животных: {[animal.show_name() for animal in self.pethorse_list_animals.values()]}")

    def delete_command(self, type_id, animal_index, del_command):
            match type_id:
                case '1':
                    if del_command == 'clear':
                        self.domestic_list_animals[animal_index].clear_commands()
                    else:
                        del_command = del_command.strip().split()
                        for index in del_command:
                            try:
                                self.domestic_list_animals[animal_index].delete_command(int(index))
                            except KeyError:
                                return KeyError('Нет такого id животного.')
                case '2':
                    if del_command == 'clear':
                        self.pethorse_list_animals[animal_index].clear_commands()
                    else:
                        del_command = del_command.strip().split()
                        for index in del_command:
                            try:
                                self.pethorse_list_animals[animal_index].delete_command(int(index))
                            except KeyError:
                                return KeyError('Нет такого id животного.')
                case _:
                    return InputExceptions("Нет такого животного")

    def save_to_json(self, type_id):
        try:
            if type_id == '1':
                domestic_data = self.domestic_list_animals
                self.encoder.encode_to_json(domestic_data, self.domestic_file)
            elif type_id == '2':
                pethorse_data = self.pethorse_list_animals
                self.encoder.encode_to_json(pethorse_data, self.pethorse_file)
            else:
                domestic_data = self.domestic_list_animals
                self.encoder.encode_to_json(domestic_data, self.domestic_file)
                pethorse_data = self.pethorse_list_animals
                self.encoder.encode_to_json(pethorse_data, self.pethorse_file)
        except IOError:
            raise IOError

    def load_saves(self):
        try:
            loaded_domestic_data = self.encoder.loads_saves(self.domestic_file)
            self.domestic_list_animals = loaded_domestic_data
            self.domestic_index = len(loaded_domestic_data.keys()) + 1
            loaded_pethorse_data = self.encoder.loads_saves(self.pethorse_file)
            self.pethorse_list_animals = loaded_pethorse_data
            self.pethorse_index = len(loaded_pethorse_data.keys()) + 1
        except OSError:
            raise OSError
