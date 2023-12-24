from datetime import date

from module.animals.domestic_animal import DomesticAnimal
from module.animals.pethorse_animal import PetHorseAnimal

test_animal = DomesticAnimal('Вася', date(2020, 12, 31))
test_animal.add_command("Прыгать")
test_animal1 = DomesticAnimal("Иван")
test_animal2 = PetHorseAnimal("Борька")

print(test_animal)
print()
print(test_animal1)
print()
print(test_animal2)
