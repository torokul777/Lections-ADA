'==================================Миксины========================'
# Миксины это классы которые будут использоваться для насследования, но от миксинов не создаются обьекты

class FlyMixin():
    def fly(self):
        print('Я могу летать')
    

class WalkMixin():
    def walk(self):
        print('Я могу ходить')


class SwimMixin():
    def swim(self):
        print('Я могу плыть')
    

class Human(SwimMixin,WalkMixin):
    name = 'человек'
    
    def talk(self):
        print('Я могу говорить')
    


class Fish(SwimMixin):
    name = 'рыба'


class Dug(WalkMixin,FlyMixin,SwimMixin):
    name = 'утка'

objects = [Human(),Fish(),Dug()]

for object in objects:
    print(object.name)


    attrs = ['fly','swim','walk','talk']
    for attr in attrs:
        if hasattr(object,attr):
            method = getattr(object,attr)
            method()

obj1 = Human()
setattr(obj1,'new_attr','hello world')
print(obj1.new_attr)
print(dir(obj1))

# hasattr() - функция которая принимает обьект и название аттрибута. ВОзвращает True, 
# если у обьекта есть такой аттрибут(метод)

# getattr() - функция которая принимает обьект и название аттрибута Возвращает значение аттрибута

# setattr() - функция которай принимает обьект, название аттрибута и значение.
#добавляет в обьект новый аттрибут или перезапишет одноименный аттрибут
