# # # "==============================1st exercise=========================="
# # # n1 = 45
# # # n2 = 6
# # # if n1 % n2 == 0:
# # #     print("Соответствующее сообщение")
# # # else:
# # #     print('не делится')

# # # "=============================2nd exercise============================"
# # # n =  int(input())
# # # if n % 6 == 0:
# # #     print('Делится')
# # # else:
# # #     print('Не делится')
# # # "=============================3rd exercise============================"
# # # n1 = int(input())
# # # n2 = int(input())
# # # n3 = int(input())
# # # numbers = n1
# # # numbers = n2
# # # numbers = n3
# # # if numbers > 10:
# # #     print("yes")
# # # else:
# # #     print('no')
# # # "=============================4th exercise============================"
# # # a = int(input())
# # # if a > 0 and a < 5:
# # #     print('Верно')
# # # else:
# # #     print('неверно')
# # # "=============================5th exercise============================"
# # # a = int(input())
# # # b = int(input())
# # # if a <= 1 and b >= 3:
# # #     print(a + b)
# # # else:
# # #     print(b - a)
# # # "=============================6th exercise============================"
# # # a = int(input('a='))
# # # b = int(input('b='))
# # # if a > 2 and a < 11 or b >= 6 and b < 14:
# # #     print("Верно")
# # # else:
# # #     print('Неверно')

# # # "=============================7th exercise============================"
# # # month = int(input('введите число, чтобы определить время года'))
# # # if month <= 3 :
# # #     print("зима")
# # # elif month <=6 :
# # #     print('лето')
# # # elif month <= 9:
# # #     print('весна')
# # # elif month <= 12:
# # #     print('осень')
# # # "=============================8th exercise============================"
# # # nomer = int(input())
# # # if nomer <=20:
# # #     print("добро пожаловать в первый подьезд!")
# # # elif nomer <=48:
# # #     print("добро пожаловать во второй подьезд!")
# # # elif nomer <=90:
# # #     print("добро пожаловать в третий подьезд!")
# # '=========================================================================='
# # #Напишите мини-проект “Калькулятор”. Для этого, вам
# # # необходимо вспомнить стандартный ввод и вывод данных, тип
# # # данных Числа и операции над числами. Также вам потребуется
# # # помощь условных операторов и циклов.
# # # Требования:
# # # 1. Ваш калькулятор должен запрашивать последовательно
# # # первое число, затем второе число. Затем калькулятор должен
# # # запросить операцию, которую он произведет с числами (сложение,
# # # вычитание, умножение, деление, остаток от деления, возведение в
# # # степень, целочисленное деление)
# # # 2. Далее калькулятор выдает вам ответ.
# # # 3. Если пользователь вводит несуществующую операцию,
# # # калькулятор выводит сообщение: “Данной операции нет в системе”
# # # 3. После того, как действие над числами было проведено, и ответ вернулся. Работа калькулятора не должна быть окончена. В терминале должно выйти собщение "Хотите продолжить?", если ответ "yes", то калькулятор снова должен запросить 2 числа и операцию над ними. Если ответ "no", то работа калькулятора должна быть завершена, и должно выйти сообщение "До свидания!"
# # # Пример:
# # # Ввод:
# # # Введите первое число: 3
# # # Введите второе число: 7
# # # Выберите операцию из следующих +-*/%// : *
# # # Вывод:
# # # Ответ: 21
# # # Ввод:
# # # Хотите продолжить(yes/no)?: yes
# # # Введите первое число: 5
# # # Введите второе число: 5
# # # Выберите операцию из следующих +-*/%// : +
# # # Вывод:
# # # Ответ: 10
# # # Хотите продолжить(yes/no)?: no
# # # Вывод: До свидания!
# # # Пример:
# # # Ввод:
# # # Введите первое число: 3
# # # Введите второе число: 7
# # # Выберите операцию из следующих +-*/%// : =
# # # Вывод:
# # # Ответ: Данной операции нет в системе


