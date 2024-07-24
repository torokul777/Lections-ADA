"================================Comprehension========================"
#Генератор с помощбю которого мы сможем создавать последовательности используя forв одну строку
'''
результат for элемент in посследовательность 
i for i in list1
pезультат for элемент in посследовательность if фильтр - фильтрация
i for i in list1 if i % 2 == 0
тело1 if условие else тело2 for элемент in посследовательность - условие
'четное' if i % 2 == 0 else 'нечетное' for i in range(1,11)
'''

# comprehension = ( i for i in range(1,6))
# print(comprehension) #<generator object <genexpr> 
# # генератор - итерируемый обьект который не хранит в себе всю посследовательность данных,
# # а создает их когда требуется
# print(next(comprehension)) # 1
# print(next(comprehension)) #2
# print(next(comprehension)) # 3
# print(next(comprehension)) # 4
# print(next(comprehension)) # 5

#next()- функция которая запрашивает у генератора текущий элемент и генератор создает следующий элемент

'==================================Синтаксический сахар========================='
# list comprehension
# list_comprehension = list( (i**2 for i in range (1,6)))
# print(list_comprehension) #[1, 4, 9, 16, 25]
# list_comprehension2 = [i**2 for i in range(1,6)]
# print(list_comprehension2) #[1, 4, 9, 16, 25]

# lst = [i for i in range (1,11) if i % 2 == 0]
# print(lst)
# lst1 = [ i for i in range(2,11,2)]
# print(lst1)

# list3 = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list3.append(i)
# print(list3)

# list1 = []
# for i in range(5):
#     list1.append('hello')
# print(list1)
#['hello', 'hello', 'hello', 'hello', 'hello']

# list_ = ['hello' for i in range(5)]
# print(list_)
#['hello', 'hello', 'hello', 'hello', 'hello']

# list3 = []
# for i in range(1,11):
#     if i % 2 ==0:
#         list3.append('четное')
#     else:
#         list3.append('нечетное')
# print(list3)


# list1 = ['четное' if num % 2 == 0 else 'нечетное' for num in range(1,11) ]
# print(list1)
# ['нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное']


# list1 = [1, 'hello', 2, 'a', 2.3, 1000, 'world']
# for i in list1:
#     if type(list1) != str:
#         print(None)
# print(list1)


# list1 = [1, 'hello', 2, 'a', 2.3, 1000, 'world']
# list2 = [ i for i in list1 if type(i) == str]
# print(list2)

'====================Dict comprehension ==========================='
# dict_ = dict( (i, i**2) for i in range(10))
# print(dict_)
# #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# dict1 = {i: i**2 for i in range(10)}
# print(dict1)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}



'дан словарь создайте его копию с помощью compehension'
# dict1 = {"a":1, "b":2, "c":3}
# dict2 = {key: value for key, value in dict1.items()}
# print(dict1)
# print(dict2)

# dict_ = {}
# for key,value in dict1.items():
#     dict_[key] = value
# print(dict_)

# dict1 = {"a":1, "b":2, "c":3}
# dict2 = {value: key for key,value in dict1.items()}
# print(dict2)

'Дан словарь где значение это - спски с числами создайте словарь где значениями будут суммы этих чисел'
# dict1 = {
#     "a":[1,2,3,4],
#     "b":[10,15,16,17],
#     "c":[1,2,54]
# }
# dict2 = {key: sum(value) for key,value in dict1.items()}
# print(dict2)
# {'a': 10, 'b': 58, 'c': 57}

'дан словарь с ключами где числа от 1 до 10 а значение числа в виде строк'

# dict2 = {i: str(i) for i in range(1,11)}
# print(dict2)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']


# dict11= {}
# for list1,list2 in dict11:
#      dict11[list1] = list2
# print(dict11)
 
# 1 sposop
dict_ = {}
# for ind in range(len(list1)):
#      key = list1[ind]
#      value = list2[ind]
#      dict_[key] = value
# print(dict_)



# # 2 sposob
# dict_ = {list1[ind]:list2[ind] for ind in range(len(list1))}


# #3 sposob
# dict_ = dict(zip(list1,list2))
# print(dict_)

'==========================Вложенные comprehension======================'
# 1 sposob

# dict1 = {}
# for i in range(1,6):
#     key = i
#     value = [j for j in range(1, +i+1)]
#     dict1[key] = value
# print(dict1)
# #{1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

# # 2 sposob
# dict3 = {i: [j for j in range(1, i+1)] for i in range(1,6)}
# print(dict3)

# # 3 sposob
# dict_ = {i: list(range(1,i+1)) for i in range(1,6)}
# print(dict_)


# lst = []
# for i in range(10):
#     inner_list = []
#     for j in range(5):
#         inner_list.append('hello world')
#     lst.append(inner_list)
# print(lst)


# #2 sposob

# list1 = [['hello world' for j in range(5)] for i in range(10)]
# print(list1)

