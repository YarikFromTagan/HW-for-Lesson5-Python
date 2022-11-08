# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход
# можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import os
import random
os.system('cls')

def game_selection():
    valid = False
    while not valid:
        game = input('Human vs Human --> введите 1\nHuman vs Bot --> введите 2\n\n--> ')
        try:
            game = int(game)
        except:
            print('\n!!! Нужно ввести число !!!')
            continue
        if game == 1:
            human_human(rest)
            valid = True
        elif game == 2:
            human_bot(rest)
            valid = True
        else: print('\nНужно ввести либо 1, либо 2\n')

def rand_step(min, max ):
    rnd_stp = random.randint(min, max)
    return rnd_stp

def draw_human_human():
    os.system('cls')
    print('Сейчас мы узнаем, кто сделает первый ход\nДля этого бросим два игральных кубика\n')
    valid = False
    while not valid:
        input('Игрок 1, для броска своих кубиков нажмите Enter')
        cube_1 = rand_step(1, 6)
        cube_2 = rand_step(1, 6)
        resut_player_1 = cube_1 + cube_2
        print(f'\nУ Вас выпало [{cube_1} : {cube_2}] итого: {resut_player_1}\n')
        input('Игрок 2, для броска своих кубиков нажмите Enter')
        cube_3 = rand_step(1, 6)
        cube_4 = rand_step(1, 6)
        resut_player_2 = cube_3 + cube_4
        print(f'\nУ Вас выпало [{cube_3} : {cube_4}] итого: {resut_player_2}\n')
        if resut_player_1 > resut_player_2:
            print('По результатам жеребьёвки Игрок 1 ходит первым!!!\n')
            input('Нажмите Enter')
            os.system('cls')
            valid = True
            return 1
        elif resut_player_1 < resut_player_2:
            print('По результатам жеребьёвки Игрок 2 ходит первым\n')
            input('Нажмите Enter')
            os.system('cls')
            valid = True
            return -1
        else:
            input('Упс... Поровну!\nТогда начнём сначала\n\nНажмите Enter')
            os.system('cls')

def draw_human_bot():
    os.system('cls')
    print('Сейчас мы узнаем, кто сделает первый ход\nДля этого бросим два игральных кубика\n')
    valid = False
    while not valid:
        input('Для броска своих кубиков нажмите Enter')
        cube_1 = rand_step(1, 6)
        cube_2 = rand_step(1, 6)
        resut_player = cube_1 + cube_2
        print(f'\nУ Вас выпало [{cube_1} : {cube_2}] итого: {resut_player}\n')
        input('Теперь мой бросок.\nНажмите пожалуйста Enter')
        cube_3 = rand_step(1, 6)
        cube_4 = rand_step(1, 6)
        resut_bot = cube_3 + cube_4
        print(f'\nА у меня выпало [{cube_3} : {cube_4}] итого: {resut_bot}\n')
        if resut_player > resut_bot:
            print('Поздравляю. Вы ходите первым!!!\n')
            input('Нажмите Enter')
            os.system('cls')
            valid = True
            return -1
        elif resut_player < resut_bot:
            print('Первый ход за мной\n')
            input('Нажмите Enter')
            os.system('cls')
            valid = True
            return 1
        else:
            input('Упс... Поровну!\nТогда начнём сначала\n\nНажмите Enter')
            os.system('cls')

def human_human(rest):
    start_rest = rest
    move = draw_human_human()

    while rest > 0:
        print(f'На кону осталось {rest} конфет из {start_rest}\n')
        if move == 1:
            valid = False
            while not valid:
                one_choice = input('Ход 1-го игрока:\nМожно взять от 1-й до 28-ми конфет, но не больше остатка\nСколько конфет Вы берёте? --> ')
                print('--------------------------')
                try:
                    one_choice = int(one_choice)
                except:
                    print('\n!!! Нужно ввести число !!!')
                    continue
                if one_choice >= 1 and one_choice <= 28 and one_choice <= rest:
                    rest -= one_choice
                    valid = True
                    os.system('cls')
                else:
                    print('Напоминаю!!!')
            
        else:
            valid = False
            while not valid:
                two_choice = input('Ход 2-го игрока:\nМожно взять от 1-й до 28-ми конфет, но не больше остатка\nСколько конфет Вы берёте? --> ')
                print('--------------------------')
                try:
                    two_choice = int(two_choice)
                except:
                    print('\n!!! Нужно ввести число !!!')
                    continue
                if two_choice >= 1 and two_choice <= 28 and two_choice <= rest:
                    rest -= two_choice
                    valid = True
                    os.system('cls')
                else:
                    print('Напоминаю!!!')
        move *= -1

    if move == -1: print("\nПобедил 1-й игрок!!!!\n")
    else: print("\nПобедил 2-й игрок!!!!\n")

def human_bot(rest):
    start_rest = rest
    move = draw_human_bot()

    while rest > 0:
        print(f'На кону осталось {rest} конфет из {start_rest}\n')
        if move == 1:
            i = 0
            while i < rest - 29:
                i += 29
            if rest%29 == 0:
                comp_take = rand_step(1, 28)
            else:
                comp_take = rest - i
            rest -= comp_take
            print(f'Мой ход, и я беру {comp_take}\n\n--------------------------\n')
            
        else:
            valid = False
            while not valid:
                my_choice = input('Ваш ход:\nМожно взять от 1-й до 28-ми конфет\nСколько конфет Вы берёте? --> ')
                print('--------------------------')
                try:
                    my_choice = int(my_choice)
                except:
                    print('\n!!! Нужно ввести число !!!')
                    continue
                if my_choice >= 1 and my_choice <= 28:
                    rest -= my_choice
                    valid = True
                    os.system('cls')
                else:
                    print('Напоминаю!!!')
        move *= -1

    if move == -1: print("\nЯ победил!!!!\n")
    else: print("\nВы победили!!!!\n")

rest = 120 # Количество конфет на кону
print('Приветствую Вас на игре с конфетами!!!\n\nКак будем играть?')
game_selection()





