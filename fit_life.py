# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_IN_LITER = 1000


def main():
    ""Функция для расчета данных пользователя""
    user_name = input("Здравствуйте, Введите Ваше Имя:")
    formatted_name = user_name.capitalize()

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
            user_weight_input = input("Введите Ваш вес(в кг):")
            user_weight = float(user_weight_input.replace(",", "."))
            break
        except ValueError:
            print("Введите пожалуйста число!")

    # проверка на ошибку ввода пользователя строки вместо числа
    while True:
        try:
            promt = "Введите Ваш рост(в метрах, например, 1.75):"
            user_height = float(input(promt).replace(",", "."))
            break
        except ValueError:
            print("Введите пожалуйста число!")

    # расчёт индекса массы тела
    bmi = round((user_weight / (user_height**2)), 1)

    # расчёт рекомендуемой нормы воды
    water_mliters = user_weight * WATER_PER_KG
    water_liters = water_mliters / ML_IN_LITER
    return (
        formatted_name,
        user_age,
        user_weight,
        user_height,
        bmi,
        water_liters
    )


if __name__ == "__main__":
    (
        formatted_name,
        user_age,
        user_weight,
        user_height,
        bmi,
        water_liters
    ) = main()

    print(
        f"Отчет для пользователя: {formatted_name} ({user_age} л.)\n"
        f"Твой Индекс Массы Тела:{bmi}\n"
        f"Рекомендуемая норма воды: {water_liters:.1f} л. в день\n\n"
        f"Расчет окончен. Будьте здоровы!",
    )
