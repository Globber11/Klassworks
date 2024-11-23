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
    for i in range(1, 5):
        print(f'   {i}){menu(i)}: {cost(menu(i))}')
