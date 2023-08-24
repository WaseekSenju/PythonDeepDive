class MyClass:
    language = 'Python'

my_obj = MyClass()

#print(my_obj.__dict__) # it's empty but it should have language?!

# but if we do

my_obj.language = 'Java'
#print(my_obj.__dict__)

# Now we have created language attribute in the namespace of the instance

# ------------------------------------------------------------------------------------------
class BankAccount:
    apr = 1.2

acc_1 = BankAccount()
acc_2 = BankAccount()

print(acc_1 is acc_2)

# Right now bot instances are empty

print(acc_1.__dict__,acc_2.__dict__)

# But python is dynamic we can add attributes in the class at runtime

BankAccount.account_type = 'Savings'

print(acc_1.account_type,acc_2.account_type)


acc_1.apr = 0
print(acc_1.__dict__)
print(acc_2.__dict__)
print(acc_1.apr, acc_2.apr)

setattr(acc_2, 'apr', 10)
print(getattr(acc_2, 'apr'))



