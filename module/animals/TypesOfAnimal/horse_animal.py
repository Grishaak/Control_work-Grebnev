from module.animals.pethorse_animal import PetHorseAnimal


class HorseAnimal(PetHorseAnimal):
    def __init__(self, name, age=0, commands='', type_animal='Animal'):
        super().__init__(name, age, commands, type_animal)

    def __str__(self):
        respond = super().__str__() + \
                  f'\nВид животного: Horse'
        return respond