# 3 sposob
# list1 = [['hello world'] * 5 for i in range(10)]
# print(list1)

# 4 sposob
# list1 = [['hello world']*5]*10
# print(list1)

# while (alive) {
#     eat();
#     sleep();
#     code();
#     repeat();
# }
# list5 = [[ i for i in range(1,6)] for i in range(11)]
# print(list5)
'====='
# dict1 = {}
# for i in range(1,6):
#     key = i
#     value = [j for j in range(1, +i+1)]
#     dict1[key] = value
# print(dict1)
  #1 sposob
# dict1 = {}
# for i in range(1,6):
#     inner_dict = {}
#     for j in range(1, i+1):
#         list_ = []
#         for k in range(1,j+1):
#             list_.append(k)
#         inner_dict[j] = list_
#     dict_[i] = inner_dict
# print(dict1)

#2 sposob
# dict2 = {
#     i:{
#         j:[k for k in range(1,j+1)] for j in range(1, i+1)
#     }
#     for i in range(1,6)
# }
# print(dict2)

# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k.replace('i',''):k.count('i')for k in dict1}
# print(dict2)
'===='
# Используя приведенный словарь dict_, создайте список из id, 
# которые хранятся под ключом comments. Берите только те комментарии, 
# количество которых больше 3
# Используя приведенный словарь dict_, создайте список из id, 
# которые хранятся под ключом comments. Берите только те комментарии, 
# количество которых больше 3
dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}
# 1 sposob
# ids = []

# for inner_dict in dict_.values():
#     comments = inner_dict['comments']
#     if len(comments) >3:
#         for comment in comments:
#             ids.append(comment['id'])
# print(ids)


#2 sposob

# ids = [comment['id'] for inner_dict in dict_.values() for comment in inner_dict['comments'] if len(comment) > 3]
# print(ids)

'exercise 1'

# list1 = [False, True, False, True, False, True, False, True, False, True] 
#  Преобразовать список логических значений в список целых чисел, 
#  где True становится 1, а False — 0:
#  list2 = [1 if i else 0 for i in list1]
# print(list2)

'exercise 2'

# list_name = ["paul", "john", "george", "ringo", "eric", "patty", "yoko", "cynthia", "linda", "jude"]
# # Создать список, содержащий длины имен из исходного списка имен:
# len_list = [len(i) for i in list_name]
# print(len_list)

'exercise 3'

# Создать список четных чисел в диапазоне от 1 до 1000 с шагом 125:
# list0 = [ element for element in range(1,1000,125)if  element % 2 == 0 ]
# print(list0)

'exercise 4'

# list1 = [44, 54, 64, 74, 104]
# # Добавить к каждому элементу списка число 6:
# list2 = [i + 6 for i in list1]
# print(list2)

'exercise 5'
# list1 = [2, 4, 6, 8, 10, 12, 14]
# # Создать список из элементов другого списка, квадраты которых больше 50:
# list2 = [i for i in list1 if i**2 > 50]
# print(list2)

' exercise 6 '
# dict1 = {"a": {"d": 3, "e": 45}, "b": {"f": 23, "j": 9}, "c": {"h": 12, "i": 89}}
# # Создать список всех значений из вложенных словарей:
# list1 = [i for i in dict1.values()]
# print(list1)

'exercise 7'
#  Создать список ключей словаря, где значения находятся в диапазоне
# от 200 до 5000, и привести ключи к верхнему регистру:

# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# list1 = [kluych.upper()  for kluych, znachenie in dict_.items() if 200 <= znachenie <= 5000]
# print(list1)

'exercise 8'
# Создать новый список, исключив все пустые
# и None элементы из исходного списка:
# list1 = [1, 2, 3, 0, None, "a", "abc", [], 23, [1, 2, 3, 4], "", {"a": 1, "b": 2}, "drf", []]
# list2 = [i for i in list1 if i != [] and i != '' and i != None]
# print(list2)



'==================================================================================='
# метод items() 
my_dict = {"a": 1, "b": 2, "c": 3}

# Получение представления пар ключ-значение
items_view = my_dict.items()

print(items_view)
# Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Использование представления для итерации по парам ключ-значение
for key, value in items_view:
    print(f"Key: {key}, Value: {value}")

# Output:
# Key: a, Value: 1
# Key: b, Value: 2
# Key: c, Value: 3
'==================================================================================='
def find_min_number():
    numbers_set = set()  # создаем пустое множество для хранения уникальных чисел

    

    for i in range(5):
        numbers_set.add(num)  # добавляем число в множествоfind_min_number()
        num = int(input(f"Введите число {i + 1}: "))

    
    min_number = min(numbers_set)

    # Выводим результат
    print(f"Самое маленькое число, которое вы ввели: {min_number}")

# Вызываем функцию для выполнения програмовровыгр_2оауц48  оаг7774 7г4
