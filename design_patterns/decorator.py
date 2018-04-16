def decorator(func):
    def inner(n):
        return func(n) + 1
    return inner


def first(n):
    return n + 1

first = decorator(first)


@decorator
def second(n):
    return n + 1


print(first(1))  # print 3
print(second(1))  # print 3
# ===============================================


def wrap_with_prints(func):
    # This will only happen when a function decorated
    # with @wrap_with_prints is defined
    print('wrap_with_prints runs only once')

    def wrapped():
        # This will happen each time just before
        # the decorated function is called
        print('About to run: %s' % func.__name__)
        # Here is where the wrapper calls the decorated function
        func()
        # This will happen each time just after
        # the decorated function is called
        print('Done running: %s' % func.__name__)

    return wrapped


@wrap_with_prints
def func_to_decorate():
    print('Running the function that was decorated.')


func_to_decorate()
print("================")
func_to_decorate()