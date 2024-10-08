'===========================================Exceptions========================================='
#Исключения(ошибки )- это обекты которые прервывают работу кода если не были обработаны

SyntaxError
#исключение которое выходит когда в коде допущена синтаксическая ошибка
"""
(
SyntaxError: unexpected EOF while parsing
(когда мы не закрыли скобочку или кавычку)
"""

"""
a = 
SyntaxError: invalid syntax
(когда мы сделали что-то не правильно в синтаксисе)
"""


NameError
#Исключение которое выходит когда мы обращаемся к несузествующей переменной
# print(toro)


IndexError
# Исключение которые выходит когда мы обращаемся по несуществующему индексу
# list_ = [1,2,3 ]
# # print(list_[1000])

# [1,2,3].pop(1000)
# IndexError: pop index out of range

KeyError
# исключение которое выходит когда обращаемся по несуществующему ключу
# dict1 = {1: 1}
# dict1.pop('b')

ValueError
# когда мы передаем в функцию некоректный дл нее тип данных
#когда мы распаковываем итерируемый обьект на несколько переменных и количество переменных не совпадает с количеством элементов в итрерируемом обьекте


# a, b, c = [1, 2] #ValueError: not enough values to unpack (expected 3, got 2)
IndentationError
# выходит когда мы не правильно используем отступы 
#     a = 5
# IndentationError: unexpected indent

TypeError
# возникает когда мы пытаемся использовать методы не свойственные какому - то типу данных
# или когда мы пытаемся передать функции больше или меньше аргументов чем принимает функция
# '5' + 5 TypeError: can only concatenate str (not "int") to str


Exception
#исключение которое создали чтобы его вызвали

'=====================================================Вызов исключений====================================================='
 # raise NameError('my exceptions ' ) #NameError: my exceptions


'=====================================================Обработка исключений====================================================='
#чтобы код не прекращал свою работу мы сможем использовать конструкцию try - except, и обрабатывать вызванное исключение
# try:
#     # код который возможно вызовит ошибку 
#     num = int(input('Введите число:'))
# except ValueError: #обишка которая может возникнуть
#         print('Вы вели не число')
# else:
#     # код который отработает только если ошибка не вышла
#         print('Введенное число ', num)
# finally:
#         #код который отработает в любом случае
#         print('до свидания')

# try:
#     raise ValueError
# except(SyntaxError, NameError):
#     print('Вышла одна из ошибок: SyntaxError , NameError')

# try:
#     raise Exception
# except:
#     print('Отловленна любая ошибка')

# try:
#     raise  TypeError('TypeError')
# except Exception as error:
#     print('Ошибка' , type(error).__name__)

# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass

# Напишите код, который пытается вывести значение переменной, не 
# определенной ранее, и обрабатывает исключение, выводя сообщение 
# "Такой переменной не существует!".
# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print('Такой переменной не существует')

# Напишите код, который принимает два числа от пользователя
#  и выводит результат их деления. 
# Обработайте исключение, которое выйдет при делении на ноль, 
# выводя сообщение "На ноль делить нельзя"

# a = int(input('Введите 1-ое число:'))
# b = int(input('Введите 2-ое число:'))

# try:
#     print(a/b)
# except (ZeroDivisionError, TypeError, ValueError):
#     print('на ноль делить нельзя')

# Напишите код, который принимает две строки от пользователя, 
# преобразует их в целые числа и выводит их сумму. 
# Обработайте исключение которое выйдет в случае если 
# пользователь передал не число а строку, выводя сообщение "Введите число!".

# num1 = (input('Введите 1-ую строку:'))
# num2 = (input('Введите 2-ую строку:'))

# try:
#     print(int(num1)+int(num2))
# except ValueError:
#     print('Введите число')

# dict1 = {'a' : 1, 'b' : 2, 'c': 3}

# try:
#     dict1['d']
# except KeyError:
#     print('Нет такого ключа')


# list_ = [1,2,3,4,5]
# try:
#     list_[8]
# except IndexError:
#     print('Такого индекса нет')




# Напишите код, который принимает возраст от пользователя и выбрасывает 
# исключение ValueError с сообщением "Доступ запрещён", если возраст меньше 18.
#  Обработайте это исключение, выводя сообщение "Введён некорректный возраст".
#  Используйте блоки else и finally для вывода сообщений "Спасибо" и "До свидания!"
#  соответственно.

