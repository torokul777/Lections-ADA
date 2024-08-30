# class methods - методы, которые принимает первым аргументом cls(ссылка на класс)
# Нужны они для создания обьектов или изменения аттрибутов класса. для создания методы класса нужно задекорировать его в класс class method

# class B:
#     @classmethod
#     def class_method(cls):
#         print('класс метод')
#         print('первый аргумент', cls)
#
#
# obj1 = B()
# B.class_method()
# obj1.class_method()
#
# class C:
#     counter = 0
#
#     def __init__(self):
#         self._inc_counter()
#
#         def __del__(self):
#             self._dec_counter()
#             del self
#
#     @classmethod
#     def _inc_counter(cls):
#         cls.counter +=1
#
#     @classmethod
#     def _dec_counter(cls):
#         cls.counter +=1
#
# obj1 = C()
# obj2 = C()
# obj3 = C()
# print(C.counter)



# static methods - просто функции внутри класса, которые не взаимодействуют ни с классом ни с обьектом
# Находятся они внутри класса лишь потому что они используются внутри класса и вне они в целом бессполезны
# Чтобы создать static метод нужно его задекорировать static method

class D:
    @staticmethod
    def hello(string):
        print(string)

obj_d = D()
obj_d.hello('hello world')
D.hello('hello world')

class CyLinder:
    def __init__(self,diametr,height):
        self.di = diametr
        self.h = height
        self.area = self.get_area(diametr,height)

    @staticmethod
    def get_area(di,h):
            from math import pi
            circle = pi * di ** 2 / 4
            side = pi * di * h
            area = circle * 2 + side
            return round(area, 2)

cylinder1 = CyLinder(4,10)
print(cylinder1.area)