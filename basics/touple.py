"=================================Tuple================================="
#Кортеж(tuple)- неизменяемый индексируемый упорядочный тип данных предназначенный для хранения любых данных
# в определенном порядке (в целом не отличается от списков 
# просто он не изменяемый поэтому занимает меньше памяти)

tuple1 = (1,2,3)
print(type(tuple1)) #<class tuple>
typle2 = (5) #<class int> запятые
print(type(typle2))

tuple2 = tuple('Hello')
print(tuple2)#('H', 'e', 'l', 'l', 'o')
tuple3 = 1,2,3
print(tuple3)

tuple4 = (1,2,3,[1,2,3])
tuple4[-1].append('Hello')
print(tuple4) #(1, 2, 3, [1, 2, 3, 'Hello'])

tuple6 = tuple([1,2,3, 'hello',1223,5488,34877843])
print(type(tuple6)) #<class tuple>

"==========================Методы Tuple============================"
#.count()- считает ко-во принятого элемента в кортежа в (tuple)
tuple_ = (1, 1, 1, 1, 1, 1, 1,False,True)
print(tuple_.count(1))

tuple7 = ('hello', 'hello', 'hello')
print(tuple7.count('hello'))

# .index()= возвращает индекс первого вхождения принятого элемента
tuple8 = (1,2,1,1,1,1,'hello',100)
print(tuple8.index(100)) #7


