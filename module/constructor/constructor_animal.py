from module.animals.TypesOfAnimal.camel_animal import CamelAnimal
from module.animals.TypesOfAnimal.cat_animal import CatAnimal
from module.animals.TypesOfAnimal.dog_animal import DogAnimal
from module.animals.TypesOfAnimal.donkey_animal import DonkeyAnimal
from module.animals.TypesOfAnimal.hamster_animal import HamsterAnimal
from module.animals.TypesOfAnimal.horse_animal import HorseAnimal
from module.animals.domestic_animal import DomesticAnimal


class ConstructorAnimal:
    def __init__(self):
        self.domestic_list_animals = []
        self.pethorse_list_animals = []

    def show_all_animals(self):
        result = ''
        result += 'Domestic animals:'
        for animal in self.domestic_list_animals:
            result += animal
        result += '\nPethorse animals:'
        for animal in self.pethorse_list_animals:
            result += animal

    def create_animal(self, type_an: int, animal_id: int, name, age):
        match type_an:
            case 1:
                match animal_id:
                    case 1:
                        animal = CatAnimal(name, age)
                    case 2:
                        animal = DogAnimal(name, age)
                    case 3:
                        animal = HamsterAnimal(name, age)
                self.domestic_list_animals.append(animal)

            case 2:
                match animal_id:
                    case 1:
                        animal = HorseAnimal(name, age)
                    case 2:
                        animal = DonkeyAnimal(name, age)
                    case 3:
                        animal = CamelAnimal(name, age)
                self.pethorse_list_animals.append(animal)

    def remove_animal(self, type_an: int, animal_index):
        if type_an == 1:
            self.domestic_list_animals.pop(animal_index)
        else:
            self.pethorse_list_animals.pop(animal_index)

    def count_all_animals(self):
        return (f"Домашних животных: {[animal.show_name() for animal in self.domestic_list_animals]}"
                f"Вьючный животных: {[animal.show_name() for animal in self.pethorse_list_animals]}")
