def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('something happen before function is called')
        func()
        print('something happen after function is called')
    return wrapper


@my_decorator
def say_hello(name):
    print(f'Hello! {name}')


say_hello(name='Torokul')