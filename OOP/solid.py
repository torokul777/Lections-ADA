#SOLID - это аббревиатура, для набора принципов проектирования, созданных для разработки ПО при помощи объектно-ориентированных языков. Принципы SOLID направлены на содействие разработки более простого, надежного и обновляемого кода

# При правильной реализации, это делает ваш код более расширяемым, логичным, и легким для чтения


# S (SRP)
"""
1) Single Responsibility Principle
(Принцип единственной обязанности)
Принцип единой обязанности требует того, чтобы один класс выполнял только одну работу. (Т.е. не надо создавать огромный класс который делает все)
"""

# Before
# class ExportCsv:
#     def __init__(self, raw_data) -> None:
#         self.data = self.prepare(raw_data)

#     def prepare(self, raw_data):
#         result = ''
#         for item in raw_data:
#             new_line = f'{item.get('name')}, {item.get('surname')}\n'
#             result += new_line
#         return result

#     def write_file(self, filename):
#         with open(filename, 'w') as f:
#             f.write(self.data)

# data = [
#   {
#     'name': 'Sherlock',
#     'surname': 'Holmes',
#   },
#   {
#     'name': 'John',
#     'surname': 'Watson',
#   }
# ]
    
# exporter = ExportCsv(data)
# exporter.write_file('out.csv')


# After
class FormatData:
    def __init__(self, raw_data) -> None:
        self.data = raw_data

    def prepare(self):
        result = ''
        for item in self.data:
            new_line = f'{item.get('name')}, {item.get('surname')}\n'
            result += new_line
        return result
    

class FileWriter:
    def __init__(self, filename) -> None:
        self.filename = filename
    
    def write_file(self, data):
        with open(self.filename, 'w') as f:
            f.write(data)

data = [
  {
    'name': 'Sherlock',
    'surname': 'Holmes',
  },
  {
    'name': 'John',
    'surname': 'Watson',
  }
]

formatter = FormatData(data)
formatted_data = formatter.prepare()

writer = FileWriter('out2.csv')
writer.write_file(formatted_data)


"""
Рассмотрим объект "Выпивоха"
для выполнения принципа SRP разделим обзянности на троих

один наливает(PourOperation)
один выпивает (DrinkUpOperation)
один закусывает (TakeBiteOperation)
"""

"""
Плюсы:
1) код стал предельно ясен на каждом уровне
2) код могут писать несколько разработчиков сразу (каждый пишет отдельный элемент)
3) упрощается автоматическое тестирование - чем проще элемент, тем легче его тестировать

Минусы:
Придется создавать больше объектов
"""


"""
2. O
Open/closed principle
Принцип открытости/закрытости

Програмные сущности (классы, модули, функции) должны быть открыты для расширения, но закрыты для модификации
"""

class Discount:
    def __init__(self, customer, price) -> None:
        self.customer = customer
        self.price = price

    def give_discount(self): # скидку для обычных покупателей, одну для других, другую если еще захотим добавить, то придется дописывать логику
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4
    
    """
    чтобы следовать OCP, мы добавим новый класс который будет расширять Discount.
    И в этом новом классе реализуем требуемую логику 
    """

class Discount:
    def __init__(self, customer, price) -> None:
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2
    

class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


"""
L - (LSP)
3. Liskov Substitution Priciple
Принцип подстановки лисков
Главная идея, стоящая за LSP в том, что для любого класса клиент должен иметь возможность использовать любой подкласс базового класса, не замечая разницы между ними, и следовательно, без каких-либо изменений поведения программы при выполнении. Это означает, что клиент полностью изолирован и не подозревает об изменениях в иерархии классов

LSP - это основа хорошего объектно-ориентированного проектирования ПО, потому что он следует одному из базовых принципов ООП - полиморфизму. Речь о том, чтобы создавать правильные иерархии, такие, что классы, производные от базового класса являлись полиморфными для их родителя по отношению к методам их интерфейсов

По простому - родительский класс можно заменить на дочерний не ломая логику. Т. е. наследование должно быть логичным что если в подителе и потомке есть какой то метод, этот метод должен принимать одинаковое количество аргументов, примерно одной и той же логике следовать
"""

# before 

# class Bird:
#     def fly(self):
#         return 'i can fly'
    

