'=====================================================Области видимости======================================'
# LEGB - local enclosed global built - in

'==========================Built - in========================='
#Встроенное пространство имен (liat, sum , dict , print,input)

'====================================== Global========================='
# Все переменные которые мы создали внутри одного файла 
# чтобы посмотреть все глобальные переменные можно использовать global()

# a = 5
# b = 'hello'
# print(globals())
'====================================Local============================='
# локальное пространство имен - переменные созданные внутри функции(цикла, условия)
# a = 10

# def func(a,b):
#     print('GLOBALS',globals())
#     print('LOCALS',locals())
#     print(a,b)
# func(5,7)

'====================================Enclosed=========================='
# Замкнутая пространство имен - локальное пространство у которого есть внутренее локальное пространство
# vars - 'global'
# def func():
#     #локальное пространство для глобального пространства
#     # замкнутая пространство потому что есть (более локальное пространство)
#     vars = 'enclosed'
#     def inner_func():
#         #локальное пространство для пространство func
#         vars = 'local'
#         print(vars)
#     print(vars)
#     inner_func()

# print(vars)
# func()

# count = 1213

# def inncrease_count():
#     global count 
#     print(count)
#     count += 1213
    

# inncrease_count()
# inncrease_count()
# inncrease_count()
# inncrease_count()
# inncrease_count()

# def count(i):
#     counter = 0

#     def increase_counter():
#         nonlocal counter
#         # допступ на изменение переменной на замкнутого пространства
#         print(counter)
#         counter += 1

#     for _ in range(i):
#         increase_counter()
# count(11) 


