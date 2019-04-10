import os
import psutil
import sys


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
    print('[3] - Выведу список процессов')
    do = int(input('Укажите номер действия:'))
    
    if do == 1:
        print(os.listdir())
    elif do == 2:
        print('Логин пользователя: ' + os.getlogin())
        print('Количество CPU: ' + str(os.cpu_count()))
        print('Кодировка файловой системы: ' + sys.getfilesystemencoding())
        print('Текущая директория: ' + os.getcwd())
        print('Платформа (ОС): ' + sys.platform)
    elif do == 3:
        print(psutil.pids())
    else:
        pass
    
elif answer == 'n':
    print('До свидания!')
else:
    print('Неизвестный ответ')
