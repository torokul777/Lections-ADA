'=========================================OOP-======================================='
# OOP - обьектно орентированнные программирование(Парадигма)

# class Person:
#     # Переменные внутри класса (обьекта) - аттрибуты класса
#     arms = 2
#     legs = 2

#     def __init__(self, name, age):
#         #__init__ - метод который будет добавлять в обьект те аттрибуты которое отличается у разных обьектов
#         # self - ссылка на обьект который только что создался аттрибуты экземпляра класса
#         self.name = name
#         self.age = age

#     def walk(self):
#         print(f'{self.name} ходит')
#     def happy_birthday(self):
#         print(f'{self.name}, happy birthday')
#         self.age +=1
#         return 'Подарок'


# obj1 = Person('Torokul',14)
# print(f'name:{obj1.name}')
# print(f'arms:{obj1.age}')
# print(f'arms:{obj1.arms}')
# print(f'legs:{obj1.legs}')
# obj1.walk()
# obj1.happy_birthday()
# print(f'тебе исполнилось:{obj1.age}!!!')
# '========================================Обьекты класса=========================='
# # обьекты, экземпляр, instance класса - обьект, созданный по шаблонну класса (он перенимает все аттрибуты и методы класса)

# '==========================================Аттрибуты и методы========================'
# # Аттрибуты - переменные
# # методы - функции

# class A:
#     var1 = 'Переменная класса'

#     def __init__(self) -> None:
#         self.var2 = 'Переменная обьекта'

# print(dir(A))
# # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']
# # macs-MacBook-Air:LLECTIONS ADA mac$ \
# obj2 = A()

# class Calculator:
#     def add(self,a,b):
#         'Функция сложение'
#         return a + b
    
#     def sqrt(self,num,ndigits=2):
#         'Функция нахождения квадртаного корня числа с округлением'
#         import math 
#         sqrt_num = math.sqrt(num)
#         return round(sqrt_num,ndigits)
    
#     def percent(self, total, percent):
#         'Функция нахождение процента от числа'
#         return (total * percent) / 100

#     def super_func(self,string):
#         'Функция которая выполняет вычисление в строке'
#         return eval(string)

# calc = Calculator()
# print(calc.add(10,10))
# print(calc.sqrt(25))
# print(calc.percent(1000,10))
# print(calc.super_func('1010'))

class Sniper:
    health = 100

    def __init__(self,name) -> None:
        self.name = name

    def shoot(self,sniper2):
        sniper2.health -=20
        print(f'Атаковал {self}')
        print(f'У {sniper2} осталось {sniper2.health}')
    def __str__(self) -> str:
        #когда нужен обьект 
        # когда оборачиваем в строку
        return self.name


sniper1 = Sniper('Torokul')
sniper2 = Sniper('Marat')

import random
while sniper1.health and sniper2.health:
    choice = random.randint(1 , 2)
    if choice == 1:
        sniper1.shoot(sniper2)
    else:
        sniper2.shoot(sniper1)
if sniper1.health:
    print(f'{sniper1} унизил {sniper2}')
else:
    print(f'{sniper2} унизил {sniper1}')
