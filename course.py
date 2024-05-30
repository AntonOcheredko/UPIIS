

def rub_to_usd(rubles, rate):

    if rubles < 0:
        raise ValueError("Сумма в рублях не может быть отрицательной.")
    if rate <= 0:
        raise ValueError("Курс доллара должен быть положительным числом.")
    return rubles / rate


def usd_to_rub(dollars, rate):

    if dollars < 0:
        raise ValueError("Сумма в долларах не может быть отрицательной.")
    if rate <= 0:
        raise ValueError("Курс доллара должен быть положительным числом.")
    return dollars * rate


def get_user_input():

    try:
        amount = float(input("Введите сумму: "))
        rate = float(input("Введите курс доллара: "))
        return amount, rate
    except ValueError:
        print("Ошибка: введите числовые значения.")
        return get_user_input()


def main():

    print("Выберите тип конвертации:")
    print("1. Рубли в Доллары")
    print("2. Доллары в Рубли")

    choice = input("Ваш выбор (1 или 2): ")

    if choice == "1":
        rubles, rate = get_user_input()
        try:
            dollars = rub_to_usd(rubles, rate)
            print(f"{rubles} руб. = {dollars:.2f} USD")
        except ValueError as e:
            print(f"Ошибка: {e}")
    elif choice == "2":
        dollars, rate = get_user_input()
        try:
            rubles = usd_to_rub(dollars, rate)
            print(f"{dollars} USD = {rubles:.2f} руб.")
        except ValueError as e:
            print(f"Ошибка: {e}")
    else:
        print("Неправильный выбор. Попробуйте снова.")
        main()


if __name__ == "__main__":
    main()
