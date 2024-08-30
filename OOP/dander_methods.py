# Магические методы
'''
Магические методы (dander methods) - специальные методы которые вызываются сами по себе 
без явного вызова. Отличительная особенность  синтаксисе __method__
Популярные магические методы:
    __init__ - конструктор
    __new__ - конструктор
    __del__ - деструктор


# Операции представления
    __str__ - представление в удобночитаемом виде для разработчиков
    __repr__ - представление в машинном виде для разработчика


# Арифметические операции
    __add__(self,other) +
    __sub__(self,other) -
    __mul__(self.other) *
    __div__(self,other) /

# Операции сравнения
    __eq__(self,other) ==
    __lt__(self,other) <
    __gt__(self,other) >
    __le__(self,other) <=
    __ge__(self,other) >=
'''
# class Person:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
#     def __add__(self, other):
#         if self.age < 0 or other.age < 0:
#             raise Exception('Вы ввели отрицательный возраст')
#         else:
#             return self.age + other.age
#     def __mul__(self, other):
#
#         return self.age * other
#
#     def __lt__(self,other):
#         return self.age > other.age
#
#     # def __str__(self):
#     #     return f"{self.name} {self.last_name}{self.age}"
#
#
# akjol = Person('akjol', 'cool', 14)
# torokul = Person('Torokul', 'Zhanyshbekov', 23)
#
#
# # print(akjol * 2)
# # print(torokul * 2)
#
# # print(akjol + torokul)
# print(torokul > akjol)




# info = ['Торокул Жанышбеков, 14 лет, '
#         'учится языку Python, '
#         'любит поиграть в футбол']
#
# inp1 = input('Введите свое имя: ').strip()
# inp2 = input('Введите свою фамилию: ').strip()
# secret = input('Введите секрет: ').strip()
#
# if inp1 == 'Торокул' and inp2 == 'Жанышбеков' and secret == 'мой папа самый лучший':
#     print(f'Добро пожаловать, мистер {inp1} {inp2}!')
# else:
#     print(f'{inp1} {inp2}, вы не обладатель этого MacBook.')
#
# prodoljenie = input(f'Хотите ли вы посмотреть информацию о {inp1}? (Введите "Да" или "Нет"): ').strip().capitalize()
# if prodoljenie == 'Да':
#     print(f'Информация о {inp1}: {info}')
# elif prodoljenie == 'Нет':
#     print('Ок, я вас понял, до свидания.')
# else:
#     print(f'Вы ввели неверный ответ. Ожидалось "Да" или "Нет", а вы ввели: {prodoljenie}')



while True:
    n1 = float(input('Введите первое число: '))
    n2 = float(input('Введите второе число: '))
    operasia = input('Выберите операцию: +,  -,  *,  /  //,   **  ')
    if operasia == '+':
        print(n1 + n2)
    elif operasia == '-':
        print(n1 - n2)
    elif operasia == '*':
        print(n1 * n2)
    elif operasia == '/':
        print(n1 / n2)
    elif operasia == '//':
        print(n1 // n2)
    elif operasia == '**':
        print(n1 ** n2)
    else:
        print('Вы ввели не правильную операцию, из перечисленных!')
        break
    zavershenie = input('Хотите ли вы продолжить? (Введите "Да" или "Нет"): ').strip().capitalize()
    if zavershenie == 'Да':
        print('Я вас понял мы продолжаем!')
        continue
    elif zavershenie == 'Нет':
        break
    else:
        print(f'Вы ввели "{zavershenie}", а надо было ввести: "Да" или "Нет"!')
        break