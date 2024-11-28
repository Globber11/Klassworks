def check_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n" + "="*30)
        func(*args, **kwargs)
        print("="*30 + "\n")
    return wrapper

    return products[user_input]

@check_decorator
def check(buskett, listD):
    moreCost = 0
    print('Ваш чек:')
    for i in range(0,len(buskett),3):
        print(f"{buskett[i]}: {buskett[i+1]} x {buskett[i+2]}шт")
        moreCost+=buskett[i+1]*buskett[i+2]
    print(' ')
    print(f'Оплачено: {moreCost}')
    if listD[0]==1:
        print(f'Внесено: {listD[1]}')
        print(f'Сдача: {listD[1]-moreCost}')


def buy(buskett):
    mostCost = 0
    for i in range(0,len(buskett),3):
        mostCost+=buskett[i+1]*buskett[i+2]
    print(f'Итого к оплате: {mostCost}')
    print('Оплата картой или наличными?')
    print('1)Наличные\n2)Карта')
    try:
        bought = int(input('Введите цифру соответствующую ващему выбору: '))
    except ValueError:
        print('Введи числовое значение!!!')
        buy(buskett)
    CardOrNal = None
    if bought==1:
        try:
            CardOrNal = int(input('Внесите сумму в рублях: '))
            if CardOrNal<mostCost:
                print('Нехватает денежных средств!!!')
            elif CardOrNal<0:
                print('Долги берут в банке а не в кафе!!!')
                buy(buskett)
        except ValueError:
            print('Введи числовое значение!!!')
            buy(buskett)
    elif bought==2:
        pass
    else:
        print('Такого варианта ответа нет!!!')
        buy(buskett)
    return [bought, CardOrNal]

def menu(user_input):
    products = {
        1: 'пепперони',
        2: 'маргарита',
        3: 'четыре сыра',
        4: 'ветчина и грибы',
        5: 'минипицца',
        6: 'сок'
    }
    return products[user_input]
def menu18(user_input):
    products = {
        1: 'пепперони',
        2: 'маргарита',
        3: 'четыре сыра',
        4: 'ветчина и грибы',
        5: 'пиво',
        6: 'виски с колой',
        7: 'кальянчик'
    }
    return products[user_input]
def printMenu():
    print('Меню: ')
    for i in range(1, 6):
        print(f'   {i}){menu(i)}: {cost(menu(i))}')
def printMenu18():
    print('Меню: ')
    for i in range(1, 7):
        print(f'   {i}){menu18(i)}: {cost18(menu18(i))}')
def cost(key):
    cost = {
        'пепперони': 50,
        'маргарита': 100,
        'четыре сыра':200,
        'ветчина и грибы':250,
        'минипицца': 300,
        'сок': 350
    }
    return cost[key]
def cost18(key):
    cost = {
        'пепперони': 50,
        'маргарита': 100,
        'четыре сыра':200,
        'ветчина и грибы':250,
        'пиво': 300,
        'виски с колой': 350,
        'кальянчик': 500
    }
    return cost[key]
def print_menu(user_data):
    if 2024-2000>=18:
        printMenu18()
    else:
        printMenu()
