import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Функція для отримання даних про курс валют за конкретну дату
def get_exchange_rate(date, currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item['cc'] == currency_code:
                return item['rate']
    return None

# Визначення дат за останній тиждень
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

dates = [(start_date + timedelta(days=i)).strftime("%Y%m%d") for i in range(8)]

# Код валюти для аналізу (наприклад, USD)
currency_code = "USD"

# Збирання даних
rates = []
for date in dates:
    rate = get_exchange_rate(date, currency_code)
    if rate is not None:
        rates.append((date, rate))

# Перетворення дат у формат для графіка
dates = [datetime.strptime(date, "%Y%m%d").strftime("%d-%m-%Y") for date, _ in rates]
values = [rate for _, rate in rates]

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(dates, values, marker='o', label=f"{currency_code} to UAH")
plt.title(f"Зміна курсу {currency_code} до UAH за останній тиждень")
plt.xlabel("Дата")
plt.ylabel("Курс")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

