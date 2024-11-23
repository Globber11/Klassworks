from model import user_data

def menu(user_input):
    global products
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
    global products
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
if 2024-user_data[born_year]>=18:
    printMenu18()
else:
    printMenu()
