import datetime

from controller.controller import Controller
from Texts import *


def start():
    controller = Controller()
    while True:
        print_text(menu_text)
        choice = scaner(input_number)
        match choice:
            case '1':
                print_text(menu_choose_animal)
                animal_id = scaner('Введите цифру выбора: ')