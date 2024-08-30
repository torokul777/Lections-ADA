'=====================================Полиморфизм======================'
# Полиморфизм - принцип ООП в котором в разных классах называются разными но реализация разная(один интерфейс - много реазлизаций)

# class Dog:
#     def speak(self):
#         print('Гав-Гав')

# class cat:
#     def speak(self):
#         print('Мяу')


# class Frog:
#     def speak(self):
#         print('Ква-Ква')

# obj = [Frog(),cat(),Dog(),cat(),Frog(),Dog()]
# for obj in obj:
#     obj.speak()


# # __add__ (+)
# print(5+5) #10
# print('5'+'5') #55 str
# print([1,2,3]+[4,5,6]) #[1,2,3,4,5,6]

# a=[1,2,3,4]
# b=[4,5,6]
# print(a.__add__(b)) #[1, 2, 3, 4, 4, 5, 6]

# #__len__
# print(len('abc')) #3
# print(len([1,2,3])) #1
# print(len([[1,2,3],[4,5,6]])) #2


# while True:
#     print('Марат лох')



# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет меня зовут {self.name} {self.last_name}'

# class Employee(Person):
#     def __init__(self, name, last_name,work,experience):
#         super().__init__(name, last_name)
#         self.work = work
#         self.experience = experience

#     def get_info(self):
#         return f'Привет меня зовут {self.name} {self.last_name}, я работаю в компании {self.work}, и мой опыт работы {self.experience}'
    
# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
    
#     def get_info(self):
#         return f'Привет меня зовут {self.name} {self.last_name}, я учусь в {self.university}, на {self.course} курсе '
    

# def get_human_info(human):
#     print(human.get_info())


# person = Person('Torokul', 'Zhanyshbekov')
# employee = Employee('Torokul','Zhanyshbekov', 'IT', '3 месяц')
# student = Student('Torokul','Znahyshbekov', 'ICT университете', 0)

# get_human_info(person)
# get_human_info(employee)
# get_human_info(student)





# Создайте классы OS, Windows, MacOS и Linux. В классе OS должен 
# быть аттрибут version, пользователь сам будет указывать версию ОС.
#  Классы Windows, MacOS и Linux должны наследоваться от OS и реализовать метод 
# copy, который возвращает строку с командой копирования для соответствующей ОС.

# горячая клавиша для Mac Os  command + c
# горячая клавиша для Windows ctrl + c
# горячая клавиша для Linux ctrl + shift + c

# class OS:
#     def __init__(self,version):
#         self.version = version
    
#     def copy(self):
#         ...

# class Windows(OS):
#     def copy(self):
#         return 'горячая клавиша для Windows ctrl + c'

# class MacOS(OS):
#     def copy(self):
#         return 'горячая клавиша для Mac Os  command + c'

# class Linux(OS):
#     def copy(self):
#         return 'горячая клавиша для Linux ctrl + shift + c'


# windows = Windows('windows 11')
# macos = MacOS('macos 2019')
# linux = Linux('linux 2022')
# print(windows.copy())
# print(macos.copy())
# print(linux.copy())







'=========================homework========================='

# # Задачи по наследованию и полиморфизму

# 1) Создайте класс Phone, который наследует класс Device.

# Должны быть атрибуты brand, model, pixel.
'==============================exercise1=================================='
# class Phone:
#     def __init__(self) -> None:
#         pass
# class Device(Phone):
#     def __init__(self,brand,model,pixel):
#         self.model = model
#         self.brand = brand
#         self.pixel = pixel

# obj1 = Device('ios','iphone','1080MP')
# print(f'model: {obj1.model}, brand: {obj1.brand}, pixel: {obj1.pixel}')

'==============================exercise2=================================='
# Создайте класс Car с атрибутами max_speed и weight. 
# Создайте метод, который посчитает время прохождения 100 метров.
#  Формула для нахождения max_speed / 100 * 3.14. Создайте два экземпляра.
# class Car:
#     def __init__(self,max_speed,weight):
#         self.max_speed = max_speed
#         self.weight = weight
    
#     def sto_metrov(self):
#         return self.max_speed / 100 * 3.14

# toro_car1 = Car(350,1760)
# toro_car2 = Car(299,1200)
# print(f'car1: {toro_car1.sto_metrov()}')
# print(f'car2: {toro_car2.sto_metrov()}')

'==============================exercise3=================================='
# Создайте класс Person с атрибутами name, age. Создайте метод eat,
#  который принимает обязательный аргумент food, данный метод выводит
#  сообщение 'Я кушаю {food}'. Определить класс Reader, хранящий информацию
#  о читателе библиотеки. Атрибуты: номер читательского билета, телефон. 
# Создайте два метода take_book, return_book, которые принимают аргумент
#  book_name. take_book выводит сообщение '{name} взял {book_name}.
# return_book выводит сообщение '{name} вернул {book_name}.
# Переопределите метод eat в Person, так чтобы он выводил сообщение:
# 'Я {name} и я не кушаю {food}, а предпочитаю книги' 


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def eat(self,food):
#         return f'Я кушаю {food}'

