print('программа номер 1')
print('Привет программист!')
name = input('Ваше имя:')
print(name, ', добро пожаловать в мир Python!')
answer = input('Давайте поработаем? (Y/N)')
if answer == 'y':
    print('Отлично хозяин!')
    print('Я умею:')
    print('[1] - выведу список файлов')
    print('[2] - выведу информацию о системе')
    do = input('Укажите номер действия:')
    if do == 1:
        pass
    elif do == 2:
        pass
    else:
        pass
elif answer == 'n':
    print('До свидания!')
else:
    print('Неизвестный ответ')
