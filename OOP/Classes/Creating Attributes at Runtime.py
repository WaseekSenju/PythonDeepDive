#What if you want to create a method in an instace?

class MyClass:
    language = 'Python'

obj = MyClass()

from types import  MethodType

obj.say_hello = MethodType(lambda self:f'Hello {self.language}!' ,obj)

print(obj.say_hello())
print(hex(id(obj)))
print(hex(id(obj.say_hello)))
print(obj.say_hello)


#-----------------------------------------------------------------Coding------------------------------------------


class Person:
    pass


