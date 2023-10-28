import requests
import time
from pystyle import Write, Colors

def check_website_speed(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return response.status_code, elapsed_time
    except requests.exceptions.RequestException as e:
        return None, str(e)

if __name__ == "__main__":
    website_url = Write.Input("Введите URL сайта для проверки скорости загрузки: ", Colors.purple_to_blue, interval=0)
    status_code, elapsed_time = check_website_speed(website_url)

    if status_code:
        Write.Print(f"Статус код: {status_code}", Colors.red_to_yellow, interval=0)
        # print(f"Скорость загрузки сайта {website_url}: {elapsed_time:.2f} секунд")
        Write.Print(f"Скорость загрузки сайта: ", Colors.purple_to_blue, interval=0)
        Write.Print(f"{elapsed_time:.2f} секунд", Colors.green_to_blue, interval=0)

    else:
        Write.Print(f"Ошибка: {elapsed_time}", Colors.red_to_yellow, interval=0)
