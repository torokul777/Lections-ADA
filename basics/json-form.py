'============================JSON========================='
#Javascriot Object notation - Универсальный формат в котором мы можем 
# хранить данные в типах данных понятных почти для всех языков 
# в программировнии

# import json

# json_list = "[1,2,3,4,5]"
# print(type(json_list)) #<class 'str'>

# python_list = json.loads(json_list)
# print(type(python_list)) #<class 'list'>

#Десерализация - это перевод с json строку в python обьект
# .loads() - для десереализации с json строки
# .load() - метод для десереализации с json файла

# сереализация - перевод python обьектов в JSON строку
# .dumbs() - метод для сереализации а json строку
# .dumb() - метод для сереализации в json файл

# with open('test.json','r') as file:
#     list_ = json.load(file)

# print(list_)
# list_.append((1,2,3))
# print(list_)

# with open('test.json','a') as file:
#     json.dump(list_,file)

            
