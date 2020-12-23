def func_open(func):
    def wrapper():
        print('hello!')
        return func
    return wrapper


@func_open
def func_close():
    return 1


print(func_close())