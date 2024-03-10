def mydecorator(func):
    def wrapper():
        print("Boshlandi.")
        func()
        print("Tugadi.")
    return wrapper

@mydecorator
def say_hello():
    print("Salom!")

say_hello()
