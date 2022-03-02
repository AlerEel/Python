import random
from time import sleep
import math

#Минимально-возможное количество попыток для точного решения
def number_of_attempts(limit):
    n = int(limit)
    return math.ceil(math.log(n, 2))

#Проверка введенных данных, число ли это.
def is_valid(number):
    if number.isdigit() == True:
        return True
    else: return False

#Приветствие
print('Добро пожаловать в игру "Угадай число"')
sleep(1)
print('Я загадаю любое число от 1 до введенного вами')
sleep(1)
print('Если не хотите продолжать игру, введите 0')
n = 1 #Условие продолжения игры 1 - да, 0 - нет.

#Игра без ограничения на количество попыток.
def game_light():
    sleep(1)
    print('введите число, больше которого мне не загадывать')
    limit = input()

    while is_valid(limit) == False:
        print('А, может быть, все-таки введем целое число?')
        limit = input()

    print(f'Я загадал число от 1 до {limit}, ваша задача - угадать, какое число я загадал')
    x = random.randint(1, int(limit))
    number = ''
    count = 0

    while x != number:
        print('Введите число')
        number = input()
        if is_valid(number) == False:
            print('А может быть все-таки введем целое число?')
        else:
            if int(number) == 0:
                print('Игра окончена')
                print(f'Число, которое было загадано - {x}')
                break
            if int(number) == x:
                count += 1
                print('Поздравляю, вы угадали!')
                print(f'Вы использовали {count} попыток')
                break
            elif int(number) < x:
                print("Введенное вами число меньше загаданного, попробуйте еще раз")
                count += 1
                continue
            elif int(number) > x:
                print("Введенное вами число больше загаданного, попробуйте еще раз")
                count += 1
                continue

#Игра с ограничением на количество попыток.
def game_hard():
    sleep(1)
    print('введите число, больше которого мне не загадывать')
    limit = input()

    while is_valid(limit) == False:
        print('А, может быть, все-таки введем целое число?')
        limit = input()

    sleep(1)
    print(f'Я загадал число от 1 до {limit}, ваша задача - угадать, какое число я загадал')
    attempts = number_of_attempts(limit)
    print(f'У вас для этого есть  {attempts} попыток')
    x = random.randint(1, int(limit))
    number = ''
    count = 0

    while x != number:
        print('Введите число')
        number = input()
        if is_valid(number) == False:
            print('А может быть все-таки введем целое число?')
        else:
            if count < attempts:
                if int(number) == 0:
                    print('Игра окончена')
                    print(f'Число, которое было загадано - {x}')
                    break
                if int(number) == x:
                    count += 1
                    print('Поздравляю, вы угадали!')
                    print(f'Вы использовали {count} попыток')
                    break
                elif int(number) < x:
                    print("Введенное вами число меньше загаданного, попробуйте еще раз")
                    count += 1
                    continue
                elif int(number) > x:
                    print("Введенное вами число больше загаданного, попробуйте еще раз")
                    count += 1
                    continue
            else:
                print(f"Попытки исчерпаны, число, которое было загадано - {x}")
                break

#Выполнение программы.
while n != 0:
    sleep(1)
    print('Выберите уровень сложности: "простой" - введите 0, "сложный" - введите 1')
    level = input()
    if is_valid(level) == False:
        print('!!!Введен некорректный тип данных!!!')
        print('Выберите уровень сложности: "простой" - введите 0, "сложный" - введите 1')
        level = input()
    else:
        level = int(level)
    if level == 0:
        game_light()
    else: game_hard()
    sleep(1)
    print('Повторим? Введите 1 - если да, и 0 - если нет.')
    n = input()
    while is_valid(n) == False:
        print('А, может быть, все-таки введем целое число?')
        n = input()
    n = int(n)

sleep(1)
print('Всего доброго!')