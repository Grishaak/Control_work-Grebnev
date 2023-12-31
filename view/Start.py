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
                type_id = scaner('Введите цифру выбора: ')
                if type_id == '1':
                    print_text(menu_domestic_animal)
                elif type_id == '2':
                    print_text(menu_pethorse_animal)
                else:
                    print_text('Неверный ввод.')
                    continue
                animal_id = scaner('Введите цифру выбора: ')
                name = scaner('Введите имя животного: ')
                age = int(scaner('Введите возраст животного: '))
                flag = controller.create_animal(type_id, animal_id, name, age)
                if flag is not None:
                    print_text('Ошибка создания.')
            case '2':
                print_text(menu_choose_animal)
                type_id = scaner('Выберите тип животного : ')
                if type_id not in ('1', '2'):
                    print_text("Неверный ввод.")
                    continue
                print_text('Все животные этого типа: ')
                print_text(controller.show_certain_animals(type_id))
                animal_index = int(scaner('Введите индекс животного: \n'))
                print_text(controller.delete_animal(type_id, animal_index))
            case '3':
                print_text(controller.show_all_animal())
            case '4':
                print_text(menu_choose_animal)
                type_id = scaner('Выберите тип животного: ')
                print_text('Все животные этого типа: ')
                print_text(controller.show_certain_animals(type_id))
                animal_index = int(scaner('Введите индекс животного: '))
                command = scaner('Введите команду(ы) какие хотите добавить: ')
                if controller.add_command(type_id, animal_index, command):
                    print_text(f'Команды добавлены.')
            case "5":
                print_text(menu_choose_animal)
                type_id = scaner('Выберите тип животного: ')
                print_text('Все животные этого типа: ')
                print_text(controller.show_certain_animals(type_id))
                animal_index = int(scaner('Введите индекс животного: '))
                del_command = scaner('Для удаления всех команд, введите "clear",'
                                     ' для удаления выборочно - только индексы: ')
                controller.delete_command(type_id, animal_index, del_command)
            case '6':
                print_text(menu_choose_animal)
                print_text('Чтобы сохранить все данные введите "all".')
                type_id = scaner('Для выборочного сохранения введите цифру: ')
                controller.save_data(type_id)
            case '7':
                controller.load_data()
            case "8":
                break
            case _:
                print_text('Неверный ввод.')