# class Penguin(Bird):
#     def fly(self):
#         raise NotImplementedError('Penguins cant fly')
    

# def make_bird_fly(bird: Bird):
#     return bird.fly()

# crow = Bird()
# print(make_bird_fly(crow))


# penguin = Penguin()
# print(make_bird_fly(penguin))



# class Bird:
#     def sound(self):
#         return 'I am a bird'
    

# class FlyingBird(Bird):
#     def fly(self):
#         return 'i can fly'
    

# class Penguin(Bird):
#     def swim(self):
#         return 'i can swim'
    

# def make_bird_fly(bird: Bird):
#     if isinstance(bird, FlyingBird):
#         return bird.fly()
#     return 'This bird cant fly'


# crow = FlyingBird()
# print(make_bird_fly(crow))

# penguin = Penguin()
# print(make_bird_fly(penguin))


"""
4. I - (ISP)
Interface Segregation Principle
Принцип разделения интерфейсов

Создавайте тонкие интерфейсы, которые ориентированы на клиента. Клиенты не должны зависеть от интерфейсов (Или же методов которые не использует), которые они не используют. Этот принцип устраняет недостатки реализации больших интерфейсов

Пример: Если есть интерфейс, который требует реализовать 10 методов, но объекту нужны только 2 из них, то лучше разделить интерфейс на несколько маленьких
"""

# before

# class Worker:
#     def work(self):
#         raise NotImplementedError
    
#     def eat(self):
#         raise NotImplementedError
    

# class Developer(Worker):
#     def work(self):
#         print('writing code')
    
#     def eat(self):
#         print('Eating food')
    

# class Robot(Worker):
#     def work(self):
#         print('Assembling parts')
    
# def manage_worker(worker: Worker):
#     worker.work()
#     worker.eat()


# developer = Developer()
# manage_worker(developer)


# robot = Robot()
# manage_worker(robot)


# after

class Workable:
    def work(self):
        raise NotImplementedError
    

class Eatable:
    def eat(self):
        raise NotImplementedError
    

class Developer(Workable, Eatable):
    def work(self):
        return 'writing code'
    
    def eat(self):
        return 'eating food'
    

class Robot(Workable):
    def work(self):
        return 'Assembling parts'
    

def manage_worker(worker: Workable):
    print(worker.work())

def manage_eater(eater: Eatable):
    print(eater.eat())

developer = Developer()
manage_worker(developer)
manage_eater(developer)

robot = Robot()
manage_worker(robot)


"""
D - (DIP)
Dependency Inversion Principle
(Принцип инверсии зависимостей)

Зависимость должна быть от абстракций, а не от конкретики. Модули верхних уровней не должны зависеть от модулей нижний уровней. Классы верхних и нижних уровней должны зависеть от одних и тех же абстракций. Абстракции не должны зависеть от деталей, детали должны зависеть от абстракций
"""


# before

# class MySQLConnection:
#     def connect(self):
#         return 'Connected to MySQL'
    

# class PasswordReminder:
#     def __init__(self) -> None:
#         self.db_connection = MySQLConnection()

#     def remind(self):
#         return self.db_connection.connect()
    
# reminder = PasswordReminder()
# print(reminder.remind())


# after

# from abc import ABC, abstractmethod


# class DBConnectionInterface(ABC):
#     def connect(self):
#         ...


# class MySQLConnection(DBConnectionInterface):
#     def connect(self):
#         return 'Connected to MySQL'
    

# class PostgreSQLConnection(DBConnectionInterface):
#     def connect(self):
#         return 'Connected to PostgreSQL'
    

# class SQLiteConnection(DBConnectionInterface):
#     def connect(self):
#         return 'connected to SQLite'
    

# class PasswordReminder:
#     def __init__(self, db_connection: DBConnectionInterface) -> None:
#         self.db_connection = db_connection

#     def remind(self):
#         return self.db_connection.connect()
    

# mysql_connection = MySQLConnection()
# postgresql_connection = PostgreSQLConnection()
# sqlite_connection = SQLiteConnection()


# reminder = PasswordReminder(mysql_connection)
# print(reminder.remind())
# reminder2 = PasswordReminder(postgresql_connection)
# print(reminder2.remind())
# reminder3 = PasswordReminder(sqlite_connection)
# print(reminder3.remind())

