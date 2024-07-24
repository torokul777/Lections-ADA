'====================================Модули и пакеты======================='
# любой файл с расширение .py - модуль
# пакет - набор модулей(обязательно должен быть файл __init__.py)

'=================================Раобота с файлами=========================='
# open() - функция которая открывает файл в определенном режиме
'Режимы'
# r - read (только для чтения)
# w = write(только для записи, если такого файла нет то он его создаст,кадлый раз файл очищается)
# a = append(только для дозаписи данные добавляется в конец)
# x - создает файл, но если файл существует выйдет ошибка
# b - binary (в бинарном виде)

'==================================Read================================='
# file = open('test.txt','r')
# print(dir(file))
# print(file.writable()) #False (проверяет можно ли записывать чтото в файл)
# print(file.readable())# True 
# print(file.read())
# '''
# HELLO
# WORLD
# '''
# print(file.read()) # ''(потому что каретка находится в конце)
# file.seek(0) (метод переносит клетку на самое начало)
# print(file.read())
#HELLO
# WORLD
# print(file.read(5)) #HELLO (cчитает до скольки то )
# print(file.read(3))#HEL
# print(file.readline()) #HELLO (читает одну строку)

# file.seek(0)
# print(file.readlines())
# #['HELLO\n', 'WORLD\n']
# file.close()

# print(file.readlines())

'==========================Write======================'
# file = open('test2.txt','w')
# # если такого файла нет то он его создаст

# print(file.readable()) #False
# print(file.writable()) #True

# file2 = open('text.txt','w')
# # стирает данные существующего файла если они там есть

# file.write('hello\n') #принимает строку и записывает ее в файл
# file.write('Hello\n World\n')

# file.close()

'==================Append================'
# file = open('test2.txt','a')

# file.write('Hello')

# file.close()
'===============================Контекстный менеджер================'
# конструкция with.....as.....

# try:
#     file = open('sdfhjjs','w')
#     file.read() # ошибка
# finally:
#     file.close()

# with open('test.txt','r') as f:
#     print(f.read())

'==============Задачи==========='
'==============exercise1 =========='
# Создайте файл, внесите туда небольшой текст. 
# В программе откройте этот файл и выведите содержимое на экран. 


# file = open('toro.py','w')
# file.write('Torokul')
# file = open('toro.py','r')
# soderjimoe = file.read()
# print(soderjimoe)

'==============exercise 2================'
# Создайте файл Создайте файл users.txt. Напишите программу которая 
#  спрашивает у пользователя его Логин и Пароль и 
# записывает в файл users.txt
    

# file = open('users.txt','w')
# login = input('Введите логин:')
# password = (input('Введите пароль:'))
# file = open('users.txt','a')
# file.write('login:' + login + ' ''password:')
# file.write(password)

'==============exercise 3=================='
#  Создайте программу, которая считает из файла текст,
#  и если в тексте содержится буква “w”, 
# то выведет на экран “Да, в тексте есть w”, иначе - “Нет,
#  в тексте нет w”. Подсказка: используйте ключевое слово in.
# Открываем файл для чтения ('r' - режим чтения)


# with open('text.txt', 'r') as file:
#     content = file.read()
# if 'w' in content:
#     print('Да, в тексте есть w')
# else:
#     print("Нет, в тексте нет 'w'")

'==================exercise 4================'
# Создайте текстовый файл python.txt и запишите в него текст 
# #1 из github: Затем, считайте его. 
# Найдите слова которые содержат букву  "o" 
# и запишите в список o_words=[] и 
#   выведите на экран все полученные слова.
# текст: 
"""
Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
"""
text = '''
Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
'''
# with open('python.txt','w') as file:
#     file.write(text)

# with open('python.txt','r') as file:
#     content = file.read()

# o_words = [word for word in content.split() if 'o' in word ]
# print(o_words)

'====================exercise 5============'
#  Возьмите текст №2(GitHub), запишите его в файл.
#  Далее считайте этот текст с файла и выведите в обратном порядке.
"""
.detacilpmoc naht retteb si xelpmoC
.xelpmoc naht retteb si elpmiS
.ticilpmi naht retteb si ticilpxE
.ylgu naht retteb si lufituaeB

"""
# text = """
# .detacilpmoc naht retteb si xelpmoC
# .xelpmoc naht retteb si elpmiS
# .ticilpmi naht retteb si ticilpxE
# .ylgu naht retteb si lufituaeB

# """
# with open('task5.txt','w') as file:
#     file.write(text)

# with open('task5.txt','r') as file:
#     content = file.read()
#     reversed_content = content[::-1]
#     print(reversed_content)

'==================exercise6=============='
# Создайте файл и запишите туда текст №3(github). 
# В каждой строчке есть цифры, которые вместе дадут число. 
# Посчитайте сумму всех чисел. 

"""
123
aaa456
fxdya 5 0 0
"""

# text = """
# 123
# aaa456
# fxdya 5 0 0
# """
# with open('task6.txt','w') as file:
#     file.write(text)

# total_sum = 0
# with open('task6.txt','r') as file:
#     for line in file:
#         for word in line.split():
#             number =''.join(filter(str.isdigit,word))
#             if number:
#                 total_sum += int(number)
# print(f"Сумма чисел: {total_sum}")

'=======================================HOMEWORK==========================================='
# json завтрашняя тема
# giton и github тема  посмортеть
# cvs file дз скачать в vscode, скинуть материал в дискорд
'=======================================HOMEWORK============================================'
