import config
import menu

# 3 задание

config.init_config()
wigth = config.get_value('screenWigth')
height = config.get_value('screenHeight')
print(f"Разрешение экрана: {wigth}x{height}")
value = int(input("Введите значение громкости в %: "))
config.set_value('volume', value)


# # 4 задание, 1 алгоритм
# # поменять x и y с помощью 3 переменной

variable = config.config['screenWigth']
config.config['screenWigth'] = config.config['screenHeight']
config.config['screenHeight'] = variable
print(f"Разрешение экрана(1 алгоритм): {config.config['screenWigth']}x{config.config['screenHeight']}")

# # 2 алгоритм
# # сохранить переменные в список, использовать reverse

parameters = list(config.config.values())
parameters.pop()
parameters.reverse()
config.config['screenWigth'] = parameters[1]
config.config['screenHeight'] = parameters[0]
print(f"Разрешение экрана(2 алгоритм): {config.config['screenWigth']}x{config.config['screenHeight']}")

# # 3 алгоритм
# # через XOR

a = config.config['screenWigth']
b = config.config['screenHeight']
a ^= b
b ^= a
a ^= b
config.config['screenWigth'] = a
config.config['screenHeight'] = b
print(f"Разрешение экрана(3 алгоритм): {config.config['screenWigth']}x{config.config['screenHeight']}")

# # 4 алгоритм
# # через сумму

a = config.config['screenWigth']
b = config.config['screenHeight']
a = a + b
b = a - b
a = a - b
config.config['screenWigth'] = a
config.config['screenHeight'] = b
print(f"Разрешение экрана(4 алгоритм): {config.config['screenWigth']}x{config.config['screenHeight']}")
config.save_config()

# # 5 задание

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