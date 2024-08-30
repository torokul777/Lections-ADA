# # Насследования - принцип ООП в котором мы можем унаследовать переопределить
# #  и использовать в дочернем классе все аттрибуты и методы родительского класса
# class A:
#     def method(self):
#         print('Метод в классе А')
# obj1 = A()
# obj1.method()

# class B(A):
#     '''
#     Насследовали все методы и аттрибуты класса  А
#     '''
# obj2 = B()
# obj2.method()

# class C(A):
#     '''
#     Насследовали все методы и аттрибуты у класса  А, и переопределили метод method()
#     '''

#     def method(self):
#         print('Метод в кклассе C')

# obj3 = C()
# obj3.method()

# class A:
#     x = 'x in A'
#     y = 'y in A'

# class B(A):
#     x = 'x in B'

# print(A.x)
# print(B.x)

'''
Виды насследований
1) одиночное насследовние(когда мы насследумемся в дочернем классе от 1 класса)
2) множественное насследование(когда мы насследуемся в дочернем классе от нескольких классов)
3) Многоуровневое насследование (когда мы насследуемся от класса у которого есть родитель)
4) иерахрхическое исследование (когда от отдного родителся много дочерных классов)
5) гибридное насследовние (когда используется несколько видов насследования)
'''

'====================================Множественное наследование==========================='
# class A:
#     a = 'a'

# class B:
#     b = 'b'

# class C(A,B):
#     c = 'с'
#     '''
#     Насоледовали все аттрибуты классов А и B
#     '''

# obj1 = C()
# print(obj1.a)
# print(obj1.b)
# print(obj1.c)

# print('a')
# print('b')
# print('c')

# class A():
#     def method(self):
#         print('Метод в классе A')

# class B():
#     def method(self):
#         print('Метод в классе B')

# class C(A,B):
#     pass

# obj_c = C()
# obj_c.method() # Метод в классе А


# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass
# class Class2(Class1):
#     def third(self):
#         ...
#     def fourth(self):
#         ...
# obj1 = Class2()
# obj1.first()
# obj1.second()
# obj1.third()
# obj1.fourth


# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj1 = B()
# obj1.method1()



# class MyDict(dict):
#     def get(self,*args):
#         value = super().get(*args)

#         if value:
#             return value
#         else:
#             return 'Are you kidding?'
        
# obj_dict = MyDict({'some_title':2})
# print(obj_dict.get('some_title'))



# class MyString(str):
#     def append(self,extra_string):
#         self.mutable_string = self + extra_string
    
#     def pop(self):
#         last_char = self.mutable_string[-1]
#         self.mutable_string = self.mutable_string[:-1]
        
#         return last_char
#     def __str__(self) -> str:
#         return self.mutable_string

# obj = MyString('hello')
# obj.append('hello')
# print(obj.pop())
# print(obj)



# class Person:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f'name: {self.name}, age: {self.age}')
# class Student(Person):
#     def __init__(self, name, age,faculty) -> None:
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print(f'name: {self.name}, age: {self.age},faculty: {self.faculty}')
    
# obj1 = Student('Torokul',14, 'computer science')
# obj1.display()
# obj1.display_student()


# class ContactList(list):
#     def serch_by_name(self,name):
#         res = [contact for contact in self if name.lower() in contact.lower() ]

#         return res
# list1 = ['Olya','Ivan','NiKIta','Vasya','Nikita','nikita']
# obj1 = ContactList(list1)

# print(obj1.serch_by_name('NIKITA'))


# from datetime import datetime
# class SmartPhones:
#     def __init__(self,name,color,memory) -> None:
#         self.name = name
#         self.memory = memory
#         self.color = color
#         self.battery = 0
#     def charge(self,power):
#         self.battery += power
#     def __str__(self) -> str:
#         return f'{self.name}, gigabayt:{self.memory}, color:{self.color}'



# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory,ios):
#         super().__init__(name, color, memory)
#         self.ios = ios
#     def send_imesssge(self,message):
#         return f'sending {message} from {self}'


# class SamSung(SmartPhones):
#     def __init__(self, name, color, memory,android) -> None:
#         super().__init__(name, color, memory)
#         self.android = android
#     def show_time(self):
#         return datetime.now().time()
    
# phone = SmartPhones('nokia','blue',16)
# print(phone)   
# print(phone.battery)
# phone.charge(100)
# print(phone.battery)

# Iphone15 = Iphone('Iphone15','gray',512,'18.0')
# print(Iphone15)
# print(Iphone15.send_imesssge('hello'))

# samsung21 = SamSung('Samsung21','blue',128,'Oreo')
# print(samsung21.show_time())


# class CustomError(Exception):
#     pass
# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(string):
#     if not string.isupper():
#         raise capitals_error
#     else:
#         f'ВСК ОТЛИЧНО! {string}'

# print(check_letters('HELLO'))
from abc import ABC, abstractmethod

class OS(ABC):
    def __init__(self, version):
        self.version = version
    
    @abstractmethod
    def copy(self):
        pass

class Windows(OS):
    def copy(self):
        return "Горячая клавиша для Windows: ctrl + c"

class MacOS(OS):
    def copy(self):
        return "Горячая клавиша для Mac OS: command + c"

class Linux(OS):
    def copy(self):
        return "Горячая клавиша для Linux: ctrl + shift + c"

# Примеры использования
windows = Windows("10")
macos = MacOS("Monterey")
linux = Linux("Ubuntu 22.04")

# Печать команд копирования для каждой ОС
print(windows.copy())  # Вывод: Горячая клавиша для Windows: ctrl + c
print(macos.copy())   # Вывод: Горячая клавиша для Mac OS: command + c
print(linux.copy())   # Вывод: Горячая клавиша для Linux: ctrl + shift + c




























