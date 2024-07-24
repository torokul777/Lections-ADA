'==================SET=================='
#set(множество) - изменяемый итерируемый индексируемый ти данных который предназначен для
#хранения уникальных значений Множества могут хранить в себе только не изменяемый типы данных
#Усли в используете tuple то в них тоже должны быть неизменяемые типы данных


# set_ = {1,2,3,4}
# set2 = {1,1,1,1,1,2,2,2,2,2,3,3,3,3,5,5,5,5}
# print(set2) #{1, 2, 3, 5}

# set_ = {(1,2,3),3}
# print(set_) #{3, (1, 2, 3)}

"=====================Методы set==========================="
#print(dir(set_))
# .add() - Добавляет элементы в set
# set1 = {1,2,3,4,5}
# set1.add(6)
# set1.add(7)
# set1.add(True)
# print(set1) #{1, 2, 3, 4, 5, 6, 7}

# .pop() - он удаляет случайный элемент из set (но есть принцип fifo)
# set2 = {1,2,3}
# popped = set2.pop()
# print(set2, popped) #{2, 3} 1

# .remove() - удаляет элемент из set по значению
# set_ = {1, 2, 3}
# set_.remove(3)
# print(set_) # {1, 2}
# set1 = {}
# set1.remove()
# print(set1) #'dict' object has no attribute 'remove'



#.difference() (-)
# set1 = {1,2,3}
# set2 = {3,4,5}
# print( set1 - set2) #{1, 2}
# print(set2 - set1) #{4, 5}

# # .symmetric_difference()- 
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.symmetric_difference(set2)) #{1, 2, 4, 5}

# .intersection() (&)
# set1 = {1,2,3,4,5,6,7,8}
# set2 = {4,5,6,7,8,9,10}
# print(set1.intersection(set2))
# print(set1 & set2)
# {4, 5, 6, 7, 8}
# {4, 5, 6, 7, 8}


# .clear()
# set1 = {1,2,3,4}
# set1.clear()
# print(set1) #set()

# .union() - возвращает множества которое содержит все элементы из всез переданныз множест

# set1 = {1,2,3}
# set2 = {True, False, (1,2,3) }
# set3 = {4,5,6,7}

# result = set1.union(set2,set3)
# print(result)
#{False, 1, 2, 3, 4, 5, 6, 7, (1, 2, 3)}


# .issubset() - проверяет является ли одно множество подмножеством другого
# (если все элементы одного множества присутствуют в лругом то вернется True)

# set1 = {1,2}
# set2 = {1,2,3,4,5}
# print(set1.issubset(set2)) #True
# print(set2.issubset(set1)) #False
# issuperset() - проверяет является ли множество надмножеством другого множества

# set1 = {1,2}
# set2 = {1,2,3,4,5}
# print(set1.issuperset(set2))# False работает наоборот
# print(set2.issuperset(set1))#True обратный метод от сабсет

# .isdisjoint() - проверяет не имеет ли два множества общих элементов
# возвращает True либо False 

# set1 = {1,2,3,4,5}
# set2 = {6,7,8,9,10}
# print(set1.isdisjoint(set2))
#True

# .discars() - удаояет элемент по указаннному значению если элемент отстутсвует то 
#ошибка не вызвывается

# set1 = {1,2,3,4}
# set1.discard(3)
# print(set1) #{1, 2, 4}
# d1 = { 'a': 100, 'b' : 200, 'c' : 300}
# d2 = {'a': 300, 'b': 200, 'd':400}
'===============1============='
# print(d1["b"] == d2["b"])
#True
'=============2================'

# person = {"name": "Kelly", "age": 25, "city": "New york"}
# print(person['age'])
'===================================3========================'

# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# result = (sample_set.union(sample_list))
# print(result)
'========4==============================='
# set1 = {6, 4, 2, 5, 7, 8, 10, 9}
# set1.remove(7)
# print(set1)
"========================5======================="
# set1 = {'Python', 'it', 'c++', 'java', 'programming'}

# set2 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set1.intersection(set2))

'=====================6========================='

# set2 = {'Python', 'it', 'c++', 'java', 'programming'}
# set3 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set3.difference(set2))

"===========================7===================="

# set_ = {1,2,3,4,5}
# set_.add(6)
# popped = set_.pop()
# print(set_, popped)
# print(popped)
'============================8======================='
#Dictionary1 
# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu['besh_barmak'] = 130
# menu['lagman'] = 135
# popped = menu.pop("borsh")
# print(menu)


"=============================9======================="
# menu = {'manty': 200, 'plov': 150, 'lagman': 135, 'besh_barmak': 130}
# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta'] 
# print(menu)

"===============================10======================"
# set1 = {'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'}
# set2 = {'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'}
# print(set1.intersection(set2))
"==================================12======================"
# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шляпа')
# suitcase.append('обувь')
# suitcase.append('кепка')
# popped = suitcase.pop(3)
# print(popped)
# print(suitcase)