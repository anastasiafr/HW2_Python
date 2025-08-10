def month_to_season(month):
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return None


def month_name(month):
    names = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь"
    }
    return names.get(month, "некорректный месяц")


try:
    user_input = int(input("Введите номер месяца (1–12): "))
    season = month_to_season(user_input)
    name = month_name(user_input)

    if season:
        print(f"{name} — это {season}")
    else:
        print("Ошибка: номер месяца должен быть от 1 до 12")
except ValueError:
    print("Ошибка: введите целое число")
