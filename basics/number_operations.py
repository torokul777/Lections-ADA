"===================Числа============="
#integers(int)- целые числа(1,2,3,4)


#age=10
#print(type(age)) #<class 'int'>
# type()- возвращает класс / тип данных к которому относится 
#переменная или значения

#b = int('10j) # ValueError : invalid literal for int() with base
#10: '`10j'`
#print (type(b))
#b = int('10')
# print(type(b)) #<class 'int'



"=====================float================"
#float - вещественные числа/числа с плавающей точкой/ десятичные

#price = 105.5
#print(type(price)) #<class 'float'>

#price2 = float(1)#1.0
#print(price2)

#price3 = float('10.64')
#print(price3)
#print(type(price3))


#import decimal
#from decimal import Decimal 

#a = Decimal('0.1')
#print(a) #0.1
#print(type(a)) #<class 'decimal.Decimal'>

"=================binary============="

# a = bin(10)
# print(a)#ob1010
# print(int(a, 2)) #10

"==================Операции над чсилами============"

# 5+7 #сложение
# 7 - 3 #вычитание
# 10*4 # умножение
# 10 / 3 #деление
# 10 // 2 #целое
# 5 % 2 #нахождение остатка от деления
# 2 ** 3 #возведения числа в степень
# 25 ** 0.5 # 5, нахождения квадратного корня

#модуль числа - из отрицательного числа в положительное
# |-5| = 5
#abs - для получения положительного числа

# print(abs(-5))
# print(abs(-8))
# print(abs(-0))


# #round()- округление числа
# print(round(1.53))
# print(round(1.555555555555555))
# print(round(1.51))
# print(round(1.5))

"""
python3 <название файла> - запуск файла через терминал 

python3 - вход в систему python shell
ctrl + d - выход из python shell
"""



#sqrt - Функция для нахождения квадратного корня числа.
# sqrt обязательно нужно импортировать

# import sqrt
# from math import sqrt

# print(sqrt(25))
# print(sqrt(36))
# print(sqrt(34))

# ==================================
# command+slash==все в хештег
# ==================================


#pow
#1) возводит число в степень
#2) находит остаток от деления на 3 число


# print(pow(2,3)) #8
# print(pow(2,3,3)) #2**3%3=2


#divmod()-функция возвращает 2 числа, где 1 число - целая часть от деления,
#2 число -остаток от деления
# print(divmod(8,2))
# print(divmod(5,2))
# print(divmod(17,3))


w1 = int(input('Введи 1-ое число:'))
w2 = int(input('Введи 2-ое чсило:'))
print(w1+w2)


