'=========================Встроенные функциии================'
# map,filter,reduce,zip,enumerate

# zip - соединяет несколько посследовательностей (получаем генератор в котором элементы - tuple)

# list1 = [1,2,3,4,5]
# list2 = ['a','b','c']
# list3 = [10.5,10.6,100.54]

# zipped = zip(list1,list2,list3)
# for element in zipped:
#     print(element)
# (1, 'a', 10.5)
# (2, 'b', 10.6)
# (3, 'c', 100.54)

# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# dict_ = dict(zip(list1,list2))
# print(dict_)
#{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

'====================Enumerate=================='
#enumerate - нумерует посследовательность(по дефолту с 0) (также получаем генератор)
# enumerated = enumerate('Hello')
# #print(enumerated) <enumerate object at 0x1025985e0>

# for el in enumerated:
#     print(el)
# (0, 'H')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

# string = 'hello world'
# print(list(enumerate(string)))
#[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')]

'========================Map=================='
# map - принимает функцию и последовательность (записыввает в новую 
# посследовательность результат функции в которую
#  передаются элементы посследовательности) 

# list_ = ['1','2','3','4','5']
# mapped_list = list(map(int,list_))
# print(mapped_list)
# [1, 2, 3, 4, 5]

# string = 'hello world'
# res = ''.join(map(lambda x: x.upper(),string))
# print(res)
# # HELLO WORLD

# list1 = [1,2,3,4,5]
# list2 = list(map(lambda x: x**2,list1))
# print(list2)
# [1, 4, 9, 16, 25]

# list1 = [1,2,3,4,5]
# def to_2_degree(x):
#     return x**2
# print(list(map(to_2_degree,list1)))
# [1, 4, 9, 16, 25]

'=======================Filter================'
# filter - возвращает генератор с элементами в прошедшими в фильтр(какое то условие),
# принимает в себя функцию и посследовательность
# list1 = [1,0,-2,-3,-4,5,10]
# filterred = list(filter(lambda x: x > 0,list1))
# print(filterred) #[1, 5, 10]

# users =[
#     {'name':'nikita', 'age': 12},
#     {'name':'nastya', 'age': 20},
#     {'name':'artem' , 'age': 19}

# ]
# # оставить пользователей которые старше 18
# res = list(filter(lambda user: user['age'] > 18, users))
# print(res)

# filtered = filter(lambda user: user['age'] < 15, users)
# res = list(map(lambda x: x['name'],filtered))
# print(res) #'[nikita']
'=======================Reduce============'
from functools import reduce
# reduce - принимает функцию и посследовательность, возврашает 1 результат
# (передаваемая функция должна принимать 2 агрумента)

# list_ = [1,2,3,4,5]
# res = reduce(lambda x, y:x*y,list_)
# print(res) #120

# string = 'hello'
# res = reduce(lambda x,y:x+'*'+y,string)
# print(res) #h*e*l*l*o
# # x = 'h', y='e'-> h*e 



# string = 'hello world'
# print(reduce(lambda x,y:string.replace(x,y),string))
# # heddo wordd

# list1 = [1,2,3,4,5,34,234,23]
# res = reduce(lambda x,y: x if x<y else y,list1)
# print(res)

users =[
    {'name':'nikita', 'age': 12},
    {'name':'nastya', 'age': 20},
    {'name':'artem' , 'age': 19}
]

# def min_dict(dict1,dict2):
#     if dict1['age'] < dict2['age']:
#         return dict1
#     return dict2
# res = reduce(min_dict, users)
# print(res)    
# {'name': 'nikita', 'age': 12}

# res = reduce(lambda x,y:x if x['age']<y['age'] else y,users)
# print(res) # {'name': 'nikita', 'age': 12}

# 1) напишите программу которая суммирует все элементы в списки используя какую т о встроенную функцию
# new_list = reduce(lambda x,y: x + y,list1)
# print(new_list) #68108

#2)напишите программу которая возваодит в квадрат каждый элемент списка
# res = list(map(lambda x: x**2,list1))
# print(res) #

#list1 = [1,12000,134,12431,43542]
# res = list(filter(lambda x: x % 2 == 0,list1))
# print(res)#[12000, 134, 43542]

# напишите программу которая отбирает слова длина которых больше 7 из исходного списка

# list1 = ["inheritance", "solid", "polymorphism", "dry", "yagni"]
# res = list(filter(lambda word: len(word) > 7,list1))
# print(res)

# напишите прогрмамму которая считает кол-во четных и нечетных чисел в списке
# и выводит их кол-во в формате строки


# list1 = [1,2,3,4,5,6,7,8,9,10]

# list2 = len(list(filter(lambda x: x % 2 != 0,list1)))
# list3 = len(list(filter(lambda x: x % 2 == 0,list1)))
# result = F'четные:{list3}, нечетные:{list2}'
# print(result) 

