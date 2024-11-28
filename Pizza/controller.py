from view import print_menu
from model import busketSave
from model import reg_and_create_id
from view import buy
from view import check
def zakaz():
    print_menu(1)
    busket = []
    try:
        print('Что вы хотели бы заказать?')
        user_input = int(input('Введите цифру соответствующую ващему выбору: '))
        user_number = int(input('введите количество: '))
        busketSave(busket, user_input, user_number)
        if input('Для продолжения заказа введите 1, иначе любой символ: ')=='1':
            zakaz()
        else:
            check(busket, buy(busket))
    except KeyError:
        print('Такого варианта нет!!!')
        zakaz()
    except ValueError:
        print('Введите число а не букву!!!')
        zakaz()
def openPizza():
    reg_and_create_id()
    zakaz()
