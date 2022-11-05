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

def rand_step(min, max ):
    rnd_stp = random.randint(min, max)
    return rnd_stp

def draw_h_b():
    os.system('cls')
    print('Сейчас узнаем, кто сделает первый ход\n')
    input('Для броска кубиков нажмите Enter')
    cube_1 = rand_step(1, 6)
    cube_2 = rand_step(1, 6)
    resut_player = cube_1 + cube_2
    print(f'У Вас выпало [{cube_1} : {cube_2}] итого: {resut_player}\n')
    input('Теперь мой бросок. Нажмите пожалуйста Enter')
    cube_3 = rand_step(1, 6)
    cube_4 = rand_step(1, 6)
    resut_bot = cube_3 + cube_4
    print(f'А у меня выпало [{cube_3} : {cube_4}] итого: {resut_bot}\n')
    if resut_player > resut_bot:
        print('Поздравляю. Вы ходите первым!!!\n')
        input('Нажмите Enter')
        os.system('cls')
        return -1
    else:
        print('Первый ход за мной\n')
        input('Нажмите Enter')
        os.system('cls')
        return 1



def hum_hum():
    print('пока не готово')

def hum_bot(rest):
    start_rest = rest
    move = draw_h_b()

    while rest > 0:
        print(f'\nНа кону {rest} конфет из {start_rest}')
        print('Можно взять от 1-й до 28-ми конфет\n')
        if move == 1:
            i = 0
            while i < rest - 29:
                i += 29
            if rest%29 == 0:
                comp_take = rand_step(1, 28)
            else:
                comp_take = rest - i
            rest -= comp_take
            #os.system('cls')
            print(f'Мой ход: Я беру {comp_take} конфет')
            #print(f'На кону {rest} конфет из {start_rest}\n')
        else:
            #print(f'На кону {rest} конфет из {start_rest}\n')
            my_choice = int(input('Ваш ход: \nСколько конфет Вы берёте? '))
            rest -= my_choice
            #print(f'\nПосле Вашего хода осталось {rest} конфет\n')
        move *= -1

    if move == -1: print("\nЯ победил!!!!\n")
    else: print("\nВы победили!!!!\n")


rest = 120
print('Приветствую Вас на игре с конфетами!!!\n\nКак будем играть?')
game = input('Human vs Human --> введите 1\nHuman vs Bot --> введите 2\n\n--> ')

if int(game) == 1: hum_hum()
elif int(game) == 2: hum_bot(rest)
else: print('\nОпределитесь с игрой и начните заново!\n')




