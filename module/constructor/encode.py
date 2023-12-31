import json
from json import JSONEncoder, JSONDecoder

from module.animals.TypesOfAnimal.camel_animal import CamelAnimal
from module.animals.TypesOfAnimal.cat_animal import CatAnimal
from module.animals.TypesOfAnimal.dog_animal import DogAnimal
from module.animals.TypesOfAnimal.donkey_animal import DonkeyAnimal
from module.animals.TypesOfAnimal.hamster_animal import HamsterAnimal
from module.animals.TypesOfAnimal.horse_animal import HorseAnimal


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

    def from_json(self, json_object):
        wrap_rotate = [CatAnimal, DogAnimal, HamsterAnimal, DonkeyAnimal, HorseAnimal, CamelAnimal]
        for item in wrap_rotate:
            if item.__name__ == str(json_object['_type_animal']):
                x = item(json_object['_name'], json_object["_age"], json_object["_commands"],
                         json_object['_type_animal'])
                return x

    def encode_to_json(self, animal_dict: dict, file):
        try:
            with open(file, "w") as fp:
                for animal in animal_dict.values():
                    product_encoded = json.dumps(animal, cls=Encoder)
                    fp.writelines(product_encoded)
                    fp.writelines("\n")
        except IOError:
            raise IOError

    def loads_saves(self, file_to_open):
        try:
            with open(file_to_open, "r") as x:
                lines = sum([1 for line in x])
            data = dict()
            with open(file_to_open, "r") as r:
                for i in range(1, lines + 1):
                    loaded_file = r.readline()
                    animal = JSONDecoder(object_hook=self.from_json).decode(loaded_file)
                    data[i] = animal
            return data
        except OSError:
            raise OSError
