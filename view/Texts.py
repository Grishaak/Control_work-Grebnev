def print_text(text):
    print(text)


menu_text = """\n1. Создать животное.
2. Удалить животное.
3. Промотреть всех животных.
4. Добавить команду животному.
5. Удалить команду(ы).
6. Сохранить данные.
7. Загрузить данные.
8. Выйти.\n"""

menu_choose_animal = """\n1. Домашнее животное.
2. Вьючное животное.\n"""

menu_domestic_animal = """\n1. Создать животное Cat. 
2. Создать животное Dog.
3. Создать животное Hamster.\n"""
menu_pethorse_animal = """\n1. Создать животное Donkey. 
2. Создать животное Horse.
3. Создать животное Camel.\n"""

input_number = "Введите цифру: "
error_input = "Невверный ввод."
input_index = "Введите индекс искомого животного: "
input_text = "Введите текст: "


def scaner(text):
    return input(text)
