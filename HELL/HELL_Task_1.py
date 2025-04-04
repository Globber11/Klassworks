import re

def validate_date(date_input):
    if re.match(r'^\d{2}-\d{2}-\d{4}$', date_input):
        if int(date_input[-4 : -1]) % 4 == 0 and int(date_input[-4 : -1]) % 100 != 0 or int(date_input[-4 : -1]) % 4 == 0 and int(date_input[-4 : -1]) % 100 == 0 and int(date_input[-4 : -1]) % 400 == 0:
            if int(date_input[-7 : -6]) % 2 == 1:
                if re.match(r'[1-31]', date_input[-10 : -9]):
                    return True
            if int(date_input[-7 : -6]) % 2 == 0 and int(date_input[-7 : -6]) != 2:
                if re.match(r'[1-30]', date_input[-10 : -9]):
                    return True
            else:
                if re.match(r'[1-29]', date_input[-10 : -9]):
                    return True
    else:
        if int(date_input[-4 : -1]) % 4 == 0 and int(date_input[-4 : -1]) % 100 != 0 or int(date_input[-4 : -1]) % 4 == 0 and int(date_input[-4 : -1]) % 100 == 0 and int(date_input[-4 : -1]) % 400 == 0:
            if int(date_input[-7 : -6]) % 2 == 1:
                if re.match(r'[1-31]', date_input[-10 : -9]):
                    return True
            if int(date_input[-7 : -6]) % 2 == 0 and int(date_input[-7 : -6]) != 2:
                if re.match(r'[1-30]', date_input[-10 : -9]):
                    return True
            else:
                if re.match(r'[1-28]', date_input[-10 : -9]):
                    return True
        return False

if validate_date(input('Введите дату для проверки: ')):
    print('Дата введена верно')
else:
    print('Дата введена неверно')
