class Myclass:
    language =  'Python'

    def say_hello():
        print('Hello world')

# all are same ways to do one thing
print(Myclass.__dict__)
print(Myclass.__dict__['say_hello']())
print(Myclass.__getattribute__(Myclass,'say_hello')())