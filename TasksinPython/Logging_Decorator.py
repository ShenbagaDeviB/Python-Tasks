def logger(fun):
    def wrapper():
        print("Starting function!!!")
        fun()
        print("Function completed...")
    return wrapper
@logger
def welcome():
    print("Welcome to python!!")
welcome()