# class Reader(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
    
#     def take_book(self,book_name):
#         return f'{self.name} взвял {book_name}'
    
#     def return_book(self,book_name):
#         return f'{self.name} вернул {book_name}'

#     def eat(self,food):
#         return f'Я {self.name}, и я не кушаю {food}, а предпочитаю книги'
    
# person = Person('Torokul',14)
# reader = Reader('Nikita', 21)

# print(person.eat('Суши'))
# print(reader.eat('Суши'))



'==============================exercise 4=================================='
#  Создать класс Student, Aspirant. Student содержит атрибуты 
# name, group, average_mark(средняя оценка). Создайте метод get_scholarship, 
# который посчитает стипендию за счёт средней оценки. Если средняя оценка
#  равна 5 то метод возвращает 2000 сом, иначе 1500 сом. Класс Aspirant должен
#  наследовать класс Student. В Aspirant переопределите метод get_scholarship,
#  так чтоб если оценка 5 то возвращает 3000 сом, иначе 2500 сом. 


# class Student:
#     def __init__(self, name, group, average_mark):
#         self.name = name
#         self.group = group
#         self.average_mark = average_mark
    
#     def get_scholarship(self):
#         return '2000 som' if self.average_mark == 5 else '1500 som'
    
# class Aspirant(Student):
#     def get_scholarship(self):
#         return '3000 som' if self.average_mark == 5 else '2500'
    
# student = Student('Torokul','Python',4.5)
# aspirant = Aspirant('Nikita','Python',5)

# print(student.get_scholarship())
# print(aspirant.get_scholarship())

'==============================exercise 4=================================='
# Создайте базовый класс Money у которого есть два аттрибута 
# экземпляра класса (country, symbol) и классы Dollar и Euro,
#  которые наследуются от Money, у этих классов должен быть аттрибут rate,
#  в котором будет храниться курс валют. Эти классы должны иметь метод exchange, 
# который конвертирует сумму в сомы и возвращает строку с результатом 
# "$ {amount} равен {som} сомам".
# "€ {amount} равен {som} сомам"  

# class Money:
#     def __init__(self, country, symbol):
#         self.country =  country
#         self.symbol = symbol

# class Dollar(Money):
#     def __init__(self, rate):
#         super().__init__('USA','$')
#         self.rate = rate
    
#     def exchange(self,amount):
#         som = amount * self.rate
#         return f'$ {amount} равен {som} сомам'

# class Euro(Money):
#     def __init__(self, rate):
#         super().__init__('Europe','€')
#         self.rate = rate
    
#     def exchange(self, amount):
#         som = amount * self.rate
#         return f'€ {amount} равен {som} сомам'

# dollar = Dollar(85)
# euro = Euro(90)

# print(dollar.exchange(250))
# print(euro.exchange(400))



# Создайте класс Person с атрибутами name, age.
#  Создайте метод eat, который принимает обязательный аргумент food, 
# данный метод выводит сообщение 'Я кушаю {food}'.
#  Определить класс Reader, хранящий информацию о читателе библиотеки.
#  Атрибуты: номер читательского билета, телефон.
#  Создайте два метода take_book, return_book, 
# которые принимают аргумент book_name. 
# take_book выводит сообщение '{name} взял {book_name}.
# return_book выводит сообщение '{name} вернул {book_name}.
# Переопределите метод eat в Person, так чтобы он выводил сообщение:
# 'Я {name} и я не кушаю {food}, а предпочитаю книги' 


# class Person:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     def __add__(self, other):
#         return self.age + other.age

#     def __mul__(self, other):
        
#         return self.age * other
        

#     # def __str__(self):
#     #     return f"{self.name} {self.last_name}{self.age}"


# akjol = Person('akjol', 'cool', -12)
# torokul = Person('Torokul', 'Zhanyshbekov', -12)


# # print(akjol * 2)
# # print(torokul * 2) 

# print(akjol + torokul)  

# Создайте класс Vector2D, представляющий 2D-вектор. Реализуйте следующие магические методы:

# __init__: для инициализации вектора.
# __add__: для сложения двух векторов.
# __sub__: для вычитания одного вектора из другого.
# __mul__: для умножения вектора на скаляр.
# __repr__: для строкового представления вектора.

# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self):
#         return self.x + self.y
    
#     def __sub__(self):
#         return self.x - self.y
    
#     def __mul__(self):
#         return self.x * self.y
    
#     def __repr__(self):
#         return self.x and self.y
    
# age = Vector2D(2,2)
# print(age.__add__())
# print(age.__sub__())
# print(age.__mul__())
# print(age.__repr__())


class Operators:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def __add__(self):
        return self.num1 + self.num2
    
    def __sub__(self):
        return self.num1 - self.num2
    
    def __mul__(self):
        return self.num1 * self.num2
    
    def __div__(self):
        return self.num1 / self.num2
    
    def round_div(self):
        return self.num1 // self.num2
    
numbers = Operators(5,5)
print(numbers.__add__())
print(numbers.__sub__())
print(numbers.__mul__())
print(numbers.__div__())
print(numbers.round_div())
