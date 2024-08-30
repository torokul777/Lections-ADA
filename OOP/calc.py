# # Создайте класс Animal с атрибутами 'name',  'age' 
# # и метод 'get_age', который возвращает строку 'я {name} 
# # и мой возраст {age}'. Создайте три экземпляра этого класса.
# # class Animal:
# #     def __init__(self,name,age) -> None:
# #         self.name = name
# #         self.age = age
# #     def get_age (self):
# #         return f'{self.name} и его возраст {self.age}'
# # anim1 = Animal('Marat1',age=0)
# # anim2 = Animal('Marat2',age=0)
# # anim3 = Animal('Marat3',age=0)
# # print(f'животное: {anim1.get_age()}')
# # print(f'животное: {anim2.get_age()}')
# # print(f'животное: {anim3.get_age()}')


# # Создайте класс Phone, который содержит атрибуты number, model.
# #  Создайте три экземпляра класса. Добавьте в класс методы: receive_call
# #  принимает один параметр name-имя звонящего. Данный метод выводит 
# # сообщение "Вам звонит {name}'. Метод get_number возвращает номер телефона.
# # class Phone:
# #     def __init__(self,number,model):
# #         self.number = number
# #         self.model = model
    
# #     def receive_call(self,name):
# #         return f'Вам звонит {name}'
    
# #     def get_number(self,model):
# #         return f'номер телевона {model}'
# # num1 = Phone('0559958798','iphnone 11')
# # num2 = Phone('0997987666','iphnone 14')
# # num3 = Phone('0777777777','nokia')

# # print(num1.receive_call('mom'))
# # print(num1.get_number())

# # print(num2.receive_call('sister'))
# # print(num2.get_number())

# # print(num3.receive_call('brother'))
# # print(num3.get_number())


# # class Phone:
# #     def __init__(self, number, model):
# #         self.number = number
# #         self.model = model
    
# #     def receive_call(self, name):
# #         return f'Вам звонит {name}'
    
# #     def get_number(self):
# #         return self.number

# # # Создание экземпляров класса Phone
# # num1 = Phone('0559958798', 'iPhone 11')
# # num2 = Phone('0997987666', 'iPhone 14')
# # num3 = Phone('0777777777', 'Nokia')

# # # Примеры использования методов
# # print(num1.receive_call('mom')) 
# # print(f'номер:{num1.get_number()}')         

# # print(num2.receive_call('sister'))
# # print(f'номер:{num2.get_number()}')          

# # print(num3.receive_call('brother'))
# # print(f'номер:{num3.get_number()}')            




# # Создайте класс Car, который имеет аттрибуты модель и макс. скорость. 
# # Создайте метод 'upgrade', который будет увеличивать макс. 
# # скорость на один км/ч.
# # class Car:
# #     def __init__(self,model,max_speed):
# #         self.model = model
# #         self.max_speed = max_speed
# #     def upgrade(self):
# #         self.max_speed +=1

# # car1 = Car('bmw m4 g80 cs',399)
# # car2 = Car('bmw m5 f 90',350)
# # car3 = Car('jiguli',77)

# # print(car1.max_speed)
# # car1.upgrade()
# # print(car1.max_speed)

# # print(car2.max_speed)
# # car2.upgrade()
# # print(car2.upgrade)

# # print(car3.max_speed)
# # car3.upgrade()
# # print(car3.max_speed)


# class Car:
#     def __init__(self, model, max_speed):
#         self.model = model
#         self.max_speed = max_speed

#     def upgrade(self):
#         self.max_speed += 1


# car1 = Car('BMW M4 G80 CS', 399)
# car2 = Car('BMW M5 F90', 350)
# car3 = Car('Jiguli', 77)


# print(f'скорость до:{car1.max_speed}')  
# car1.upgrade()
# print(f'скорость после:{car1.max_speed}')  

# print(f'скорость до:{car2.max_speed}')  
# car2.upgrade()
# print(f'скорость после:{car2.max_speed}')  

# print(f'скорость до:{car3.max_speed}')  
# car3.upgrade()
# print(f'скорость после:{car3.max_speed}')  


# Нужно создать программу для банкомата, 
# который принимает деньги и выдает деньги.
#  Создайте класс Банкомат с методами: 

# Чтобы банкомат принимал деньги
# Чтобы банкомат выдавал деньги
# Чтобы банкомат показывал остаток денег
# # class Bankomat:
#     def __init__(self):
#         self.balance = 0  # Изначально баланс равен 0

