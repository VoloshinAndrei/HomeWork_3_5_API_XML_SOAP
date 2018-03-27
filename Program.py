# Домашнее задание к лекции 3.5 «Работа с API для получения курсов валют, xml/soap»
# Используя сервисы http://www.webservicex.net/ и http://fx.currencysystem.com/webservices/CurrencyServer4.asmx
# (для валют), написать функции, которые на вход примут данные из соответствующих файлов (находятся на GitHub)
# и посчитают результат. Результат выводить в консоль.
# В качестве параметра функция должна принимать путь к файлу с данными.
#
# Задача №1
# Дано: семь значений температур по Фаренгейту в файле temps.txt. Необходимо вывести среднюю за неделю арифметическую
# температуру по Цельсию.
#
# Задача №2
# Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут и выписывать цены на перелеты.
# Даны цены на билеты в местных валютах (файл currencies.txt). Формат данных в файле:
#
# <откуда куда>: <стоимость билета> <код валюты>
# Пример:
# MOSCOW-LONDON: 120 EUR
# Посчитайте, сколько вы потратите на путешествие денег в рублях (без копеек, округлить в большую сторону).
#
# Задача №3
# Дано: длина пути в милях, название пути (файл travel.txt) в формате:
#
# <название пути>: <длина в пути> <мера расстояния>
# Пример:
# MOSCOW-LONDON: 1,553.86 mi
# Необходимо посчитать суммарное расстояние пути в километрах с точностью до сотых.

import osa


def task1(filename):
    sum = 0
    n = 0
    URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.client.Client(URL)
    with open(filename, encoding='utf-8') as f:
        for line in f:
            a = int(line.strip().split(' ')[0])
            sum += client.service.ConvertTemp(Temperature=a, FromUnit='degreeCelsius', ToUnit='degreeFahrenheit')
            n += 1
    print('Средняя за неделю арифметическая температура по Цельсию:', sum/n)


def task2(filename):
    URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client = osa.client.Client(URL)
    sum = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            a = int(line.strip().split(' ')[1])
            b = line.strip().split(' ')[2]
            sum += client.service.ConvertToNum(toCurrency='RUB', fromCurrency=b, amount=a, rounding=True)
    print('Потратите на путешествие денег в рублях :', round(sum, 0))


def task3(filename):
    URL = 'http://www.webservicex.net/ConvertSpeed.asmx?WSDL'
    client = osa.client.Client(URL)
    sum = 0.0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            str = line.strip().split(' ')[1]
            a = float(str.replace(',',''))
            sum += client.service.ConvertSpeed(speed=a, FromUnit='milesPerhour', ToUnit='kilometersPerhour')
    print('Суммарное расстояние пути в километрах с точностью до сотых:', round(sum, 2))


task1('temps.txt')
task2('currencies.txt')
task3('travel.txt')
