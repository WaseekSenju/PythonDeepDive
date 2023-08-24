class Myclass:
    def say_hello():
        print('Hello World!')


my_obj = Myclass()

print(Myclass.say_hello)
print(my_obj.say_hello) #it is bound to the my_obj

# method is an actual object type