while True:
    a = int(input('Введите 1-ое число:'))
    b = int(input('Ввелите 2-ое число:'))
    operasia = input('Выберите операцию +,-,*,/,%,//,**')
    if operasia == '+':
        print(a + b)
    elif operasia == "-":
        print(a - b)
    elif operasia == '*':
        print(a * b)
    elif operasia == "/":
        print(a / b)
    elif operasia == "%":
        print(a % b)
    elif operasia == '//':
        print (a // b)
    elif operasia =='**':
        print(a ** b)
    else:
        print('Данной операции нет в системе!')
    prodoljenie = input(('Хотите продолжить(yes/no?)'))
    if prodoljenie.lower() != 'yes':    
        break

# # '========home work================'
# # '1 exercise'
# # #for i in range(1,101):    print(i)


# # '2 exercise'
# # #for i in range(0,51,2): print(i)

# # '3 exercise'
# # # list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# # # list123 = [i for i in list_ if i > 0]
# # # print(list123)
# # '4 exercise'

# # # numbers  = [num ** 2 for num in range(1, 26)]
# # # print(numbers)

# # '5 exercise'
# # # str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# # # list1 = [] 

# # # for i in str_list:
# # #     list1.append(int(i))  

# # # print(list1)

# # '6 exercise'
# # # toro = [i ** 2 if i % 2 == 0 else i for i in range(1, 11)]
# # # print(toro)

# # '7 exercise ' 
# # # toro = [print('True') if i % 2 == 0 else print('False') for i in range(1,11)]

# # '8 exercise'
# # # list_name = ["paul", "john", "george", "ringo", "eric", "patty", "yoko", "cynthia", "linda", "jude" ]
# # # toro = ['longer' if len(torokul) > 4 else 'shorter' for torokul in list_name]
# # # print(toro)
# # # list_name = ["paul", "john", "george", "ringo", "eric", "patty", "yoko", "cynthia", "linda", "jude"]
 
# # ' 9 exercise'
# # # dict1 = {num: num ** 2 for num in range(1,11) }
# # # print(dict1)
# # '10 exercise'
# # # n = int(input('Введите число:'))
# # # dict2 = {num: num ** 2 for num in range(1,501) if num % n == 0 ** 2 }
# # # print(dict2)
# # # Пример словаря
# # my_dict = {'a': 1, 'b': 2, 'c': 3}

# # # Запрашиваем у пользователя ключ для поиска
# # key = input("Введите ключ для поиска: ")

# # try:
# #     # Пытаемся получить значение по ключу из словаря
# #     value = my_dict[key]
# #     print(f"Значение по ключу '{key}': {value}")
# # except KeyError:
# #     # Обработка исключения, если ключа нет в словаре
# #     print("Нет такого ключа!")



# # # Пример списка
# # my_list = [1, 2, 3, 4, 5]

# # try:
# #     # Запрашиваем у пользователя индекс элемента
# #     index = int(input(f"Введите индекс (от 0 до {len(my_list)-1}): "))
    
# #     # Пытаемся получить элемент по указанному индексу
# #     element = my_list[index]
# #     print(f"Элемент по индексу {index}: {element}")
    
# # except IndexError:
# #     # Обработка исключения, если индекс выходит за пределы списка
# #     print("Нет такого элемента!")
# # except ValueError:
# #     # Обработка исключения, если введенное значение не является целым числом
# #     print("Введите целое число в качестве индекса!")


# # try:
# #     age = int(input("Введите ваш возраст: "))
    
# #     if age < 18:
# #         raise ValueError("Доступ запрещён")
    
# # except ValueError as e:
# #     print("Введён некорректный возраст")
    
# # else:
# #     print("Спасибо")
    
# # finally:
   
   
   
   
   
   
# #     print("До свидания!")




# # try:
# #     num1 = float(input("Введите первое число: "))
# #     num2 = float(input("Введите второе число: "))
    
# #     result = num1 / num2
    
# # except ValueError:
# #     print("Произошла ошибка!")
    
# # except ZeroDivisionError:
# #     print("Произошла ошибка!")
    
# # else:
# #     print(f"Результат деления {num1} на {num2} равен {result:.2f}")





# # try:
# #     amount = float(input("Введите сумму денег: "))
    
# #     if amount < 0:
# #         raise ValueError("Сумма не может быть отрицательной!")
    
# # except ValueError as e:
# #     print(f"Ошибка: {e}")
    
# # else:
# #     print(f"Сумма денег: {amount:.2f}")



# # try:
# #     result = obj.get()
# #     print("Метод успешно вызван")
# # except AttributeError:
# #     print("Объект не имеет метода get")
# # except Exception as e:
# #     print(f"Произошла ошибка: {e}")





# # my_list = [1, 2, 3, 4, 5]

# # try:
# #     my_list.get()
# # except AttributeError:
# #     pass  # Ничего не делаем, если возникает AttributeError






# try:
#     result = "строка" + 123  # Попытка сложить строку и число
# except TypeError:
#     print("Unsupported option")  # Обработка исключения TypeError


# my_list = [1, 2, 3, 4, 5]

# try:
#     index = 0
#     while True:
#         print(my_list[index])
#         index += 1

# except IndexError:
#     pass  # Ничего не делаем при возникновении IndexError









# password = input("Введите пароль: ")

# if len(password) < 6:
#     raise ValueError("Длина пароля должна быть не менее 6 символов")
# else:
#     print("Пароль принят")

# warehouse = [
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]

# max_length = 10 # Максимальная длина хранилища

# if len(warehouse) > max_length:
#     raise ValueError(f"Длина хранилища превышает {max_length}")
# else:
#     print("Длина хранилища в пределах допустимого")






# value = 10

# try:
#     while value > 0:
#         print(f"Текущее значение: {value}")
#         value -= 1
# except KeyboardInterrupt:
#     print("\nNope")

# input_string = input("Введите элементы, разделенные пробелами: ")

# try:
#     elements = input_string.split()
#     numbers = []
    
#     for element in elements:
#         try:
#             number = int(element)
#             numbers.append(number)
#         except ValueError:
#             raise ValueError(f"Данный элемент '{element}' не является числом!")
    
#     print("Список чисел:", numbers)

# except ValueError as e:
#     print(f"Ошибка: {e}")
# login = input('Введите свой логин:')
# password = input('Введите свой пароль:')
# if login == type(str):
#     print('Вы успшено ввели логин!')
# elif password == type(str or int):
#     print('Вы успешно ввели свой пароль!')
# print(f"Ваш логин: {login}")
# print(f"Ваш пароль: {password}")

