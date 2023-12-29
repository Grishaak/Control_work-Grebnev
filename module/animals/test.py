from datetime import date

from module.animals.TypesOfAnimal.camel_animal import CamelAnimal
from module.animals.TypesOfAnimal.cat_animal import CatAnimal
from module.animals.TypesOfAnimal.dog_animal import DogAnimal
from module.animals.TypesOfAnimal.donkey_animal import DonkeyAnimal
from module.animals.TypesOfAnimal.hamster_animal import HamsterAnimal
from module.animals.TypesOfAnimal.horse_animal import HorseAnimal
from module.animals.domestic_animal import DomesticAnimal
from module.animals.pethorse_animal import PetHorseAnimal

test_animal = DomesticAnimal('Вася', date(2020, 12, 31))
test_animal.add_command("Прыгать")
test_animal1 = DomesticAnimal("Иван")
test_animal2 = PetHorseAnimal("Борька")
cat = CatAnimal('Миша', 10)
dog = DogAnimal("Кира", 13)
hamster = HamsterAnimal('Жека', 9)
donkey = DonkeyAnimal("Боря", 5)
horse = HorseAnimal("Вера", 12)
camel = CamelAnimal("Эмир", 4)

print(cat)
print()
print(dog)
print()
print(hamster)
print()
print(horse)
print()
print(donkey)
print()
print(camel)