# age = int(input('Введите свой возраст:'))
# try:
#     if age < 18:
#         raise ValueError('Доступ запрещен')
# except ValueError:
#     print('Введен некоректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# Напишите код, который принимает два числа от пользователя и выводит 
# результат их деления. Обработайте исключения ValueError и ZeroDivisionError, 
# выводя сообщение "Произошла ошибка!".

# try:
#     num1 = float(input('введите первое число:'))
#     num2 = float(input('Введите второе число:'))
#     r = num1 / num2
# except(ValueError,ZeroDivisionError):
#     print('Произошла ошибка')
# else:
#     print(r)

# Напишите код, который принимает сумму денег от пользователя и выбрасывает 
# исключение ValueError с сообщением "Сумма не может быть отрицательной!", 
# если сумма меньше 0. Обработайте это исключение и выведите сообщение ошибки. 
# Если исключение не возникло, выведите сумму.


# try:
#     summa = float(input('Введите сумму чисел:'))
#     if summa < 0 :
#         raise ValueError 
# except ValueError:
#     print('Ошибка')
# else:
#     print(summa)



#  Напишите код, который пытается вызвать метод get для списка.
#  Обработайте исключение AttributeError,
#  не выполняя никаких действий при возникновении ошибки.

# lst1 = [1,2,3,4,5]
# try:
#     lst1.get()
#     print('метод вызван')
# except AttributeError:
#     print('Ошибка')



# Напишите код, который пытается сложить строку и число. Обработайте исключение
#  TypeError, выводя сообщение "Unsupported option".



# try:
#     str1 = str(input('Введите строку:'))
#     int1 = int(input('Введите число:'))
#     summa = str1 + int1
# except TypeError:
#     print('Unsupported option')


# Напишите код, который пытается расширить список, который не был создан. 
# Обработайте исключение NameError, и выведите сообщение 'list does not exist'.

# try:
#     list1.extend(range(10))
# except NameError:
#     print('list does not exist')


# Напишите код, который перебирает элементы списка, превышая его длину.
#  Обработайте исключение IndexError, не выполняя никаких действий
#  при возникновении ошибки



# try:
#     list1 = [1,2,3,4,5,6,7]

#     for i in range(0,len(list1)+1):
#         print(list1[i])
# except IndexError:
#     print('Ошибка')




# Напишите код, который проверяет длину пароля и выбрасывает исключение ValueError,
#  если длина меньше 6 символов. 
# (можно без try-except, просто через raise выкидывать ошибку)
# parol = input('Введите пароль:')
# if len(parol) < 6:
#     raise ValueError('Пароль должен составлять не менее больше 6 символов')
# else:
#     print('Пароль верный')



# warehouse = [
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]
# # Напишите код, который проверяет длину хранилища и выбрасывает 
# # исключение ValueError, если длина больше 10

# if len(warehouse) > 10:
#        raise ValueError(' на складе не должно быть более 10 коробок')
# for box in warehouse:
#         if len(box) > 3:
#               raise ValueError('в коробке  не должно быть более 3х элементов')


# # Напишите код, который пытается импортировать несуществующий модуль lamabimgo.
# #  Обработайте исключение ImportError, выводя сообщение "Такого модуля нет"

# try:
#     import lamabigmo
# except ImportError:
#       print('Такого модуля не существует')

# n = 10
# try:
#     while n > 0:
#          print(n)
#          n -=1
# except KeyboardInterrupt:
#          print('Nope')


#  Напишите код, который принимает строку, разделяет её на 
# элементы и пытается преобразовать каждый элемент в целое число, 
# добавляя его в список. 
# Если элемент не является числом, выбрасывайте исключение ValueError
#  с сообщением "Данный элемент не является числом!".

# str1 = input('Введите число:').split()
# list1 = []
# for element in str1:
#     try:
#         list1.append(int(element))
#     except ValueError:
#         print('данный элемент не является числом')
# print(list1)

'=============================================HOMEWORK============================'

