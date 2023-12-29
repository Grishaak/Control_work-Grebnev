from module.animals.pethorse_animal import PetHorseAnimal


class HorseAnimal(PetHorseAnimal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        respond = super().__str__() + \
                  f'\n Вид животного: Horse'
        return respond