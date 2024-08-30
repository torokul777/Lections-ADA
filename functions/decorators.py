'=========================Дикораторы==================='
# функция высшего порядка - функция которая принимает в аргументы другую функцию
#создает внутри себя функцию, возврашает функцию
# Декотатор - функция высшего порядка которая нужна чтобы расширять функционал
#функции не изменяя ее (функция обертка)

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         from datetime import datetime
#         print('start:',datetime.now())
#         func(*args,**kwargs)
#         print('finish:',datetime.now())
#     return wrapper
# @decorator
# def hello():
#     print('hello world')

# hello()

# @decorator
# def my_sqrt(x):
#     print(x ** 0.5)

# def func_start_time(func):
#     def wrapper(*args,**kwargs):
#         from datetime import datetime
#         now = datetime.now()
#         correct_format = now.strftime('%d.%m.%Y %H:%M')
#         print('функция запущена', correct_format)
#         func(*args,**kwargs)
#     return wrapper
# @func_start_time
# def func1():
#     print('hello')
# func1()

# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args,**kwargs):
#             for i in range(num):
#                 func(*args,**kwargs)
#         return wrapper
#     return inner_decorator
# @decorator(12)
# def hello():
#     print('hello world')
# hello()


# import requests
# from time import time

# def benchmark(func):
#     def wrapper(*args,**kwargs):
#         start = time()
#         func()
#         end = time()
#         time_exec = end - start
#         print(f"Время выполнения {time_exec} сукунд")
#     return wrapper
# @benchmark

# def fetch_webpage() -> None:
#     webpage = requests.get('https://google.com')

# fetch_webpage()
class RadioMixin:
    def play_music(self, song_name):
        return f'Название: {song_name}'

class Auto(RadioMixin):
    def __init__(self, model):
        self.model = model

    def info(self):
        return f'Модель машины: {self.model}'

class Boat(RadioMixin):
    def __init__(self, model):
        self.model = model

    def info(self):
        return f'Модель корабля: {self.model}'

class Amphibian(RadioMixin):
    def __init__(self, type):
        self.type = type

    def info(self):
        return f'Тип амфибии: {self.type}'


auto = Auto('BMW M5')
boat = Boat('Yamaha')
amphibian = Amphibian('Gibbs Quadski')


print(auto.info())         
print(boat.info())         
print(amphibian.info())   


print(auto.play_music('Despacito'))     
print(boat.play_music('Blinding Lights'))
print(amphibian.play_music('Shape of You'))
