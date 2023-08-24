class Program:
    language = "Python"

    def say_hello():
        print(f"Hello from {Program.language}")

p = Program()

print(p.__class__)

print(p.__dict__) # it's empty but may have attribute not visible here as p.__class__ is also available here

print(Program.__dict__)


