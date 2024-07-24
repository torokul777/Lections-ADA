"===================Логические операторы====================="
# логические операторы - выражения, которые возвращают True, если выражение верное, False - если выражение не верное

"====Равенство===="
5 == 5 # сравнения, в данном выражении вернется True
# name = 5 - Оператор присваивания 
2 == 5 # False

"====Не равенство===="
4 != 5 # True
5 != 5 # False

"====Больше===="
4 > 4 # False
10 > 5 # True

"====Меньше===="
1 < 4 # True
10 < 5 # False


"====Больше или равно===="
10 >= 4 # True
4 >= 4 # True
1 > 10 # False

"====Меньше или равно===="
10 <= 20 # True
10 <= 10 # True
20 <= 10 # False

print('5' == 5)
print('Hello' == 'hello')

"==== and, or, not ====="
#and - и, Возваращает True если оба условия верны, False - если хоть одно из них неверно

#or - или, Вернет True, если хоть одно условие верно, False - если оба условия неверны

#not - не

a = 5
b = 3

print(a == b and a > b) # False
print(a == b or a > b) # True

print(not True)
print(not False)

print(not a == 5)

"===== Boolean Type ===="

print(bool(1))
print(bool(0))
print(bool(-122))

print(bool('hello'))
print(bool(' '))
print(bool(''))

"==== is ===="
a = 5
b = 5
print(a == b)
print(a is b)

"====NoneType===="
# None - неизменяемый тип данных с одним значением None, который используется для обозначения отсутствия значения

print(bool(None))
print(bool('None'))

