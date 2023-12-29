from module.animals.domestic_animal import DomesticAnimal


class HamsterAnimal(DomesticAnimal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        respond = super().__str__() + \
                  f'\n Вид животного: Hamster'
        return respond
