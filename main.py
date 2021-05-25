import random


#  Функция, которая закрывает двери
def close(x):
    x[random.randint(0, 2)] = True


#  Функция, меняющая двери
def change(x, c):
    new_door = x[c]
    #  Дверь меняется на оставшуюся, если выбрана ложная, то выбирается верная и наоборот
    new_door = False if new_door else True
    return new_door


#  Выбор случайной двери
def choose_random_door(x, c):
    x.remove(True)
    x[random.randint(0, 1)] = True
    new_door = True if x[random.randint(0, 1)] else False
    return new_door


#  Подсчёт вариантов выигрыша
win_1 = 0
win_2 = 0
win_3 = 0
for i in range(1000):
    doors = [False, False, False]
    random.seed(version=2)
    close(doors)
    choose = random.randint(0, 1)
    #  Если выбор не меняется
    win_1 = win_1 + 1 if doors[choose] else win_1 + 0
    #  Если выбор меняется
    win_2 = win_2 + 1 if change(doors, choose) else win_2 + 0
    #  Если меняются вещи за дверями
    win_3 = win_3 + 1 if choose_random_door(doors, choose) else win_3 + 0


win_1_chance = win_1*100/(i+1)
win_2_chance = win_2*100/(i+1)
win_3_chance = win_3*100/(i+1)

print('Если выбор двери не изменялся, шанс победы равен ', win_1_chance, "%")
print('Если выбор двери изменялся ', win_2_chance, "%")
print('Если менялись предметы за дверью, и менялся выбор двери ', win_3_chance, "%")

