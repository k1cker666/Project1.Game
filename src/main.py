import config
import menu

# 3 задание
cfg = config.init_config()
print(f"Разрешение экрана: {cfg['screenWigth']}x{cfg['screenHeight']}")

# ввод громкости, в формулировке задания не понял 3 пункт(зачем save если можно сразу через set)
# value = int(input("Введите значение громкости в %: "))
# config.set_value('volume', value)

# 4 задание, 1 алгоритм
# поменять x и y с помощью 3 переменной

thrd_variable = cfg['screenWigth']
cfg['screenWigth'] = cfg['screenHeight']
cfg['screenHeight'] = thrd_variable
print(f"Разрешение экрана(1 алгоритм): {cfg['screenWigth']}x{cfg['screenHeight']}")
config.save_config(cfg)

# 2 алгоритм
# сохранить переменные в список, использовать reverse

parameters = list(cfg.values())
parameters.pop()
parameters.reverse()
cfg['screenWigth'] = parameters[1]
cfg['screenHeight'] = parameters[0]
print(f"Разрешение экрана(2 алгоритм): {cfg['screenWigth']}x{cfg['screenHeight']}")
config.save_config(cfg)

# 3 алгоритм
# через XOR

variable_a = cfg['screenWigth']
variable_b = cfg['screenHeight']
a = variable_b ^ variable_a
cfg['screenWigth'] = a ^ variable_a
b = variable_a ^ variable_b
cfg['screenHeight'] = b ^ variable_b
print(f"Разрешение экрана(3 алгоритм): {cfg['screenWigth']}x{cfg['screenHeight']}")
config.save_config(cfg)

# 4 алгоритм
# через сумму

a = cfg['screenWigth']
b = cfg['screenHeight']
a = a + b
b = a - b
a = a - b
cfg['screenWigth'] = a
cfg['screenHeight'] = b
print(f"Разрешение экрана(4 алгоритм): {cfg['screenWigth']}x{cfg['screenHeight']}")
config.save_config(cfg)

# 5 задание

menu.print_menu()

while True:
    try:
        user_answer = int(input("Ваше действие: "))
        if user_answer == 3:
            print("Ну пока!")
            break
        else:
            print("Лох, ты не угадал!") # =)
    except ValueError:
        print("Пиши только цифры!")