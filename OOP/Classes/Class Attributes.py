class MyClass:
    language = 'Python'
    version = '3.9'

print(getattr(MyClass,'version'))
#it is equivalant to
print(MyClass.version)

# we can add attributes during runtime
MyClass.x = 100

# where state of a class is stored in python? IN a DICTIONARY!!

print(MyClass.__dict__)

del MyClass.x

print(MyClass.__dict__.items()) # prints list of tuples

