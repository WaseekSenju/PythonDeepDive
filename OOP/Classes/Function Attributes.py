class Myclass:
    def say_hello(obj):
        print('Hello World!')


my_obj = Myclass()

#print(Myclass.say_hello)
#print(my_obj.say_hello) #it is bound to the my_obj

# method is an actual object type

class Person:
    language = 'Python'
    def hello(obj, name):
        print(f"hello {name}! I am {obj.language}")


p1 = Person()
p1.language = 'Dart'
#p1.hello('Waseek')

# ------------------------------Coding-------------------------------------------

class Person:
    def say_hello():
        print('Hello')

p = Person()
# print(hex(id(p)) )
#
#
# print(p.say_hello)
# print(type(p.say_hello) is type(Person.say_hello)) # the type is changed from functino to method

# p.say_hello() # it is bound to the method so python injects the p into method as aurgument

# -------------------------------------------------------------------------

class Person:
    def say_hello(*args):
        print('say_hello args :',args)

# Person.say_hello()


# p = Person()
# print(hex(id(p)))
# p.say_hello()

# -------------------------------------------------------------------------
class Person:
    def set_name(instance_obj,new_name):
        instance_obj.name = new_name



p = Person()
# p.set_name("Waseek")
# print(p.__dict__)
#
# Person.set_name(p,"Hassaan")
# print(p.__dict__)
# # -------------------------------------------------------------------------

class Person:
    def say_hello(self):
        print(f'{self} say Hello')

p =Person()

# p.say_hello()
# m_hello = p.say_hello
#
# print(m_hello.__func__) # now it has a handle at the class and it knows what to call
# print(m_hello.__self__) # its a pointer to p instance(what I am bound too)

# -------------------------------------------------------------------------

class Person:
    def say_hello(self):
        print(f'instance method called from :',self)


p = Person()

print(hex(id(p)))
p.say_hello()

Person.do_work = lambda self: f'do_work called from {self}'


print(Person.__dict__)
print(p.say_hello)
print(p.do_work) # we didn't redefine p but it got the do_work function

p.other_func = lambda *args: f'Other func called with {args}'

print(p.other_func(1,2,3))
print(p.other_func) # it is not bound to anything so be careful with it


print(p.other_func())