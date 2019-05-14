"""basic decorator stuff."""


def null_decorator(func):
    return func

"new function greet."


def greet():
    return 'Hello!'

greet = null_decorator(greet)

print(greet())


@null_decorator
def greet():
    return 'Holla!'

print(greet())

"new decorater"


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase

def greet():
    return 'Hello!'


print(greet())

print(greet)

print(null_decorator(greet))

print(uppercase(greet))