#     def deposit(self, amount):
#         """
#         Метод для пополнения баланса банкомата.
#         :param amount: Сумма для пополнения (должна быть положительным числом)
#         """
#         if amount > 0:
#             self.balance += amount
#             print(f"Баланс пополнен на {amount} единиц. Текущий баланс: {self.balance}")
#         else:
#             print("Сумма пополнения должна быть положительной.")

#     def withdraw(self, amount):
#         """
#         Метод для снятия денег с баланса банкомата.
#         :param amount: Сумма для снятия (должна быть положительным числом и не превышать текущий баланс)
#         """
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Снято {amount} единиц. Текущий баланс: {self.balance}")
#             else:
#                 print("Недостаточно средств для выполнения операции.")
#         else:
#             print("Сумма снятия должна быть положительной.")

#     def check_balance(self):
#         """
#         Метод для отображения текущего баланса.
#         """
#         print(f"Текущий баланс: {self.balance}")

# # Пример использования
# if __name__ == "__main__":
#     atm = Bankomat()

#     atm.deposit(1000)  # Пополнение счета на 1000 единиц
#     atm.check_balance()  # Проверка баланса

#     atm.withdraw(500)  # Снятие 500 единиц
#     atm.check_balance()  # Проверка баланса

#     atm.deposit(-100)  # Пополнение с отрицательной суммой (ошибка)
#     atm.withdraw(600)  # Снятие суммы больше текущего баланса (ошибка)
'===================================================================='
# class Bankomat:
#     def __init__(self) -> None:
#         self.balance = 0
    
#     def deposit(self,sum):
#         if sum > 0:
#             self.balance += sum
#         else:
#             return 'Сумма не может быть меньше нуля'
#         return f'на вашем счету - {self.balance} сом '
    
#     def withdraw(self,amount):
#         if amount > self.balance:
#             return 'На вашем счету не достатончно средств'
#         self.balance -=amount
#         f'на вашем счету - {self.balance} сом '
    
#     def show_balance(self):
#         return f'на вашем счету - {self.balance} сом'

# obj1 = Bankomat()
# print(obj1.show_balance())
# print(obj1.deposit(100000))
# print(obj1.withdraw(10))
        
# Создайте класс Song с атрибутами author, title и year.
#  Напишите методы showauthor, showtitle и show_year,
# которые возвращают строки с информацией о песне. 
# Создайте объект этого класса и выведите информацию о песне, используя методы.
# class Song:
    # def __init__(self,author:str,title:str,year:int) -> None:
    #     self.author = author
    #     self.title = title
    #     self.year = year
    
    # def show_author(self):
    #     return f'Автор этой песни {self.author}'
    
    # def show_title(self):
    #     return f'Название песни {self.title}'
    
    # def show_year(self):
    #     return f'Год выпуска песни {self.year}'

# obj1 = Song('Sam Smith','Fire in fire',2022)
# print(obj1.show_author())
# print(obj1.show_title())
# print(obj1.show_year())



# Создайте класс Taxi с атрибутами name, cost и cost_km. 
# Напишите метод get_total_cost, который принимает расстояние 
# в километрах и возвращает общую стоимость поездки. 
# Создайте несколько объектов этого класса и выведите стоимость 
# поездки для каждого из них.
# class Taxi:
#     def __init__(self,name:str, cost:float, cost_km : float):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#     def get_total_cost(self, km:float):
#         total_cost = self.cost * km * self.cost_km
#         return f'Такси : {self.name}, стоимость поездки : {total_cost} сом'

# obj1 = Taxi('Yandex',15,7)
# obj2 = Taxi('Namba',10,5)

# print(obj1.get_total_cost(10))
# print(obj2.get_total_cost(100))


# Создайте класс Phone с атрибутами name, last_name и phone. 
# Напишите метод get_info, который выводит информацию о контакте. 
# Создайте объект этого класса и выведите информацию о контакте.
# class Phone:
#     def __init__(self,name,last_name,phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'
    
# contact = Phone('Torokul','Zhanyshbekov','077777777777')
# print(contact.get_info())

# Создайте класс Salary с атрибутом класса percent
#  (по умолчанию 8). Напишите метод __init, который
#  инициализирует атрибуты экземпляра salary и experience. 
# Напишите метод count_percent, который рассчитывает налог
#  на зарплату за весь период работы. Создайте объект этого 
# класса и выведите рассчитанный налог.
class Salary:
    percent = 8
    def __init__(self,salary,experience):
        self.salary = salary
        self.experience = experience
    def count_percent(self):
        month_tax = self.salary /100 * self.percent
        res = self.experience * month_tax
        return f'Сумма налога за весь опыт работы: {res}'

obj1 = Salary(100000,10)
print (obj1.count_percent())