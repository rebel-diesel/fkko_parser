from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Подключение Brave и ChromeDriver
service = Service("driver/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options.add_argument("--headless")  # можно включить, когда отладим

driver = webdriver.Chrome(service=service, options=options)

all_kod = []
all_name = []

# Парсинг всех 38 страниц
for page in range(1, 39):
    if page == 1:
        url = "http://kod-fkko.ru/spisok-othodov/"
    else:
        url = f"http://kod-fkko.ru/spisok-othodov/page/{page}/"

    print(f"Парсинг страницы {page}...")
    driver.get(url)

    # Получаем коды и наименования
    kod_elements = driver.find_elements(By.CLASS_NAME, "my_col1")
    name_elements = driver.find_elements(By.CLASS_NAME, "my_col2")

    for kod, name in zip(kod_elements, name_elements):
        k = kod.text.strip()
        n = name.text.strip()
        if k and n:
            all_kod.append(k)
            all_name.append(n)

# Запись результата в текстовый файл
with open("fkko_full.txt", "w", encoding="utf-8") as f:
    for k, n in zip(all_kod, all_name):
        f.write(f"{k} - {n}\n")

driver.quit()
print("Готово. Сохранено в fkko_full.txt.")
