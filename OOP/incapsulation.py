# Инкапсуляция (Incapsulation)
'''
Существует 2 оперделения: 
    1) Инкапусляция - это принцип ООП который заключается в том что все методы 
и аттрибуты должны быть заключены в 1 класс(капсулу)
    2) Инкапсуляция - это наличие 3 видов доступа:
- public - публичный это 
-proctected - защищенный
- privаte  - приватный
public - обычные методы и аттрибуты которые я могу использовать как внутри  и так и вне класса
_protected  - методы и аттрибуты которык я не могу использовать и изменять вне класса
__private - методы и аттрибуты которые я не могу использовать и изменять вне класса
            + и они насследуются в других классах можно обращаться нелегально(obj._Person__secret)
Для легального обращения к приватным и защищенным аттрибутам существуют getter и setter 
getter - получает аттрибут
setter - изменяет его
Синтаксис:
    @property 
    def password(self):
        return self.__password

    @password.setter(self,new_password):
        self.__pasword = new_password
!!! Setter нельзя использовать без getter 

'''

# class Person:
#     __sectet = 'I am gay'
#     def __init__(self,name:str,age:int,last_name:str,bank_code:str):
#         self.age = age
#         self.name = name
#         self.last_name = last_name
#         self._bank_code = bank_code #защищенный атрибут: _
#     def __private(self):
#         ...
# class Peson2(Person):
#     ...

# # print(p._Person__secret)




# p = Person('Torokul',14,'Zhanyshbekov',6543)

# class User:
#     def __init__(self,name,password):
#         self.name = name
#         self.__password = password
    
#     def get_password(self): #getter
#         return self.__password
    
#     @property # Декоратор
#     def password(self):
#         return self.__password
#     def set_password(self,new_password: str): #setter
#         self.__password = new_password
    
#     @password.setter
#     def password(self, new_password):
#         self.__password = new_password
# john = User('Torokul','Marat loh')
# # password = john.get_password()
# # john.set_password('Torokul loh')
# # password = john.get_password()
# # print(password)

# print(john.password)
# john.password = 'test'
# print(john.password)


# Создайте миксин RadioMixin с методом play_music
# который принимает название песни и выводит его название на экран
# Используйте этот миксин в классаз Auto Boat и Amphbian Саоздайте
# обьекты этих классов
class Clock:
    from datetime import datetime


    now = datetime.now()
    def current_time(self,time):
        self.time = time
        return f'Текущее время: {self.now}'
class Alarm(Clock):
    def off(self):
        return 'Будильник выключен'

class AlarmClock(Alarm):
    def alarm_on(self):
        return 'Будильник включен'

alarmclock = AlarmClock()
print(alarmclock.current_time())
print(alarmclock.alarm_on())
