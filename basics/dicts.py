'==========================Словари=========================='
# dict - это изменяемый итерируемый неупорядочный неидндексируыемый тип данных
#  для зранения данных в паре{ключ : значение

# user = {
#     "name" : 'Torokul',
#     'city' : 'Bishkek',
#     'country' : " Kyrgyzstan",
# }
# print(user['name'])
# print(user['city'])
# print(user['country'])

# #Ключами в словаре могут быть только не изменяемые типы данных

# dict1 = { 'a' : 1, 'b' : 2, 'c' : 3, 'a' : 4}

# print(dict['a']) #4, если ключи одинаковые то сохранится только последнее значение
# # print(dict['d']) #KeyError: 'd'

# dict1 = {'a' : 1, 'b' : 2, 'c' : 3, 'a' : 4}
# # dict2 = dict( [ ('a', 1), ('b',2)])
# #print(dict2) 
# dict3 = dict(['ab','cd', 'ef']) #{'a': 'b', 'c': 'd', 'e': 'f'}
# print(dict3)

# dict4 = {}
# dict4['name'] = 'Torokul'
# dict4['name'] = "Nastya"
# print(dict4) #{'name': 'Torokul'}

'=============================Методы словарей=================='
# print(dir(dict4))
# get - метод , который возвращает значение по ключу если такого ключа нет то 
# возвращает None, или деволтное значение
# user = {
#     "name" : 'Torokul',
#     'city' : 'Bishkek',
#     'country' : " Kyrgyzstan",

# }
# print(user.get('name'))
# print(user.get('city'))
# print(user.get('country'))

# .pop()- Метод который удаляет пару по ключу и возвращает значение
# dict_ = {'a':1, 'b':2, "c":3}
# popped = dict_.pop('a')
# print(dict_)
# print(popped)
#вывод:#{'b': 2, 'c': 3}
#1
# dict_.pop('a') KeyError: 'a'

# . poppitem()-метод который удаляет последнюю пару и возвращает ее
# dict5= {'a':1, 'b':2, "c":3}
# popped = dict5.popitem()
# print(dict5)
# print(popped)
# #{'a': 1, 'b': 2}
# # ('c', 3)

# dict0 = {}
# print(dict0.popitem()) #KeyError: 'popitem(): dictionary is empty'

# update()- расширяет наш словарь парами из второго словаря
# dict1 = {1: 'a', 2: 'b', 3: ' c'}
# dict2 = {2: 'c', 4:'d'}
# dict1.update(dict2)
# print(dict1) #{1: 'a', 2: 'c', 3: ' c', 4: 'd'}

# # .clear() - удаляет все пары в словаре
# dict1.clear()
# print(dict1) #{}

#.fromkeys() - метод для создания нового словаря используя список ключей

# dict1 = dict.fromkeys('hi')
# print(dict1) #{'h': None, 'i': None}

# dict2 = dict.fromkeys([1, 2, 3])
# print(dict2) #{1: None, 2: None, 3: None}

# dict3 = dict.fromkeys([1,2,3], 'hello')
# print(dict3) #{1: 'hello', 2: 'hello', 3: 'hello'}


#print(dir(dict3))

"========================================================"
#keys, values, items
 #keys = метод который возвращает ключи
 # values - метод который возвращает значение
 # items - мед который возвращает пару в ключ - значение в виду tuple

user = {
    "name" : 'Torokul',
    'city' : 'Bishkek',
    'country' : " Kyrgyzstan",
}
# print(user.keys()) #dict_keys(['name', 'city', 'country'])
# print(user.values()) #dict_values(['Torokul', 'Bishkek', ' Kyrgyzstan'])
# print(user.items())#([('name', 'Torokul'), ('city', 'Bishkek'), ('country', ' Kyrgyzstan')])

'===========================Итерирование словарей==================='

user = {
    "name" : 'Torokul',
    'city' : 'Bishkek',
    'country' : " Kyrgyzstan",
}

# for key in user:
#     print(key)
# #name
# # city
# # country
# # при итерации словаря будут призодить ключи

# for key in user.keys():
#     print(key)
#     #name
#     # city
#     # country
#     # при итерации dict_keys тоде приходят ключи

# for value in user.values():
#     print(value)  
# #     Torokul
# # Bishkek
# #  Kyrgyzstan
# #при итерации dict_vales призодят значение

# for items in user.items():
#     print(items)
# #('name', 'Torokul')
# # ('city', 'Bishkek')
# # ('country', ' Kyrgyzstan')
# #При итерации dict_items приходят пары (ключ-значение ) в tuple

# for key,value in user.items():
#     print(key,value)
#     #name Torokul
#     # city Bishkek
#     # country  Kyrgyzstan

'''
Вам дан словарь


'''
# dict1 = {'a' : 1, 'b' : 2, "c" : 3}
# #создайте новый словарь dict2, поменяв местами ключи со значениями
# # dict2 = {1: 'a', 2: 'b', 3: 'c'}

# #items,for
# dict2 = {}
# dict2[1] = 'a'
# dict2[2] = 'b'
# dict2[3] = 'c'
# for key, value in dict1.items():
#     dict2[value] = key
#     print(dict2)
# {1: 'a', 2: 'b', 3: 'c'}




#dict4 = {}
# dict4['name'] = 'Torokul'
# dict4['name'] = "Nastya"
# print(dict4) #{'name': 'Torokul'}















