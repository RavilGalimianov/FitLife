# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_IN_LITER = 1000


user_name = input("Здравствуйте, Введите Ваше Имя:")

# проверка на ошибку ввода пользователя строки вместо числа
while True:
    try:
        user_age = int(input("Введите Ваш возраст:"))
        break
    except ValueError:
        print("Введите пожалуйста число!")

# проверка на ошибку ввода пользователя строки вместо числа
while True:
    try:
        user_weight = float(input("Введите Ваш вес(в кг):"))
        break
    except ValueError:
        print("Введите пожалуйста число!")

# проверка на ошибку ввода пользователя строки вместо числа
while True:
    try:
        promt = "Введите Ваш рост(в метрах, например, 1.75):"
        user_height = float(input(promt))
        break
    except ValueError:
        print("Введите пожалуйста число!")

# расчёт индекса массы тела
bmi = round((user_weight / (user_height**2)), 1)

# расчёт рекомендуемой нормы воды
water_mliters = user_weight * WATER_PER_KG
water_liters = water_mliters / ML_IN_LITER


print(
    f"Отчет для пользователя: {user_name.capitalize()} ({user_age} л.)\n"
    f"Твой Индекс Массы Тела:{bmi}\n"
    f"Рекомендуемая норма воды: {water_liters:.1f} л. в день\n\n"
    f"Расчет окончен. Будьте здоровы!"
)
