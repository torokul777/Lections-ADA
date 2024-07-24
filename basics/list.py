"===========================List=============================="
#Списки - это изменяемый индексируемый упорядочный итерируемый тип данных который 
# предназначен для хранения любых данных в определенном порядке 


# list_ = [1, 2, 3, 'hello', [1, 2, 3], [[[1, 2, 3]]], None, True ]
# print(list_[1]) # 2
# print(list_[3][-1]) # o
# print(list_[4][2]) #3


# new_list = list('Hello , World!')
# print(new_list) #['H', 'e', 'l', 'l', 'o', ' ', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# range()- принемает 3 аргумента, первый начало диапозона, 2-конец 3-шаг


'========================Методы списков==========================='
#.append()-добавляет элемент в конец списка

# list_= ['hello',22,26]
# list_.append(1)
# list_.append(1)
# list_.append(1)
# print(list_) #[1, 1, 1]
# list_.append('hello')
# print(list_)

#.pop()-он удаляет элемент из списка по индексу и результатом метода 
# будет удаленный элемент(метод возвращает удаленный элемент),
# если не указать индекс удалит с конца

# popped_el = list_.pop(1)
# print(popped_el)
# print(list_)
# popped_el = list_.pop()
# # print(popped_el)


#remove()-удаляет элемент из списка по значению
# list2 = ['asya', 'bad', 'best', 'beautiful','stupid' ]
# list2.remove('bad')
# list2.remove('stupid')
# print(list2)

# #.count()-считает количество принятого элемента в списке
# list2.count()
# print(list2)

# list3 = ['hello','hello','hello']
# print(list3.count('hello'))


#.index ()- возвращает индекс первого вхождения принятого элемента
# list3 = ['hello',1,2,3,4,'hello']
# print(list3.index(1))#1

#.insert()-добавляет элемент во список по индексу
# list3 = ['hello','hello','hello',1,2,3]
# list3.insert(1,'world')
# print(list3)

# .extend() - добавляет элементы принятого списка в первый списоr изменяя его

# list3 = ['hello','hello','hello',1,4,100,None]
# list4= [1,2,3,4,5,{'a':123}]
# list3.extend(list4)
# print(list3) #['hello', 'hello', 'hello', 1, 4, 100, None, 1, 2, 3, 4, 5, {'a': 123}]

#.reverse()- изменяет список, раставляя его элементы в обратном порядке
# list3.reverse()
# print(list3)

# .sort()-сортирует список, состоящий из элементов в одного типа данных
# list3.sort()
# print(list3)

list5 = [1,2,3,4,4,5,1000,211,5754783474376878534]

list5.sort()
print(list5)

# list5 = ['a','b', 'A', 'B','hello']
# list5.sort()
# print(list5)

#.clear()-удаляет все элементы
# list5 = [1,2,3,4,4,5,1000,211,5754783474376878534]
# list5.clear()
# print(list5)#[]

# len() - считает кол-во элементов в посследовательности
list1 = [1, 2, 3, 4, 5, 6, 7, 8, [1,2,3]]
print(len(list1)) 
#множественное присваивание
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

a, b = [1,22]
print(a)
print(b)

name,age,city = ['nikita', 5,'bishkek']
print(name)
print(age)
print(city)





