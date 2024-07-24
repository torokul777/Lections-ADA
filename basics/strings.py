"==============Строки=============="
# Строки - это неизменяемый тип данных, который предназначен для хранение текста,
# заключенного в одинарные или двойные ковычки

# str_= 'строка с одинарными кавычками'
# str2= "строка с двойными кавычками"
# # error_string = 'неправильная строка"
# str3 = """
# Многострочный текст в двойных кавычках, можно использовать 'любые' "кавычки"
# """

# str4 = 'Don\'t'
# str5 = "Don't"

"====================Конкетенация======="
# name = 'torokul'
# last_name = 'zhanyshbekov'
# full_name = name+' '+last_name


# print(full_name)
# print('Hello'*10)

"==========Экранизация строк==========="
#'\n' - переносит на новую строку
#print('Hello\nworld')
# print('Hello')
# print('world')
# \t- табулция
print('hello\tworld')

# \v - перенос на новую строку со смещение вправо на длину
#предыдущей строки
# print('hello\vworld\vmy\vname\v')

#\r - перенос каретки на начало строки
# print('hello \rHi')#Hillo

"===================Форматироване строк=================="
# title = 'Iphone 15'
# price = 1000
# print(f'Название: {title}\nЦена:{price}')


# format2 = 'Название: {}\nЦена: {}'
# print(format2.format(' Iphone 15', '1000'))
# print(format2.format(' Iphone 12', '700'))


# format3 = 'Название: %s\nЦена :%s'
# print(format3 % ('Iphone 15', '1000'))

"==================Методы строк==============="
#Методы - это функции, которые относятся к определенному классу (типу данных),
#к ним мы обращаемся через точку
# print(dir(str)) #dir- показывает все методы определенного типы данных

# string = 'hello'
# print(string.upper())#HELLO, переводит все символы в верхний регистр

# string1 ='HELLO'
# print(string.lower())#hello, переводит все символы в нижний регистр

# print('HellO'.swapcase())#hELLo, HELLO, переводит все символы в противположный регистр

# print('hello world'.title())#Переведет все слова в верхний регистр
# print('Hello world'.capitalize())#переводит только первую букву первого слова в верзний регистр, остальные слова остаются неизменными

# print('hello'.center(11,'-'))#---hello---

# print('world'.count("w"))#1,возвращает количество вхождения заданного символа

# print('hello'.startswith('h'))#True, проверяет, начинается ли строка с заданного символа, возварает true или false

# print('hello'.startswith('H'))#False
# print('hello'.endswith('hello'))#True, проверят заканчивается ли строка заданным символом
# print('hello'.endswith('lo'))#True


# .islower()-проверяет, находится ли строка польностью в нижнем регистре
# print('hello, world'.silower())#True
# print('hElLo, worLd'.silower())#False


# # .isupper() - проверяет, находится ли строка польностью в верхнем регистре
# print('hello world'.isupper())#false


# .isdigit()- проверяет состоит ли строка польностью из чисел
# print('1233123131'.isdigit())#True
# print('12331231sfdsd'.isdigit())#False


# # .isalpha()- проверяет состоит ли строка только из букв
# print('hello'.isalpha())#true
# print('hello213'.isalpha())#FALSE


# print('hello123'.isalnum())#True
# print('123'.isalnum())#True
# print('hello'.isalnum())#True


# # .split()-возваразет список который разделилил по заданному разделител/ на отдельные строки
# print('hello, world, my name is nikita'.split())
# #['hello,', 'world,', 'my', 'name', 'is', 'nikita']

# # .join()- соединяет список по указнному разделителю
# print('-'.join(['hello,', 'world,', 'my', 'name', 'is', 'nikita']))
# #hello,-world,-my-name-is-nikita

# .strip()- убивает пробелы слве и справа
# string = '       hello          world          '
# print(string)
# print(string.strip()) #hello      world

# string = 'hello'
# # .lstrip()- убирает все пробелы слева
# # .rstrip()- убивает все пробелы справо

# print(string.lstrip())
# print(string.rsprip())


"==============ИНДЕКСЫ=============="
#Индекс - порядковый номер в посследовательности (символа в строке), (индексация начинается с нуля)

'h e l l o w o r l d'
#0 1 2 3 4 5 6 7 8 9
#               -2 -1

string1 = 'hello world'
print(string1[10])
print(string1[0])
print(string1[-1])


#срез - подстрока нашей строки
print(string1[0:5])#hello
print(string1[0:4])#hell
print(string1[6:12])#world
print(string1[6:])#world


string2 = 'torokul'
print(string2[::-1])#lukorot
print(string2[1:5])#orok


#""==повторить эту тему и на завтра подготовиться на тему циклы(for_loop,if_else)=="