'======================exercise 1======================'
# def min_num():
#     num_set = set()
#     num1 = int(input('Введите первое число :'))
#     num2 = int(input('Введите второе число :'))
#     num3 = int(input('Введите третье число :'))
#     num4 = int(input('Введите четвертое число :'))
#     num5 = int(input('Введите пятое число :'))
#     num_set.add(num1)
#     num_set.add(num2)
#     num_set.add(num3)
#     num_set.add(num4)
#     num_set.add(num5)
#     min_number = min(num_set)
#     print(f"Самое маленькое число:{min_number}")
# min_num()

'======================exercise 2======================'
# Вы работаете в Банке и пишите программу которая считает % для кредита.
#  Спросите у пользователя сумму займа(не меньше 100 000)
#  и посчитайте сколько нужно будет вернуть если процент = 7.89, 
# результат округлите до 2 чисел после точки.
# Формула подсчёта переплаты: Сумма * (% / 100)

# def bank():
#     summa = float(input('Введите сумму займа(не меньше 100 000) '))
#     procent = 7.89
#     res = summa * (procent / 100)
#     res = round(res,2)
#     print(f"результат:{res}")

# bank()

'=============================exercise 7===================='
#  Напишите функцию add, 
# которая принимает два целых числа и возвращает их сумму.

# def add():
#     n1 = int(input('введите первое число:'))
#     n2 = int(input('введите второе число:'))
#     res = n1+n2
#     print(f'Сумма первого и второго числа равна:{res}')
# add()
'==========================exercise 8 ======================='

# Напишите функцию get_string_length,
#  которая принимает строку и возвращает ее длину.

# def get_string_length():
#     str_ = input('Введите строку:')
#     res = len(str_)
#     print(f'Длина строки равна:{res}')
# get_string_length()

'==========================================exercise 9==========================='
# Напишите функцию get_type, которая принимает два объекта 
# и выводит их типы данных
# def get_type(object1,object2):
#     res1 = type(object1) 
#     res2 = type(object2) 
#     print(res1)
#     print(res2)
# get_type(object1=12,object2='torokul')

'======================exercise 10=================='
# Напишите функцию check, которая принимает целое число
#  и возвращает строку "It is odd number", 
# если число нечетное, и "It is even number", если число четное.
# def check():
#     n = int(input('Введите целое число:'))
#     if n % 2 != 0:
#         print('It is odd number')
#     else:
#         print( "It is even number")
#     print(n)

# check()

'========================exercise 11================='
# Напишите функцию is_palindrome, которая принимает строку и возвращает
#  True, если строка является палиндромом, и False в противном случае. 
# Палиндром - строка которая справа налево, и слева на право читается одинаково.
#  Например "Анна", "Казак" 
# def is_palindrome():
#     str1  = input('Введите строку:')
#     if str1 == str1[: : -1]:
#         print('True')
#     else:
#         print('False')
    
# is_palindrome()

'=========================exercise 12=================='
# Напишите функцию max_num, которая принимает два целых числа
#  и возвращает большее из них.
# def max_num():
#     n1 = int(input('Введите первое целое число:'))
#     n2 = int(input('Введите второе целое число:'))
#     if n1 > n2:
#         print('Первое число больше второго')
#     elif n2 > n1:
#         print('Второе число больше первого')
#     else:
#         print('оба числа равны')
# max_num()

'==========================exercise 13================'
#  Напишите функцию multiply_list,
#  которая принимает список чисел и возвращает их произведение.

# def multiple_list(numbers):
#     res = 1
#     for num in numbers:
#         res *= num 
#     return res
# list1 = [5,5]
# print(f"Произведение чисел {list1} равно {multiple_list(list1)}")

'===============================exercise 14====================='

#Напишите функцию sum_digits, которая принимает целое 
#число и возвращает сумму его цифр.
#Например: число 122 - его сумма 5, так как 1 + 2 + 2 = 5
# def sum_digits(number):
#     summa = 0
#     for i in str(number):
#         if i.isdigit():
#             summa += int(i)
#     return summa
# n1 = 122
# print(f"Сумма {n1} равна {sum_digits(n1)}")

# n2 = 456
# print(f"Сумма {n2} равна {sum_digits(n2)}")

n1 = int(input())
k = map(int,input())
if sum(k) == 0:
    print('EASY')
else:
    print('HARD')
