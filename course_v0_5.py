
def rub_to_usd(rubles, rate):

    return rubles / rate

def usd_to_rub(dollars, rate):

    return dollars * rate

# Примеры использования
rubles = 1000
rate = 95.0

print(f"{rubles} руб. = {rub_to_usd(rubles, rate):.2f} USD")
print(f"100 USD = {usd_to_rub(100, rate):.2f} руб.")