# напишите программу которая находит самое длинное имя в списке
# list1 = ["Paul", "George", "Ringo", "John"]
# res = reduce(lambda x,y: x if len(x) > len(y) else y,list1)
# print(res)


# напишите программу которая меняет число на 'fizz ' если оно делится на 3 и на строку 'buzz' если не делится в диапозоне чисел от 1 до 50 включительно

# res = list(map(lambda x: 'fizz' if x % 3 == 0 else 'buzz',range(1,51)))
# print(res)

# напишите программу которая находит минимальное значение у элемента в списке
# list1 = [1,2,3,4,5,6,7,8,9]
# res = reduce(lambda x, y:x if x<y else y,list1)
# print(res)


# def krasivyi_god():
#     if n1 == 1987:
#         print(2013)
#     elif n1 == 2013:
#         print(2014)
# n1 = int(input())
# krasivyi_god()


# Доктор Брюс Беннер ненавидит своих врагов (сильнее, чем это делают другие). Как мы знаем, он с трудом общается, когда превращается в Халка. Поэтому он просит вас помочь ему с выражением своих чувств.

# Халк очень любит погружение, и его чувства крайне сложные. Они состоят из n уровней, первый из них — это ненависть, второй — любовь, третий снова ненависть и так далее...

# Например, для n = 1 чувства Халка выражаются как "I hate it", для n = 2 это уже "I hate that I love it", а для n = 3 — "I hate that I love that I hate it".

# Помогите Брюсу выразить свои чувства на n-м уровне погружения.

# Входные данные
# В единственной строке входных данных записано единственное целое число n (1 ≤ n ≤ 100) — количество уровней погружения.


# Выходные данные
# Выведите строку, описывающую чувства доктора Бреннера.

# def hulk(n):
#     chuvstvo = ''
#     for i in range(1, n+1):
#         if i == 1:
#             chuvstvo += "I hate"
#         elif i % 2 == 0:
#             chuvstvo += " that I love"
#         else:
#             chuvstvo += " that I hate"
    
#     chuvstvo += " it"
#     return chuvstvo

# n = int(input())
# print(hulk(n))
'=================homework======================'
'=================exercise1====================='
# Напишите программу, которая принимает строку "hello" 
# и выводит кортеж, содержащий индекс и соответствующий
#  символ для каждого символа строки, используя 
# встроенные функции
# def word():
#     for el in  enumerate('hello'):
#         print(el)
# word()

'=================exercise2====================='
# Напишите программу, которая принимает список чисел list1 =  [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
#  и выводит новый список, содержащий абсолютные значения
#  этих чисел.
# list1 =  [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# abs_ = [abs(num) for num in list1]
# print(abs_)

'=================exercise3====================='
# Напишите программу, которая принимает список 
# list1 = ["hello", 123] и выводит новый список,
# содержащий тип каждого элемента исходного списка.
# list1 = ["hello", 123]
# type_ = [type(x) for x in list1]
# print(type_)
'==================exercise 4================'
# Напишите программу, которая принимает список имен
# и выводит новый список, в котором к
#  каждому имени добавляется строка " Python", 
# если длина имени больше 5 символов, и строка " JavaScript", 
# если длина имени 5 символов или меньше.
#  (Используйте функцию map() и f строки для форматирования
#  и добавления к имени новых слов)
# def add_language(name):
#     if len(name) > 5:
#         return f"{name} Python"
#     else:
#         return f"{name} JavaScript"

# names = ["Alice", "Bob", "Charlie", "Eve", "Frank", "Grace", "Hank"]
# new_names = list(map(add_language, names))
# print(new_names)

'===================exercise 5=========='
# Напишите программу, которая принимает список строк
#  email_list = ["123hello@gmail.com", "123", "hello"] 
# и выводит новый список, в котором строка остается неизменной,
#  если она заканчивается на "@gmail.com", а если нет,
#  то заменяется на "Not valid email" (используйте map(),
#  и метод строк .endswith(), если что посмотрите в лекции
#  по строкам как он использовался)

# def email_(email):
#     if email.endswith("@gmail.com"):
#         return email
#     else:
#         return "Not valid email"
# email_list = ["123hello@gmail.com", "123", "hello", "test@yahoo.com"]

# validated_emails = list(map(email_, email_list))

# print(validated_emails)

'================exercise 6==========='
# Напишите программу, которая проверяет, является ли список list1 = ['a', 'n', 'n', 'a'] палиндромом, и выводит "YES", если это так, и "NO", если не
# list1 = ['a', 'n', 'n', 'a']
# palindrom = list1[::-1]
# if list1 == palindrom:
#     print('YES')
# else:
#     print('NO')
# print(list1)
